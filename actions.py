"""
Functions for all possible actions
"""
import random
import backdoorgery


class DiscordBody(object):
    """
    Possible 'actions' the bot may take.
    """
    def __init__(self, mind):
        self.mind = mind
        self.vars = {}

    def interface(self, command):
        """
        Call the given command

        :returns: the result of the command
        :rtype: obj
        """
        return command()

    def text(self, text):
        """
        1 Billion IQ Developer

        :param str text: the text to return

        :returns: the text param
        :rtype: str
        """
        return text.format(author=self.vars['author'],
                           channel=self.vars['channel'],
                           input=self.vars['input'])

    def nyx(self):
        """
        Generate a random Nyx quote

        :returns: one of Nyx's final battle quotes.
        :rtype: str
        """
        return random.sample({
            "Celebrate life's grandeur. Its brilliance. Its magnificence.",
            "There is both joy and wonder in coming to understand another.",
        }, 1)[0]

    def owo(self):
        """
        NYI
        See Sagiri's owo command implementation

        :returns: "OwO"
        :rtype: str
        """
        return "OwO"

    def games(self):
        """
        Show some stats based off of a user and a console

        :returns: the command terms if improperly called or a user's console metrics
        :rtype: str
        """
        terms = self.vars['text'].split(" ")[1:]
        if len(terms) < 2:
            return ".games takes a {user} and a {console}"
        return backdoorgery.getConsoleMetrics(terms[0], terms[1])
