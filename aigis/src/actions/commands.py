"""
All command keywords. JFF or not.
"""
import random

from src.consts import AIGIS, ZALTU, PAUL

LUIGISMUG = "<:luigi2smug:534514921333981206>"
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

AND ALL MY WAIFUS LOVE ME
NOT A SINGLE ONE IS
OVER THIRTEEN

AND ALL MY WAIFUS LOVE MEEEEEEE
I SWEAR, 3D IS A MEME


IT'S A LEWD PLACE
AND THEY SAY IT GETS LEWDER
YEAH VANILLA'S COOL
BUT HAVE YOU TRIED FUTA?

RAVIOLI
RAVIOLI
DON'T EVEN THINK ABOUT TOUCHING THAT LOLI

OH MY GOD
WHAT HAVE YOU DONE
THE FBI'S COMING SO YOU MIGHT AS WELL RUN

MY WORLD'S ON FIRE
HOW ABOUT YOURS?
BURNING DOWN AROUND ME AS I'M TACKLED TO THE FLOOR

HEY NOW
I WAS GIVEN
TWENTY-FIVE YEARS
TO LIFE

HEY NOW
I PROCLAIMED I
WAS A PEDO
OUT OF SPITE

AND ALL THE INMATES LOVE ME
DURING SHOWER TIME ESPECIALLY

AND ALL THE INMATES LOVE MEEEEEEE
PLEASE GET ME OUT SOON MOMMY ( ;_;)
"""
DOOMFIST = """
AND DEY SAY
AND DEY SAY
AND DEY SAY
AND DEY SAY CHIVALRY IS DED
"""
HEADSHOT = """
MY HEART'S BEATING
HEART'S BEATING HANDS ARE SHAKING
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
VELVET_ROOM = """
Welcome to the Velvet Room.

My name is Igor.
I am delighted to make your acquaintance.
This place exists between dream and reality.
Mind and matter.
Only those who have forged some sort of contract may enter.
"""
ANIME = [
    "Death Note",
    "Hidan no Aria, but unironically",
    "Stop watching anime, faggot",
    "Fruits Basket",
    "The Persona  movies ;) . Play the game first though.",
    "Boku no Pico",
    "Cory in the House",
    "Hataraku Saibou",
    "Black Lagoon",
    "Jormungand",
    "Durarara, mainly because the OP1 is amazing",
    "Eiken"
]
PERSONA_QUOTES = [
    "Celebrate life's grandeur. Its brilliance. Its magnificence.",
    "There is both joy and wonder in coming to understand another.",
    "Beyond the beaten path lies the absolute end. It matters not who you are, death awaits.",
    "It requires great courage to look at oneself honestly, and forge one's own path..."
]
COMMANDMENTS = [
    "Traps are gay.",
    "Luigi is the real hero.",
    "It was probably Maybelline.",
    "We are throwing.",
    "We live in a society.",
    "No items, Ganondorf only, Final Destination.",
    PAUL+" is Trump, confirmed.",
    "gg ez",
    "Having more than one Waifu will destroy your laifu.",
    "It's almost scary how good I am.",
    "OwO what's this?",
    "REEEEEEEEEEEEEEEEEEEEEEEEEEEE",
    "I'VE GOT THE FEELING THAT THEY'VE GOT A SHIEEEEEEEEEELD GENERATOR!",
    LUIGISMUG.join(["", " ALL ", " THEY ", " DO ", " IS ", " SPAM ", " GREEN ", " MARIO ", " FACE "]),
    "I AM GOING TO POST THIS LUIGI EVERY DAY UNTIL YOU LIKE IT",
    "DESU VULT"
]
COMMANDMENTWRAPPER = "\"{commandment}\"\n    So sayeth the scriptures."

MC_INSTALL_INSTR = """
Steps to join the MAD Minecraft server:
1 - Download and install Minecraft:
https://minecraft.net
2 - Download and install the Twitch client:
https://app.twitch.tv/download
3 - After logging in to the twitch client, go to the "Mods" section that you can find on the top toolbar
4 - Select "Minecraft"
5 - Browse All Modpacks and search for "All The Mods 3"
5 - Download "All The Mods 3" version 5.11.2
6 - Launch Minecraft through the Twitch Client and log in with your Minecraft credentials
7 - Select "Launch Options"
8 - In the "JVM Arguments" section, set the first argument to "-Xmx10G"
(this sets Minecraft to take up to 10 GB RAM. It generally won't hit that, but it will speed up boot time significantly)
7 - Launch by clicking "Play" on the "News" tab. It takes a long time to load...
8 - Once loaded, select "Multiplayer", "Add Server" and set the server address to the IP:
{IP}
9 - Join Server!
"""

COMMAND_KEYWORDS = {
    "hewwo": lambda body: body.text("*notices {author}* OwO who's this?"),
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
    "mon hun": lambda body: body.text("{author} Still a bad game you ban-evading shitlord"),
    "mons hun": lambda body: body.text("{author} Still a bad game you ban-evading shitlord"),
    "i did a thing": lambda body: body.text("Thank you Kanye, very cool"),
    "we live in a society": lambda body: body.text("Gamers rise up"),
    "gamers rise up": lambda body: body.text("We live in a society"),
    "shotgun": lambda body: body.text(HIGH_IQ_SHOTGUN),
    "i'll be tracer": lambda body: body.text("I'm already Tracer."),
    "real woman": lambda body: body.text("Hello yes I am real woman you want go skateboards?"),
    "stupid cat": lambda body: body.text("Damn rat."),
    "damn rat": lambda body: body.text("Stupid cat."),
    "ken": lambda body: body.text("Ken is a team-killing shit."),
    "feelsbadman": lambda body: body.text(LUIGIHANDS),
    "feels bad man": lambda body: body.text(LUIGIHANDS),
    "skyrim": lambda body: body.text("sKyRiM bElOnGs To ThE nOrDs!"),
    "based revolver jesus": lambda body: body.text("B A S E D\nA\nS\nE\nD"),
    "i chooseth this fate of mine own free will": lambda body: body.text(VELVET_ROOM),
    "he did it": lambda body: body.text("The absolute madlad! " + LUIGICHAMP),
    "memes": lambda body: body.text("And Dreams"),
    "black": lambda body: body.text("What, are you racist?"),
    ">.>": lambda body: body.text("<.<"),
    "big gay": lambda body: body.text("DAAAAAAAAANCE"),
    AIGIS+" is true meaning life": lambda body: body.text("42 of course"),
    AIGIS+" love": lambda body: body.text("I only love "+ZALTU),
    AIGIS+" ur mom gay lol": lambda body: body.text("no u"),
    AIGIS+" you know what time it is": lambda body: body.text("{author} time to get a new watch"),
    AIGIS+" sing song": lambda body: body.text(AIGIS_SONG),
    AIGIS+" anime": lambda body: body.text(random.sample(ANIME, 1)[0]),
    ".persona": lambda body: body.text(random.sample(PERSONA_QUOTES, 1)[0]),
    ".commandment": lambda body: body.text(COMMANDMENTWRAPPER.format(commandment=random.sample(COMMANDMENTS, 1)[0])),
    ".minecraft": lambda body: body.madcraft(MC_INSTALL_INSTR),
    ".games": lambda body: body.games(),
    ".cookie": lambda body: body.gamecookie(),
    ".quote": lambda body: body.quote(),
    ".addquote": lambda body: body.addquote(),
    "dcpls": lambda body: body.sigkill(),
}
