"""
Functions for all possible actions
"""
import random
import json
import os

from src.libs import backdoorgery

from src.consts import ADMINID, DBPATH

QUOTES_FILE = os.path.join(DBPATH, "quotes.json")
MADCRAFT_FILE = os.path.join(DBPATH, "ip.json")


class Actions(object):
    """
    Possible 'actions' the bot may take.
    """
    def __init__(self):
        self.vars = {}

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

    def owo(self):
        """
        NYI
        See Sagiri's owo command implementation

        :returns: lowogi
        :rtype: str
        """
        return "<:lowogi:510216907987746819>"

    def sigkill(self):
        """
        Send a DC signal to DiscordSenses

        :returns: a dc signal
        :rtype: str
        """
        if self.vars["input"].author.id in ADMINID:
            return "SIGKILL"
        return "You can't tell me what to do."

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

    def gamecookie(self):
        """
        Show a random game from a user's backloggery

        :returns: a random game or the command syntax
        :rtype: str
        """
        terms = self.vars['text'].split(" ")[1:]
        if not len(terms):
            return ".cookie takes a {user}"
        return backdoorgery.getFortuneCookie(terms[0])

    def quote(self):
        """
        Fetch a user's quote

        :returns: a quote or an appropriate error
        :rtype: str
        """
        try:
            quotee = self.vars['text'].split(" ")[1]
        except (KeyError, IndexError):
            return "No one to quote"
        with open(QUOTES_FILE, 'r+') as quote_file:
            quotes = json.load(quote_file)

        try:
            userquotes = quotes[quotee]
        except KeyError:
            return "{user} has no registered quotes".format(user=quotee)
        return random.sample(userquotes, 1)[0]

    def addquote(self):
        """
        Add a quote to a user's quote bank

        :returns: confirmation of receipt
        :rtype: str
        """
        terms = self.vars["text"].split(" ")
        try:
            quotee = terms[1]
            quote = " ".join(terms[2:])
        except (KeyError, IndexError):
            return "Woah there son, you aren't even quoting anything."
        formattedQuote = quote + "\n        - " + quotee
        with open(QUOTES_FILE, 'r+') as quote_file:
            quotes = json.load(quote_file)
        if quotee in quotes:
            quotes[quotee].append(formattedQuote)
        else:
            quotes.setdefault(quotee, [formattedQuote])
        with open(QUOTES_FILE, 'w+') as quote_file:
            quote_file.write(json.dumps(quotes))

        return "I'll remember that."

    def madcraft(self, instructs):
        try:
            ip = None
            with open(MADCRAFT_FILE, 'r+') as ipfile:
                ip = ipfile.readline()
        except:
            pass
        if not ip:
            return "No Madcraft set up in DB"
        return instructs.format(IP=ip)



if __name__ == "__main__":
    A = Actions()
    print(A.madcraft("{IP}"))