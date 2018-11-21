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
    "hewwo?": lambda body: body.text("*notices {author}* OwO who's this?"),
    "lol": lambda body: body.text("lmaonade"),
    "brigitte": lambda body: body.text("bRrRrAgUeTtE XD XD"),
    "dcpls": lambda body: body.text("SIGKILL"),
    "*poke*": lambda body: body.text("*poke*"),
    "omae wa mou shindeiru": lambda body: body.text("NANI!?"),
    "booli": lambda body: body.text(":luigina:"),
    USERID+" who you love": lambda body: body.text("I only love "+ZALTU),
    USERID+" do you love me": lambda body: body.text("I only love "+ZALTU),
    USERID+" who you not love": lambda body: body.text("You."),
    USERID+" who you don't love": lambda body: body.text("You."),
    USERID+" who you dont love": lambda body: body.text("You."),
    USERID+" ur mom gay lol": lambda body: body.text("no u"),
    USERID+" you know what time it is": lambda body: body.text("{author} time to get a new watch"),
    ".persona": lambda body: body.interface(body.nyx),
    ".owo": lambda body: body.interface(body.owo),
    ".games": lambda body: body.interface(body.games)
}


CONTEXT_MAP = {
    "Discord": lambda mind, delta: mind._processDiscord(delta)
}
