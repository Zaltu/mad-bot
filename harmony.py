from threading import Thread
from pprint import pprint as pp

import discord

import consts

DISCORD_CONTEXT = "Discord"

class DiscordSenses(discord.Client):
    """
    Discord API wrapper
    """
    def __init__(self, bot, token):
        self.token = token
        self.sigkill = False  # Warning! Dangerous!
        self.connectionThread = Thread(name="Start Thread", target=self._startConnection)
        self.bot = bot
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

    async def on_message(self, message):
        ### Temporary
        print("\nAuthor")
        pp(message.author.nick)
        pp(message.author.id)
        print("\nChannel")
        pp(message.channel.name)
        pp(message.channel.id)
        print("\nContent")
        pp(message.content)
        ###
        answer = self.bot.sense(DISCORD_CONTEXT, message)
        if answer and 'SIGKILL' in answer:
            print("SIGKILL sent")
            self._endConnection()
        elif answer:
            await self.send_message(message.channel, answer)
