"""
VERY mad bot responding at incredibly hihg speeds
"""
from consts import USERID, COMMAND_KEYWORDS
from actions import Body

class Reactor(object):
    """
    Handles bot reactions to server activity
    """
    def __init__(self):
        self.body = Body()

    def process(self, text):
        """
        Filter for the incoming text message to parse it along Aigis' lines.

        :param str text: input text

        :returns: message to post, if applicable
        :rtype: str|None
        """
        # Set Body context
        self.body.vars['text'] = text

        words = set(text.split(" "))
        most = 0
        command = None
        for key in COMMAND_KEYWORDS:
            intNum = len(set(key.split(" ")).intersection(words))
            if len(key.split(" ")) == intNum and  most < intNum or (most == intNum and \
                    len(set(key.split(" "))) < len(set(command.split(" "))) if command else 0):
                most = intNum
                command = key

        if command:
            return COMMAND_KEYWORDS[command](self.body)


if __name__ == "__main__":
    R = Reactor()
    print(R.process("hewwo?"))
