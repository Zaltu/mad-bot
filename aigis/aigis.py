"""
Main bot control center
"""
from pprint import pprint as pp
from src.core.reactor import Reactor
from src.core.harmony import Harmony
from src.habits.habits import Habits

class Aigis():
    """
    Aigis
    """
    def __init__(self):
        self.name = "Aigis"
        self.delta = "Aware"
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
        pp(delta.content)
        self.delta = delta
        return self.mind.process(delta)


if __name__ == "__main__":
    Aigis()
