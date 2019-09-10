"""
Master class of the MAD discord Bot
"""
from pprint import pprint as pp
from src.core.reactor import Reactor
from src.core.harmony import Harmony
from src.habits.habits import Habits

class MADBot():
    """
    Container class to hold all of the MAD Bot's functionality classes.
    """
    def __init__(self):
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
        print("\nAuthor")
        pp(delta.author.name)
        print("\nChannel")
        pp(delta.channel.name)
        print("\nContent")
        return self.mind.process(delta)


if __name__ == "__main__":
    MADBot()
