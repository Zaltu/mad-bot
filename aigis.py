"""
Main bot control center
"""
import json
import asyncio

from reactor import Mind
from harmony import DiscordSenses
from habits import Habits

class Aigis(object):
    """
    Aigis
    """
    def __init__(self):
        self.name = "Aigis"
        self.delta = "Aware"
        self.discordSenses = DiscordSenses(self, discordCreds())
        self.discordSenses.activate()
        #asyncio.run(test())
        self.mind = Mind(self)
        self.habits = Habits(self.discordSenses)

    def sense(self, context, delta):
        """
        Recieve and redirect a sensory input

        :param str context: bot recognized context
        :param obj delta: state change

        :returns: any response to the input from the context
        :rtype: obj
        """
        self.delta = delta
        return self.react(context, delta)

    def react(self, context, delta):
        """
        Activate the action in the context

        :param str context: bot recognized context
        :param obj delta: state change

        :returns: any response to the input from the context
        :rtype: obj
        """
        return self.mind.process(context, delta)


#async def test():
#    await self.discordSenses.send_message(destination=self.discordSenses.get_channel("337753641299738624"), content="testing")

def discordCreds():
    """
    Get the discord key from the secrets file.

    :returns: Discord Bot API auth key
    :rtype: str
    """
    with open('db/discordKey.json', 'r+') as secret:
        key = json.load(secret)["key"]
    return key


if __name__ == "__main__":
    A = Aigis()
