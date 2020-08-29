"""
Master class of the MAD discord Bot
"""
import logging

from src.reactor.actions import Reactor
from src.core.harmony import Harmony
from src.habits.habits import Habits

class MADBot():
    """
    Container class to hold all of the MAD Bot's functionality classes.
    """
    def __init__(self):
        self.logger = logging.getLogger("MADBot")
        #self.logger.setLevel(logging.INFO)
        self.harmony = Harmony(on_message_callback=self.react)
        self.reactor = Reactor(self)
        self.harmony.activate()
        self.habits = Habits(self.harmony)

    async def react(self, delta):
        """
        React to a sensory input.

        :param obj delta: state change

        :returns: any response to the input from the context
        :rtype: obj
        """
        print(delta.channel.id)
        return await self.reactor.process(delta)


def launch():
    """
    Launch function as defined by AIGIS conventions.
    """
    MADBot()
