"""
Main bot control center
"""
# Disable pylint error since async non-def causes file to be percieved as erroneous
#pylint:disable=no-name-in-module
import json
import os

from src.core.reactor import Reactor
from src.core.harmony import Harmony
from src.core.habits import Habits

class Aigis(object):
    """
    Aigis
    """
    def __init__(self):
        self.name = "Aigis"
        self.delta = "Aware"
        self.harmony = Harmony(self.sense, discordCreds())
        self.harmony.activate()
        self.mind = Reactor(self)
        self.habits = Habits(self.harmony)

    def sense(self, delta):
        """
        Recieve and redirect a sensory input

        :param obj delta: state change

        :returns: any response to the input from the context
        :rtype: obj
        """
        self.delta = delta
        return self.react(delta)

    def react(self, delta):
        """
        Activate the action in the context

        :param obj delta: state change

        :returns: any response to the input from the context
        :rtype: obj
        """
        return self.mind.process(delta)


def discordCreds():
    """
    Get the discord key from the secrets file.

    :returns: Discord Bot API auth key
    :rtype: str
    """
    from src.consts import DBPATH
    with open(os.path.join(DBPATH, 'discordKey.json'), 'r+') as secret:
        key = json.load(secret)["key"]
    return key


if __name__ == "__main__":
    Aigis()
