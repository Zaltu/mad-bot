"""
VERY mad bot responding at incredibly hihg speeds
"""
from consts import BASIC_RETORTS, BUTT_INS, USERID


class Reactor(object):
    """
    Handles bot reactions to server activity
    """
    def __init__(self):
        self.message = ""

    def process(self, message):
        """
        Recieve and process text message

        :param str message: message to process

        :returns: any "regex" matched answers
        :rtype: str|None
        """
        self.message = message
        return self._pseudoRegex()

    def _isMentioned(self):
        """
        Check if the bot was mentioned in the message

        :returns: if the bot was @ed
        :rtype: bool
        """
        if USERID in self.message:
            return True
        return False

    def _pseudoRegex(self):
        """
        prioritize the types of responses. Not a real regex.

        :returns: forwards the text returns of each response type
        :rtype: str|None
        """
        if self._isMentioned():
            return self._retort() or self._beUseful()
        else:
            return self._butt()

    def _retort(self):
        """
        Finds any basic retorts

        :returns: retort
        :rtype: str|None
        """
        for snippet in BASIC_RETORTS:
            if snippet in self.message:
                return BASIC_RETORTS.get(snippet)

    def _butt(self):
        """
        Butts into conversations

        :returns: meme phrase
        :rtype: str|None
        """
        for snippet in BUTT_INS:
            if snippet in self.message:
                return BUTT_INS.get(snippet)

    def _beUseful(self):
        """
        Any real functionality returns from here

        :returns: useful answer to legit question
        :rtype: str|None
        """
        for snippet in BUTT_INS:
            if snippet in self.message:
                return BUTT_INS.get(snippet)
