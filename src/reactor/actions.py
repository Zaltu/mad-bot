"""
Functions for all possible actions
"""
import random
import json
import os
import re

import requests
import wikipedia

import aigis

from src.consts import AIGISID, ADMINID, DBPATH
from src.actions.commands import LUIGIHANDS, LOWOGI, COMMAND_KEYWORDS

QUOTES_FILE = os.path.join(DBPATH, "quotes.json")
MADCRAFT_FILE = os.path.join(DBPATH, "ip.config")
TENOR_FILE = os.path.join(DBPATH, "tenor.secret")

TENOR_URL = "https://api.tenor.com/v1/search?q={keyword}&key={key}&limit=1&media_filter=minimal"
KONA_URL = "https://konachan.com/post.json?page=1&limit=1&tags={tags}"
BOORU_URL = "https://danbooru.donmai.us/posts.json?limit=1&page=1&tags={tags}"
GEL_URL = "https://gelbooru.com//index.php?page=dapi&s=post&q=index&json=1&pid=1&limit=1&tags={tags}"



class Reactor():
    """
    Possible 'actions' the bot may take.

    :param Aigis bot: parent bot containing app features.
    """
    def __init__(self, bot):
        self.vars = {}
        self.parent = bot
        self.post = lambda mess: self.parent.harmony.sendMessage(self.vars['channel'], mess)

    def process(self, delta):
        """
        Filter for the incoming text message to parse it along Aigis' lines.

        :param str delta: explicit input
        """
        if delta.author.id == AIGISID:
            # Ignore self-driven actions
            return

        # Set Body context
        self.vars = {
            'text': delta.content,
            'channel': delta.channel,
            'author': "<@!%s>" % delta.author.id,
            'input': delta
        }
        words = re.sub("[!#$,':;?]", '', delta.content.lower())
        words = set(words.split(" "))
        most = 0
        command = None
        for key in COMMAND_KEYWORDS:
            intNum = len(set(key.split(" ")).intersection(words))
            if len(key.split(" ")) == intNum and  most < intNum or (most == intNum and \
                    len(set(key.split(" "))) < len(set(command.split(" "))) if command else 0):
                most = intNum
                command = key

        if command:
            COMMAND_KEYWORDS[command](self)

    def text(self, text):
        """
        1 Billion IQ Developer

        :param str text: the text to return
        """
        print(self.vars)
        self.post(text.format(author=self.vars['author'],
                              channel=self.vars['channel'],
                              input=self.vars['input']))

    def owo(self):
        """
        NYI
        See Sagiri's owo command implementation
        """
        self.post("Nyaat yet impwemented " + LOWOGI)

    def sigkill(self):
        """
        Send a DC signal to DiscordSenses
        """
        if self.vars["input"].author.id in ADMINID:
            self.parent.harmony.sigkill()
        self.post("You can't tell me what to do.")

    def games(self):
        """
        Show some stats based off of a user and a console
        """
        terms = self.vars['text'].split(" ")[1:]
        if len(terms) < 2:
            self.post("`games` takes a {user} and a {console}")
        self.post(aigis.backloggery.getConsoleMetrics(terms[0], terms[1]))

    def gamecookie(self):
        """
        Show a random game from a user's backloggery
        """
        terms = self.vars['text'].split(" ")[1:]
        if not terms:
            self.post("`cookie` takes a {user}")
        self.post(aigis.backloggery.getFortuneCookie(terms[0]))

    def quote(self):
        """
        Fetch a user's quote
        """
        try:
            quotee = self.vars['text'].split(" ")[1]
        except (KeyError, IndexError):
            self.post("No one to quote")
        with open(QUOTES_FILE, 'r+') as quote_file:
            quotes = json.load(quote_file)
        try:
            userquotes = quotes[quotee]
        except KeyError:
            self.post("{user} has no registered quotes".format(user=quotee))
        self.post(random.sample(userquotes, 1)[0])

    def addquote(self):
        """
        Add a quote to a user's quote bank
        """
        terms = self.vars["text"].split(" ")
        try:
            quotee = terms[1]
            quote = " ".join(terms[2:])
        except (KeyError, IndexError):
            self.post("Woah there son, you aren't even quoting anything.")
        formattedQuote = quote + "\n        - " + quotee
        with open(QUOTES_FILE, 'r+') as quote_file:
            quotes = json.load(quote_file)
        if quotee in quotes:
            quotes[quotee].append(formattedQuote)
        else:
            quotes.setdefault(quotee, [formattedQuote])
        with open(QUOTES_FILE, 'w+') as quote_file:
            quote_file.write(json.dumps(quotes, indent=4))

        self.post("I'll remember that.")

    def madcraft(self, instructs):
        """
        Post instructions on connecting to the MC server

        :param str instructs: standard instructions to format
        """
        try:
            ip = None
            with open(MADCRAFT_FILE, 'r+') as ipfile:
                ip = ipfile.readline()
        except:  #pylint: disable=bare-except
            pass
        if not ip:
            self.post("No Madcraft set up in DB")
        self.post(instructs.format(IP=ip))

    def aigif(self):
        """
        Searches for a (reasonably relevant) gif.
        Currently just from tenor. Might look into flavouring in the future

        String type return will eventually be deprecated in favor of
        download/clean workflow for cleaner responses
        """
        with open(TENOR_FILE, 'r') as secret_file:
            key = json.load(secret_file)['key']
        # Full text but pop the first element which should be the command
        keywords = " ".join(self.vars["text"].split(" ")[1:])

        tenor_san = requests.get(TENOR_URL.format(keyword=keywords, key=key)).json()
        self.post(tenor_san['results'][0]['url'])

    def weeb(self):
        """
        Posts one of the top results for a specific set of keywords from
        a booru. Search order is Konachan -> Danbooru -> Gelbooru

        NOT sfw filtered... Partially cause I'm not sure I know how.

        String type return will eventually be deprecated in favor of
        download/clean workflow for cleaner responses
        """
        # Full text but pop the first element which should be the command
        keywords = self.vars["text"].split(" ")
        tags = "+".join(keywords[1:])
        self.post(_kona(tags) or _booru(tags) or _gel(tags) or "No results " + LUIGIHANDS)

    def wiki(self):
        """
        Posts the summary of an article matching the search terms from Wikipedia.
        """
        keywords = self.vars["text"].split(" ")
        terms = " ".join(keywords[1:])
        try:
            self.post(wikipedia.summary(terms))
        except wikipedia.exceptions.PageError:
            self.post("No article found matching the term \"{}\"".format(terms))

    def dndspell(self):
        """
        Fetch the description of a spell from D&D 5e
        """
        spellname = " ".join(self.vars["text"].split(" ")[1:])
        desc = aigis.dnd.get_spell_desc(spellname)
        self.post(desc if desc else "No spell found matching \"%s\"" % spellname)

    def translator(self):
        """
        Translate some text to a given language.
        """
        textlist = self.vars["text"].split(" ")
        tl = textlist[1]
        try:
            translated = aigis.translation.translate(" ".join(textlist[2:]), target_lang=tl)
        except aigis.translation.BadLanguageError as e:
            translated = str(e)
        self.post(translated)


def _kona(tags):
    """
    Fetch image from konachan

    :param str tags: tags to search for

    :returns: image URL
    :rtype: str
    """
    kona_chan = requests.get(KONA_URL.format(tags=tags)).json()
    if kona_chan:
        return kona_chan[0]['file_url']
    return None


def _booru(tags):
    """
    Fetch image from danbooru

    :param str tags: tags to search for

    :returns: image URL
    :rtype: str
    """
    booru_chan = requests.get(BOORU_URL.format(tags=tags)).json()
    if booru_chan:
        return booru_chan[0]['file_url']
    return None


def _gel(tags):
    """
    Fetch image from gelbooru

    :param str tags: tags to search for

    :returns: image URL
    :rtype: str
    """
    try:
        gel_chan = requests.get(GEL_URL.format(tags=tags)).json()
    except json.decoder.JSONDecodeError:
        gel_chan = None
    if gel_chan:
        return gel_chan[0]['file_url']
    return None