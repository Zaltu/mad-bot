"""
Functions for all possible actions
"""
#pylint: disable=no-self-use
import random
import json
import os

import requests

from src.libs import backdoorgery

from src.consts import ADMINID, DBPATH

QUOTES_FILE = os.path.join(DBPATH, "quotes.json")
MADCRAFT_FILE = os.path.join(DBPATH, "ip.config")
TENOR_FILE = os.path.join(DBPATH, "tenor.secret")

TENOR_URL = "https://api.tenor.com/v1/search?q={keyword}&key={key}&limit=1&media_filter=minimal"


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
        terms = self.vars['text'].split(" ")[2:]
        if len(terms) < 2:
            return "`games` takes a {user} and a {console}"
        return backdoorgery.getConsoleMetrics(terms[0], terms[1])

    def gamecookie(self):
        """
        Show a random game from a user's backloggery

        :returns: a random game or the command syntax
        :rtype: str
        """
        terms = self.vars['text'].split(" ")[2:]
        if not len(terms):
            return "`cookie` takes a {user}"
        return backdoorgery.getFortuneCookie(terms[0])

    def quote(self):
        """
        Fetch a user's quote

        :returns: a quote or an appropriate error
        :rtype: str
        """
        try:
            quotee = self.vars['text'].split(" ")[2]
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
            quotee = terms[2]
            quote = " ".join(terms[3:])
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
        """
        Post instructions on connecting to the MC server

        :param str instructs: standard instructions to format

        :returns: instructions formatted with the connection IP
        :rtype: str
        """
        try:
            ip = None
            with open(MADCRAFT_FILE, 'r+') as ipfile:
                ip = ipfile.readline()
        except:  #pylint: disable=bare-except
            pass
        if not ip:
            return "No Madcraft set up in DB"
        return instructs.format(IP=ip)

    def aigif(self):
        """
        Searches for a (reasonably relevant) gif.
        Currently just from tenor. Might look into flavouring in the future

        String type return will eventually be deprecated in favor of
        download/clean workflow for cleaner responses

        :returns: Tenor gif URL
        :rtype: str
        """
        with open(TENOR_FILE, 'r') as secret_file:
            key = json.load(secret_file)['key']
        # Full text but pop the first element which should be the command
        keywords = " ".join(self.vars["text"].split(" ")[1:])

        tenor_san = requests.get(TENOR_URL.format(keyword=keywords, key=key)).json()
        return tenor_san['results'][0]['url']

    def kona(self):
        """
        Posts one of the top results for a specific set of keywords from konachan

        String type return will eventually be deprecated in favor of
        download/clean workflow for cleaner responses

        :returns: konachan image URL
        :rtype: str
        """
        keywords = " ".join(self.vars["text"].split(" ")[1:])
        return "NYI"
        #tenor_san = requests.get(TENOR_URL.format(keyword=keywords, key=key)).json()
        #return tenor_san['results'][0]['url']



if __name__ == "__main__":
    A = Actions()
