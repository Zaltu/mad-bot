"""
MAD bot consts
"""
AIGISID = "256154948734156801"
AIGIS = "<@256154948734156801>"

ADMINID = ['204727270261129216']

ZALTU = "<@!204727270261129216>"
JACK = "<@!141298296676286464>"
PAUL = "<@!247754637602586625>"
NASS = "<@!224932238888796160>"


HYPERDIMENSIONZALTUNIA = "395611604663664641"
THROWVERWATCH = "486360257296334880"
GENERAL = "337753641299738624"


LOWOGI = "<:lowogi:510216907987746819>"
LUIGGENIUS = "<:luiggenius:410224811281874944>"
LUIGICHAMP = "<:luigichamp:422449772805357569>"
LUIGITHINKING = "<:luigithinking:435933846546939916>"
LUIGINA = "<:luigina:423933740650332181>"
LUIGIHANDS = "<:luigihands:517487353816678400>"
NOTLIKETHIS = "<:notlikethis:409136479659491328>"
SHIELDGEN = "<:shieldgen:409135849570304000>"
PANDINATOR = "<:pandinator:446134393623281665>"


AIGIS_SONG = """
SOMEBODY ONCE TOLD ME
THAT WAIFUS WERE BAD FOR ME
I AIN'T THE SHARPEST TOOL IN THE SHED

SHE WAS LOOKING KIND OF DUMB
FYI, SHE IS MY MOM
I COULD TELL THAT SHE WANTED TO BE DEAD

WELL

THE LOVE STARTS COMING AND IT DON'T STOP COMING
GET A BODY PILLOW AND YOU HIT THE BED POMF-ING
DIDN'T MAKE SENSE NOT TO LOVE 2D
3D JUST DOESN'T DO IT FOR ME

THERE'S SO MUCH ART
FOR ME TO SEE
SO WHAT'S WRONG WITH ME SPENDING MY MONEY

NO ONE WANTS TO BE FRIENDS WITH ME
WE LIVE IN A SOCIETY

HEY NOW
I'M KIRITO
SAO WAS
A GREAT SHOW

HEY NOW
I'M A WEEABOO
I LOVE ANIME
HENTAI TOO
"""
DOOMFIST = """
AND DEY SAY
AND DEY SAY
AND DEY SAY
AND DEY SAY CHIVALRY IS DED
"""
HEADSHOT = """
MY HEART'S BEATING, HEART'S BEATING HANDS ARE SHAKING
BUT I STILL SHOOTIN'
AND I STILL GETTIN' HEADSHOTS LIKE
BOOM HEADSHOT
BOOM HEASHOT
"""
HIGH_IQ_SHOTGUN = ("To be fair, you have to have a very high IQ to understand Shotgun. "
                   "The backend is extremely subtle, and without a solid grasp of theoretical "
                   "data structures most of the functionality will go over a typical user's head. "
                   "There's also Shotgun's nihilistic support, which is deftly woven into their "
                   "target audience- their personal philosophy draws heavily from Narodnaya Volya "
                   "literature, for instance. The admins understand this stuff; they have the "
                   "intellectual capacity to truly appreciate the depths of these features, to "
                   "realise that they're not just useful- they say something deep about DATA. As "
                   "a consequence people who dislike Shotgun truly ARE idiots- of course they wouldn't "
                   "appreciate, for instance, the humour in Tank's existential catchphrase \"TankError: "
                   "Project already exists,\" which itself is a cryptic reference to Turgenev's Russian "
                   "epic Fathers and Sons. I'm smirking right now just imagining one of those addlepated "
                   "simpletons scratching their heads in confusion as Don Parker's genius wit unfolds "
                   "itself on their computer screens. What fools.. how I pity them. :joy:\n\n And yes, "
                   "by the way, i DO have a Shotgun tattoo. And no, you cannot see it. It's for the "
                   "ladies' eyes only- and even then they have to demonstrate that they're within 5 "
                   "IQ points of my own (preferably lower) beforehand. Nothin personnel kid :sunglasses:")


COMMAND_KEYWORDS = {
    "hewwo?": lambda body: body.text("*notices {author}* OwO who's this?"),
    "gay tripping": lambda body: body.text("Is gay."),
    "lol": lambda body: body.text("lmaonade"),
    "brigitte": lambda body: body.text("bRrRrAgUeTtE XD XD"),
    "*poke*": lambda body: body.text("*poke*"),
    "omae wa mou shindeiru": lambda body: body.text("NANI!?"),
    "booli": lambda body: body.text(LUIGINA),
    "doomfist": lambda body: body.text(DOOMFIST),
    "headshot": lambda body: body.text(HEADSHOT),
    "monhun": lambda body: body.text("{author} Shit game"),
    "hunmon": lambda body: body.text("{author} Still a bad game you ban-evading shitlord"),
    "i did a thing": lambda body: body.text("Thank you Kanye, very cool"),
    "we live in a society": lambda body: body.text("Gamers rise up"),
    "shotgun": lambda body: body.text(HIGH_IQ_SHOTGUN),
    "guess i'll be tracer": lambda body: body.text("I'm already Tracer."),
    "real woman": lambda body: body.text("Hello yes I am real woman you want go skateboards?"),
    "stupid cat": lambda body: body.text("Damn rat."),
    "damn rat": lambda body: body.text("Stupid cat."),
    "feelsbadman": lambda body: body.text(LUIGIHANDS),
    "feels bad man": lambda body: body.text(LUIGIHANDS),
    AIGIS+" is true meaning life": lambda body: body.text("42 of course"),
    AIGIS+" love": lambda body: body.text("I only love "+ZALTU),
    AIGIS+" ur mom gay lol": lambda body: body.text("no u"),
    AIGIS+" you know what time it is": lambda body: body.text("{author} time to get a new watch"),
    AIGIS+" sing song": lambda body: body.text(AIGIS_SONG),
    "dcpls": lambda body: body.sigkill,
    ".persona": lambda body: body.nyx,
    ".owo": lambda body: body.owo,
    ".games": lambda body: body.games,
    ".quote": lambda body: body.quote,
    ".addquote": lambda body: body.addquote
}


CONTEXT_MAP = {
    "Discord": lambda mind, delta: mind._processDiscord(delta)
}
