"""
MAD bot consts
"""
import actions


USERID = "<@256154948734156801>"

ZALTU = "<@!204727270261129216>"
JACK = "<@!141298296676286464>"
PAUL = "<@!247754637602586625>"
NASS = "<@!224932238888796160>"


HYPERDIMENSIONZALTUNIA = "395611604663664641"
THROWVERWATCH = "486360257296334880"
GENERAL = "337753641299738624"


COMMAND_KEYWORDS = {
    "hewwo?": lambda: "*notices {author}* OwO who's this?",
    "lol": lambda: "lmaonade",
    "brigitte": lambda: "bRrRrAgUeTtE XD XD",
    "dcpls": lambda: "SIGKILL",
    "*poke*": lambda: "*poke*",
    "omae wa mou shindeiru": lambda: "NANI!?",
    "booli": lambda: ":luigina:",
    USERID+" who you love": lambda: "I only love "+ZALTU,
    USERID+" do you love me": lambda: "I only love "+ZALTU,
    USERID+" who you not love": lambda: "You.",
    USERID+" who you don't love": lambda: "You.",
    USERID+" who you dont love": lambda: "You.",
    USERID+" ur mom gay lol": lambda: "no u",
    USERID+" you know what time it is": lambda: "{author} time to get a new watch",
    ".persona": actions.nyx,
    ".owo": actions.owo
}
