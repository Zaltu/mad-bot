"""
VERY mad bot responding at incredibly hihg speeds
"""
import re

from src.actions.commands import COMMAND_KEYWORDS
from src.actions.actions import Actions
from src.consts import AIGISID

class Reactor(object):
    """
    Handles bot reactions to server activity

    :param obj bot: the bot that handles the body and mind
    """
    def __init__(self, bot):
        self.parent = bot
        self.body = Actions(bot)

    def process(self, delta):
        """
        Filter for the incoming text message to parse it along Aigis' lines.

        :param str delta: explicit input
        """
        if delta.author.id == AIGISID:
            # Ignore self-driven actions
            return

        # Set Body context
        self.body.vars = {
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
            COMMAND_KEYWORDS[command](self.body)
