from threading import Thread
from pprint import pprint as pp

import discord

import consts
from reactor import Reactor


class Harmony(discord.Client):
    """
    Discord API wrapper
    """
    def __init__(self, token):
        self.token = token
        self.sigkill = False  # Warning! Dangerous!
        self.connectionThread = Thread(name="Start Thread", target=self._startConnection)
        self.endConnectionThread = Thread(name="End Thread", target=self._endConnection)
        self.reactor = Reactor()
        super().__init__()

    def activate(self):
        """
        Bring bot online
        """
        self.connectionThread.start()
        self.endConnectionThread.start()

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
        while not self.sigkill:
            pass
        self.loop.stop()
        while self.loop.is_running():
            pass
        self.loop.run_until_complete(self.logout())

    def _sanitizeMessage(self, message):
        return message.lower()

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
        cleaned = self._sanitizeMessage(message.content)
        answer = self.reactor.process(cleaned)
        if answer and 'SIGKILL' in answer:
            print("SIGKILL sent")
            self.sigkill = True
        elif answer:
            answer = answer.format(author="<@!"+message.author.id+">")
            await self.send_message(message.channel, answer)


if __name__ == "__main__":
    H = Harmony('')
    H.activate()
