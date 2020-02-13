"""
Mad bot wrapper around the discord python API
"""
#pylint: disable=missing-yield-doc,missing-yield-type-doc
from threading import Thread
import os
import json
import asyncio

import discord

from src.consts import DBPATH


MAX_LENGTH_MESSAGE = 1900

class Harmony(discord.Client):
    """
    Discord API wrapper

    :param function on_message_callback: optionally immediately set the callback for received messages
    """
    def __init__(self, on_message_callback=None):
        self.token = discordCreds()
        self.connectionThread = Thread(name="Start Thread", target=self._startConnection)
        self.endConnectionThread = Thread(name="End Thread", target=self._endConnection)
        self.on_message_callback = on_message_callback or default_on_message
        super().__init__()

    def activate(self):
        """
        Bring bot online
        """
        self.connectionThread.start()

    def _startConnection(self):
        """
        Start discord connection
        """
        try:
            self.loop.run_until_complete(self.start(self.token))
        except RuntimeError as e:
            if "Event loop stopped before Future completed." not in str(e):
                print(e)

    def _endConnection(self):
        """
        Ends the connection and should log off/close the websocket
        """
        self.loop.stop()
        while self.loop.is_running():
            pass
        self.loop.run_until_complete(self.logout())

    def set_on_message_callback(self, callback):
        """
        Set function to be called when receiving a message

        :param function callback: function to call when receiving messages
        """
        self.on_message_callback = callback

    async def on_message(self, message):
        """
        Process messages received from discord.

        :param discord.message message: message received
        """
        self.on_message_callback(message)

    async def aSendMessage(self, channel, message):
        """
        Async Send a message to a given channel

        :param discord.channel channel: channel to send the message to
        :param str message: message to send
        """
        for chunk in _chunksToMaxChars(message):
            await channel.send(chunk)

    def sendMessage(self, channel, message):
        """
        Non-async wrapper for sending a message to a channel.
        Call is still made in async, but the event loop wrapper is handled for you.

        :param discord.channel channel: channel to send the message to
        :param str message: message to send
        """
        asyncio.ensure_future(self.aSendMessage(channel, message))

    async def aSendFile(self, channel, afile, text):
        """
        Upload file to given channel

        :param discord.channel channel: channel to send the message to
        :param str afile: path to file to upload
        :param str text: message to send
        """
        await channel.send(text, file=discord.File(afile))

    def sendFile(self, channel, afile, text=""):
        """
        Non-async wrapper for uploading a file to a channel.
        Call is still made in async, but the event loop wrapper is handled for you.

        :param discord.channel channel: channel to send the message to
        :param str afile: path to file to upload
        :param str text: message to send
        """
        asyncio.ensure_future(self.aSendFile(channel, afile, text))


    def sigkill(self):
        """
        End the connection gracefully.
        """
        self.endConnectionThread.start()


def discordCreds():
    """
    Get the discord key from the secrets file.

    :returns: Discord Bot API auth key
    :rtype: str
    """
    with open(os.path.join(DBPATH, 'discordKey.secret'), 'r+') as secret:
        key = json.load(secret)["key"]
    return key


def default_on_message(message):  #pylint: disable=unused-argument
    """
    By default, does nothing.

    :param discord.message message: the message received
    """
    return None



def _chunksToMaxChars(message):
    """
    Discord accepts up to 2000 characters in a single message.
    This creates an iterator splitting a string into chunks of acceptable length.
    This function is NOT EFFICIENT.

    :param str message: string to truncate

    :yields: chunked string to 1900 characters, ceilinged to the nearest word.
    :yieldtype: str
    """
    # Most messages should be under the limit, let's be at least a little efficient here...
    if len(str(message)) < MAX_LENGTH_MESSAGE:
        yield message
        return
    splitstr = message.split(" ")
    i = 0
    while i < len(splitstr):
        beginOffset = i
        while len(" ".join(splitstr[beginOffset:i])) < MAX_LENGTH_MESSAGE and i < len(splitstr):
            i += 1
        yield " ".join(splitstr[beginOffset:i])
