"""
Master class of the MAD discord Bot
"""
import logging

from src.core.reactor import Reactor
from src.core.harmony import Harmony
from src.habits.habits import Habits

class MADBot():
    """
    Container class to hold all of the MAD Bot's functionality classes.

    :param logging.logger logger: a parent logger, optional
    """
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger("MADBot")
        self.harmony = Harmony(on_message_callback=self.react)
        self.harmony.activate()
        self.mind = Reactor(self)
        self.habits = Habits(self.harmony)

    def react(self, delta):
        """
        React to a sensory input.

        :param obj delta: state change

        :returns: any response to the input from the context
        :rtype: obj
        """
        logtext = """Author:
        {}
        Channel:
        {}
        Content:
        {}""".format(delta.author.nick, delta.channel.name, delta.content)
        self.logger.info(logtext)
        return self.mind.process(delta)


def launch(logger):
    """
    Launch function as defined by AIGIS conventions.

    :param logging.logger logger: a parent logger provided by AIGIS
    """
    MADBot(logger)
