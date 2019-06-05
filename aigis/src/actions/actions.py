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

from src.actions.commands import LUIGIHANDS, LOWOGI

QUOTES_FILE = os.path.join(DBPATH, "quotes.json")
MADCRAFT_FILE = os.path.join(DBPATH, "ip.config")
TENOR_FILE = os.path.join(DBPATH, "tenor.secret")

TENOR_URL = "https://api.tenor.com/v1/search?q={keyword}&key={key}&limit=1&media_filter=minimal"
KONA_URL = "https://konachan.com/post.json?page=1&limit=1&tags={tags}"
BOORU_URL = "https://danbooru.donmai.us/posts.json?limit=1&page=1&tags={tags}"
GEL_URL = "https://gelbooru.com//index.php?page=dapi&s=post&q=index&json=1&pid=1&limit=1&tags={tags}"



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
        print(self.vars)
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
        return "Nyaat yet impwemented " + LOWOGI

    def sigkill(self):
        """
        Send a DC signal to DiscordSenses

        :returns: a dc signal
        :rtype: str
        """
        print(self.vars["input"].author.id)
        if self.vars["input"].author.id in ADMINID:
            return "SIGKILL"
        return "You can't tell me what to do."

    def games(self):
        """
        Show some stats based off of a user and a console

        :returns: the command terms if improperly called or a user's console metrics
        :rtype: str
        """
        print(self.vars["text"])
        terms = self.vars['text'].split(" ")[1:]
        print(terms)
        if len(terms) < 2:
            return "`games` takes a {user} and a {console}"
        return backdoorgery.getConsoleMetrics(terms[0], terms[1])

    def gamecookie(self):
        """
        Show a random game from a user's backloggery

        :returns: a random game or the command syntax
        :rtype: str
        """
        terms = self.vars['text'].split(" ")[1:]
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

    def weeb(self):
        """
        Posts one of the top results for a specific set of keywords from
        a booru. Search order is Konachan -> Danbooru -> Gelbooru

        NOT sfw filtered... Partially cause I'm not sure I know how.

        String type return will eventually be deprecated in favor of
        download/clean workflow for cleaner responses

        :returns: danbooru image URL
        :rtype: str
        """
        # Full text but pop the first element which should be the command
        keywords = self.vars["text"].split(" ")
        tags = "+".join(keywords[1:])
        return _kona(tags) or _booru(tags) or _gel(tags) or "No results " + LUIGIHANDS


def _kona(tags):
    kona_chan = requests.get(KONA_URL.format(tags=tags)).json()
    if kona_chan:
        return kona_chan[0]['file_url']
    return None


def _booru(tags):
    booru_chan = requests.get(BOORU_URL.format(tags=tags)).json()
    if booru_chan:
        return booru_chan[0]['file_url']
    return None


def _gel(tags):
    try:
        gel_chan = requests.get(GEL_URL.format(tags=tags)).json()
    except json.decoder.JSONDecodeError:
        gel_chan = None
    if gel_chan:
        return gel_chan[0]['file_url']
    return None



if __name__ == "__main__":
    # Doesnt work cause python luigihands
    A = Actions()
    A.vars = {"text":".weeb luigi"}
    print(A.weeb())
