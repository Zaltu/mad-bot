"""
Main bot control center
"""
from reactor import Mind
from harmony import DiscordSenses

class Aigis(object):
    """
    Aigis
    """
    def __init__(self):
        self.name = "Aigis"
        self.delta = "Aware"
        self.discordSenses = DiscordSenses(self, '')
        self.discordSenses.activate()
        self.mind = Mind(self)

    def sense(self, context, delta):
        self.delta = delta
        return self.react(context, delta)

    def react(self, context, delta):
        return self.mind.process(context, delta)



if __name__ == "__main__":
    A = Aigis()
