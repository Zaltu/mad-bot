"""
Functions for all possible actions
"""
import asyncio
import random
import json
import glob
import os
import re

import requests
import wikipedia
import youtube_dl

import aigis

from src.consts import AIGISID, ADMINID, DBPATH
from src.reactor.commands import LUIGIHANDS, LOWOGI, COMMAND_KEYWORDS
from src.reactor import minesweeper

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
        self.delta = {}
        self.parent = bot
        self.post = lambda mess: self.parent.harmony.sendMessage(self.delta['channel'], mess)
        self.postfile = lambda mess, afile: self.parent.harmony.sendFile(self.delta['channel'], mess, afile)

    def process(self, full_delta):
        """
        Filter for the incoming text message to parse it along Aigis' lines.

        :param str full_delta: explicit input
        """
        # Set Body context
        self.delta = {
            'text': " ".join(full_delta.content.split(" ")[1:]),
            'channel': full_delta.channel,
            'author': "<@!%s>" % full_delta.author.id,
            'input': full_delta,
            'command': full_delta.content.split(" ")[0]
        }
        words = re.sub("[!#$,':;?]", '', full_delta.content.lower())
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
            self.parent.logger.info("Responding to command: %s", command)
            COMMAND_KEYWORDS[command](self)

    def text(self, text):
        """
        1 Billion IQ Developer

        :param str text: the text to return
        """
        self.post(text.format(author=self.delta['author'],
                              channel=self.delta['channel'],
                              input=self.delta['input']))

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
        if self.delta["input"].author.id in ADMINID:
            self.parent.harmony.sigkill()
            return
        self.post("You can't tell me what to do.")

    def reload_plugin(self):
        """
        Request the AIGIS core to reload a plugin.
        Somewhat dangerous...
        """
        if self.delta["input"].author.id in ADMINID:
            aigis.AIGISReload(self.delta["text"])
            return
        self.post("You can't tell me what to do.")

    def games(self):
        """
        Show some stats based off of a user and a console
        """
        terms = self.delta['text'].split(" ")
        if len(terms) < 2:
            self.post("`games` takes a {user} and a {console}")
        self.post(aigis.backloggery.getConsoleMetrics(terms[0], terms[1]))

    def gamecookie(self):
        """
        Show a random game from a user's backloggery
        """
        terms = self.delta['text'].split(" ")
        if not terms:
            self.post("`cookie` takes a {user}")
        self.post(aigis.backloggery.getFortuneCookie(terms[0]))

    def quote(self):
        """
        Fetch a user's quote
        """
        try:
            quotee = self.delta['text']
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
        terms = self.delta["text"].split(" ")
        try:
            quotee = terms[0]
            quote = " ".join(terms[1:])
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
        keywords = self.delta["text"]

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
        tags = "+".join(self.delta["text"].split(" "))
        self.post(_kona(tags) or _booru(tags) or _gel(tags) or "No results " + LUIGIHANDS)

    def wiki(self):
        """
        Posts the summary of an article matching the search terms from Wikipedia.
        """
        keywords = self.delta["text"].split(" ")
        terms = " ".join(keywords)
        try:
            self.post(wikipedia.summary(terms))
        except wikipedia.exceptions.PageError:
            self.post("No article found matching the term \"{}\"".format(terms))

    def dndspell(self):
        """
        Fetch the description of a spell from D&D 5e
        """
        spellname = self.delta["text"]
        desc = aigis.dnd.get_spell_desc(spellname)
        self.post(desc if desc else "No spell found matching \"%s\"" % spellname)

    def translator(self):
        """
        Translate some text to a given language.
        """
        with self.delta['channel'].typing():
            textlist = self.delta["text"].split(" ")
            tl = textlist[0]
            try:
                translated = aigis.translation.translate(" ".join(textlist[1:]), target_lang=tl)
            except aigis.translation.BadLanguageError as e:
                translated = str(e)
            self.post(translated)

    def getaudio(self):
        """
        Download an audio file and upload it to the channel.
        Basically, used to rip audio files.
        """
        filepath = os.path.join(DBPATH, 'ytdl-out', '%(title)s.%(ext)s')
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': filepath,
            'max_filesize': 1073741824,  # 1GB, not lg
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3'
            }],
            'logger': self.parent.logger
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([self.delta['text']])
            except youtube_dl.utils.DownloadError as e:
                self.parent.logger.error(str(e))
                self.post("Unexpected error occured, sorry...")
                return
        fp = glob.glob(os.path.join(DBPATH, 'ytdl-out', '*'))[0]  # There's only one I hope
        self._clean_async_file_upload(fp)

    def genesis(self):
        """
        Generate stuff using AIGIS.generate.
        """
        requestAttr = self.delta["text"].split(" ")[0]
        kwargs = _genesis_args(self.delta["text"].split(" ")[1:])
        try:
            generator = getattr(aigis.generate, requestAttr)
        except AttributeError:
            # No valid genesis for this attr
            self.post("No generator exists for %s" % requestAttr)
        try:
            created = generator(**kwargs)
            if os.path.exists(created):
                self._clean_async_file_upload(created)
            else:
                self.post(created)
        except (TypeError, KeyError):
            self.post("Unrecognized argument in\n%s" % kwargs)
    
    def aitext(self):
        """
        Auto-generate ML text using genesis AIText (wrapper).
        """
        try:
            created = aigis.generate.text(self.delta["text"], random.randint(10, 75))
            self.post(created)
        except Exception:  #pylint: disable=broad-except
            self.post("Unknown error occured, and process halted to preserve RAM.")

    def furi(self):
        """
        Convert japanese text to furigana (for educational purposes).
        """
        self.post(
            aigis.japanese.to_furigana(self.delta["text"])
        )

    def minesweeper(self):
        """
        Let's play some minesweeper comrades!
        """
        try:
            dim = int(self.delta["text"])
        except (ValueError, TypeError):
            dim = 5
        self.post(
            minesweeper.getMineField(dim, dim)
        )

    def _clean_async_file_upload(self, fp, text="Here you go!"):
        async def wrapper():
            """
            Make sure the deletion of the temp file happens after the file is sent...
            """
            await self.parent.harmony.aSendFile(self.delta['channel'], fp, text)
            # Cleanup so we don't have shit hanging around forever
            os.remove(fp)
        asyncio.ensure_future(wrapper())

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

def _genesis_args(args):
    """
    Split potential genesis args into an actual key dict

    :param list args: list of received arguments

    :returns: k-v paired arguments
    :rtype: dict
    """
    res = {}
    n=0
    try:
        while n < len(args):
            t = args[n]
            while n+1 !=len(args) and "=" not in args[n+1]:
                n+=1
                t = " ".join([t]+[args[n]])
            n+=1
            y = t.split("=")
            res[y[0]] = y[1]
    except Exception:  #pylint: disable=broad-except
        return {}
    return res
