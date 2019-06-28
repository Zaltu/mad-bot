"""
Mad bot wrapper around the discord python API
"""
from threading import Thread
from pprint import pprint as pp
import os
import json
import asyncio

import discord

from src.consts import DBPATH


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
        await channel.send(message)

    def sendMessage(self, channel, message):
        """
        Non-async wrapper for sending a message to a channel.
        Call is still made in async, but the event loop wrapper is handled for you.

        :param discord.channel channel: channel to send the message to
        :param str message: message to send
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.aSendMessage(channel, message))

    async def aSendFile(self, channel, file):
        """
        NYI
        Upload file to given channel
        """

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


def default_on_message(message):
    """
    By default, log all messages recieved.

    :param discord.message message: the message received

    :returns: empty string because pylint hates None
    :rtype: evaluates to false
    """
    print("\nAuthor")
    pp(message.author.nick)
    pp(message.author.id)
    print("\nChannel")
    pp(message.channel.name)
    print("\nContent")
    pp(message.content)
    return ""
