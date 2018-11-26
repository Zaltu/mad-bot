"""
VERY mad bot responding at incredibly hihg speeds
"""
from consts import COMMAND_KEYWORDS, CONTEXT_MAP
from actions import DiscordBody

class Mind(object):
    """
    Handles bot reactions to server activity

    :param obj bot: the bot that handles the body and mind
    """
    def __init__(self, bot):
        self.parent = bot

    def process(self, context, delta):
        """
        Filter for the incoming text message to parse it along Aigis' lines.

        :param str context: input context
        :param str delta: explicit input

        :returns: message to post, if applicable
        :rtype: str|None
        """
        #try:
        return CONTEXT_MAP[context](self, delta)
        #except KeyError:
        #    return "I don't know what a {context} is... :(".format(context=context)

    def _processDiscord(self, delta):
        """
        Discord context processor
        Currently only processes text inputs

        :param obj delta: a discord input object

        :returns: If delta was reacted to properly.
        :rtype: bool
        """

        body = DiscordBody(self)

        # Set Body context
        body.vars = {
            'text': delta.content,
            'channel': delta.channel,
            'author': "<@!"+delta.author.id+">",
            'input': "N/A"
        }

        words = set(delta.content.lower().split(" "))
        most = 0
        command = None
        for key in COMMAND_KEYWORDS:
            intNum = len(set(key.split(" ")).intersection(words))
            if len(key.split(" ")) == intNum and  most < intNum or (most == intNum and \
                    len(set(key.split(" "))) < len(set(command.split(" "))) if command else 0):
                most = intNum
                command = key

        if command:
            return COMMAND_KEYWORDS[command](body)
