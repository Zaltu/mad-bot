"""
Functions for all possible actions
"""
import random


class Body(object):

    def __init__(self):
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
        return text

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
        terms = self.vars['text'].split(" ")[1:]
        return terms
