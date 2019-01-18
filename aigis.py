"""
Main bot control center
"""
import json
import schedule

from reactor import Mind
from harmony import DiscordSenses
import habits

class Aigis(object):
    """
    Aigis
    """
    def __init__(self):
        self.name = "Aigis"
        self.delta = "Aware"
        self.discordSenses = DiscordSenses(self, discordCreds())
        self.discordSenses.activate()
        self.mind = Mind(self)

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

    def routine(self):
        """
        Define certain actions to be done routinely, independant of input
        """
        for habit in habits.DAILY:
            schedule.every().day.at("20:30").do(lambda job=habit: job(self.discordSenses))
        schedule.run_pending()


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
