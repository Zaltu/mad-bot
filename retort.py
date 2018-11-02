"""
VERY mad bot responding at incredibly hihg speeds
"""
from consts import BASIC_RETORTS, BUTT_INS, USERID


class Reactor(object):

    def __init__(self, botname):
        self.botname = botname
        self.message = ""

    def _isMentioned(self):
        if USERID in self.message:
            return True
        return False


    def pseudoRegex(self):
        if self._isMentioned():
            return self.retort() or self.beUseful()
        else:
            return self.butt()

    def retort(self):
        for answerTo in BASIC_RETORTS:
            if answerTo in self.message:
                return BASIC_RETORTS.get(answerTo)

    def butt(self):
        for answerTo in BUTT_INS:
            if answerTo in self.message:
                return BUTT_INS.get(answerTo)

    def beUseful(self):
        for answerTo in BUTT_INS:
            if answerTo in self.message:
                return BUTT_INS.get(answerTo)
