"""
Main bot control center
"""
# Disable pylint error since async non-def causes file to be percieved as erroneous
#pylint:disable=no-name-in-module

from src.core.reactor import Reactor
from src.core.harmony import Harmony
from src.habits.habits import Habits

class Aigis(object):
    """
    Aigis
    """
    def __init__(self):
        self.name = "Aigis"
        self.delta = "Aware"
        self.harmony = Harmony(self.react)
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
        self.delta = delta
        return self.mind.process(delta)


if __name__ == "__main__":
    Aigis()
