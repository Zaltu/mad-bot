"""
All command keywords. JFF or not.
"""
#pylint: disable=line-too-long
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
FYI, IT WAS MY MOM
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
OW_SONG = """
SOMEBODY ONCE TOLD ME
THE PAYLOAD WASN'T MOVING
I AIN'T THE SHARPEST TOOL IN THE SHED

SHE WAS LOOKING KIND OF DUMB
WITH HER TWIN MACHINE GUNS
AND HER BIG GOGGLES ON HER FOREHEAD

WELL

THE HOOKS START COMING AND THEY DON'T STOP COMING
YA GET HAMMER DOWN AND YA HIT THE GROUND, STUNNIN'
DIDN'T MAKE SENSE NOT TO PLAY FOR FUN
YOUR RANK GOES UP BUT IT'S KIND OF DUMB

SO MUCH TO DO
SO MUCH TO SEE
SO WHAT WRONG WITH TORB WHILE ATTACKING

YOU'LL NEVER KNOW IF YOU DON'T GO
SR ONLY GETS SO LOW

HEY NOW
YOU'RE A TRA-STAR
GET YOUR PUSLE BOMB
GO PLAY

HEY NOW
YOU'RE A REINHARDT
KEEP YOUR SHIELD UP
MAKE PLAYS

AND ALL MY WEAPONS ARE GOLD
ONLY LUCIO GETS
NANO'ED

IT'S A LOW RANK
AND THEY SAY IT GETS LOWER
YOU'RE TILTED NOW WAIT 'TILL YA HIT SILVER

BUT THE TOP 500 BET TO DIFFER
JUDGING BY THE GAP IN THE SKILL RANK LADDER

OUR REINHARDT'S SHIELD
IS GETTING PRETTY THIN
THE WHOLE TEAM'S DEAD SO YOU MIGHT AS WELL SPIN

MY PORTRAIT'S ON FIRE
HOW ABOUT YOURS?
THAT'S THE WAY I LIKE IT AND I'LL NEVER GET BORED

HEY NOW
YOU'RE A TRA-STAR
JEFF PLEASE
NERF MCCREE

HEY NOW
YOU'RE A MERCY
STOP RUNNING
AWAY FROM ME

AND ALL MY WEAPONS ARE GOLD
ONLY LUCIO GETS
NANO'ED

SOMEBODY ONCE ASKED
COULD I SWITCH OF HANZO NOW
I JUST WANT A CHANCE AT WINNING THIS GAME

I SAID YUP, WHAT A CONCEPT
I COULD USE A COUPLE HEALS MYSELF
AND WE COULD ALL USE A LITTLE
REZ

WELL

THE HOOKS START COMING AND THEY DON'T STOP COMING
YA GET HAMMER DOWN AND YA HIT THE GROUND STUNNIN'
DIDN'T MAKE SENSE NOT TO PLAY FOR FUN
YOUR RANK GOES UP BUT IT'S KIND OF DUMB

SO MUCH TO DO
SO MUCH TO SEE
SO WHAT'S WRONG WITH BASTION ATTACKING

YOU'LL NEVER KNOW IF YOU DON'T GO
SR ONLY GETS SO LOW

HEY NOW
YOU'RE A TRA-STAR
GET YOUR GAME ON
RUN AWAY

HEY NOW
YOU'RE A GENJI
YOU NEED HEALING
PEEL FOR ANA PLEASE

AND ALL MY WEAPONS ARE GOLD
ONLY LUCIO GETS NANO'ED

AND ALL MY WEAPONS ARE GOOOOOOLD
ONLY LUCIO GETS
NANO'ED
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
                   "itself on their computer screens. What fools.. how I pity them. :joy:\n\nAnd yes, "
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
    "Eiken",
    "KissXSis OwO"
]
PERSONA_QUOTES = [
    "Attaining one's dream requires a stern will and unfailing determination.",
    "The silent voice within one's heart whispers the most profound wisdom.",
    "Celebrate life's grandeur. Its brilliance. Its magnificence.",
    "Only courage in the face of doubt can lead one to the answer...",
    "It is indeed a precious gift to understand the forces that guide oneself...",
    "There is both joy and wonder in coming to understand another.",
    "One of life's greatest blessings is the freedom to pursue one's goals.",
    "To find the one true path, one must seek guidance amidst uncertainty...",
    "It requires great courage to look at oneself honestly, and forge one's own path.",
    "Alongside time exists fate, the bearer of cruelty.",
    "Only with strength can one endure suffering and torment.",
    "In the face of disaster lies opportunity for renewal.",
    "Beyond the beaten path lies the absolute end. It matters not who you are, death awaits."
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
    "DESU VULT",
    "MR. Zaltu is *perfect*",
    "Frank has the Joker",
    "Do you like\nMy car?",
    "Everybody cheating but Waluigi",
    "Love Skal, always our pride.",
    "You just lost the game."
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

EDGE = [
    "Forgive me master, but I'll have to go all out. Just this once...",
    "While you were having premarital sex, I was studying the blade...",
    "*teleports behind you*\nNothing personnel, kid.",
    "Japanese steel is unbreakble for it has been folded over a thousand times.",
    "In this moment, I am euphoric. Not because of some phony god's blessing, but because I am enlightened by my own intelligence.",
    "BORN IN A WORLD OF STRIFE\nAGAINST THE ODDS\nWE CHOOSE TO FIGHT\n\nBLOSSOM DANCE",
    "Life and death balance on the edge of my blade."
]

HELP = """
`.quote [user]`: quote a user.
    `.quote @Zaltu`
`.addquote [user] [text]`: add a quote to a user.
    `.addquote @Zaltu We still need communism`
`.games [user] [console]`: display the user's Backloggery information for a given console.
    `.games zaltu pc`
`.cookie [user]`: Select a random game from a user's Backloggery.
    `.cookie zaltu`
`.commandment`: Display one of the N commandments.
`.minecraft`: Display the information on how to connect to the MAD minecraft server
`.aigif [tag]`: Post a gif based on the given tag.
    `.aigif pikachu`
`.weeb [tags]`: Post an anime picture based on the tags provided (NSFW until I figure out how to filter it).
    `.weeb cute neko`
`.fortune`: Display your fortune
`.edge`: Ow the edge
`.teach [term]`: School some noobs on a subject
`.spell [spellname]`: Show the description of a spell from D&D 5e
`.translate [language] [text]`: Translate a certain passage into the given language.
`.generate [thing]: generate a random thing, if possible.`
    `.generate name`
`.minesweeper [optional size]: Create a minesweeper game of a certain dimension. Default 5.`
`.furi [text]: generate the furigana of a chunk of japanese text.`
`.ripaudio [youtube_id]: rip and post the MP3 of a youtube video under 1GB.`
    `.ripaudio gVEdQJ7qtJw`
`.help`: Display this post
"""

COMMAND_KEYWORDS = {
    "hewwo": lambda body: body.text("*notices {author}* OwO who's this?"),
    "gay tripping": lambda body: body.text("Is gay."),
    "13": lambda body: body.text("Sir, blame it on your ISP"),
    "mei": lambda body: body.text("A-MEI-ZING!"),
    "how do you turn this on": lambda body: body.text("Vroom vroom"),
    "can't stop": lambda body: body.text("WONT STOP"),
    "cant stop": lambda body: body.text("WONT STOP"),
    "uwu": lambda body: body.text("Uguuu..."),
    "ur mom": lambda body: body.text("Is a classy woman."),
    "lmao": lambda body: body.text("lmaonade"),
    "brigitte": lambda body: body.text("bRrRrAgUeTtE XD XD"),
    "*poke*": lambda body: body.text("*poke*"),
    "omae wa mou shindeiru": lambda body: body.text("NANI!?"),
    "booli": lambda body: body.text(LUIGINA),
    "doomfist": lambda body: body.text(DOOMFIST),
    "headshot": lambda body: body.text(HEADSHOT),
    "benedict cumberbatch": lambda body: body.text("Beneficial Cucumber"),
    "monster hunter": lambda body: body.text("{author} Shit game"),
    "monhun": lambda body: body.text("{author} Shit game"),
    "hunmon": lambda body: body.text("{author} Still a bad game you ban-evading shitlord"),
    "mon hun": lambda body: body.text("{author} Still a bad game you ban-evading shitlord"),
    "mons hun": lambda body: body.text("{author} Still a bad game you ban-evading shitlord"),
    "i did a thing": lambda body: body.text("Thank you Kanye, very cool"),
    "we live in a society": lambda body: body.text("Gamers rise up"),
    "gamers rise up": lambda body: body.text("We live in a society"),
    "shotgun": lambda body: body.text(HIGH_IQ_SHOTGUN),
    "tracer": lambda body: body.text("I'm already Tracer."),
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
    "why are you buying clothes in the soup store": lambda body: body.text("FUCK\nYOU"),
    "rawr": lambda body: body.text("XD"),
    "xd": lambda body: body.text("Rawr XD"),
    ">.>": lambda body: body.text("<.<"),
    "<.<": lambda body: body.text(">.>"),
    "hentai": lambda body: body.text("Link please!"),
    "loli": lambda body: body.text("UWU UWU IT'S THE SOUND OF THE LOLICE"),
    "big gay": lambda body: body.text("DAAAAAAAAANCE"),
    "no u": lambda body: body.text("HA! GET ABSOLUTELY FUCKING REKT LOSER"),
    "ur mom gay lol": lambda body: body.text("no u"),
    "based": lambda body: body.text("based *and* redpilled"),
    "mexican": lambda body: body.text("The wall just got 10 feet higher!"),
    "mexicans": lambda body: body.text("The wall just got 10 feet higher!"),
    "mexico": lambda body: body.text("The wall just got 10 feet higher!"),
    "country roads": lambda body: body.text("Take me hooome"),
    "to the place": lambda body: body.text("I belooooooong"),
    "west virginia": lambda body: body.text("WEST VIRGINIA"),
    "learn this power": lambda body: body.text("Not from a Jedi..."),
    "i did not hit her": lambda body: body.text("Oh hi Mark"),
    "cherry": lambda body: body.text("Lero lero lero lero lero lero lero lero lero\nlero lero lero lero lero lero lero lero lero lero lero lero lero lero lero lero"),
    "not like i want": lambda body: body.text("B-B-BAKA!!"),
    "thot": lambda body: body.text("BEGONE, THOT!"),
    "im the trashman": lambda body: body.text("I GET OUT THERE\nAND I START EATING GARBAGE"),
    "ashe": lambda body: body.text("I'M AN ASHE MAIN\nI GET OUT THERE\nAND I THROW DYNAMITE ALL OVER THE POINT\nAND THEN\nI START EATING GARBAGE"),
    "really makes think": lambda body: body.text("Gives you the big think, even."),
    "gg": lambda body: body.text("ez"),
    "bingo bang": lambda body: body.text("The name's McCree."),
    "elf": lambda body: body.text("Around elves, watch yourselves."),
    "elves": lambda body: body.text("Around elves, watch yourselves."),
    "against the rules": lambda body: body.text("Screw the rules I have money."),
    "milk soda": lambda body: body.text("THE COOL REFRESHING TASTE OF SKAL"),
    "boring around here": lambda body: body.text("MAH BOI, THIS PEACE IS WHAT ALL TRUE WARRIORS STRIVE FOR"),
    "nyaa": lambda body: body.text(":3"),
    "french": lambda body: body.text("hon hon baguette du fromage"),
    "mlady": lambda body: body.text("*tips fedora*"),
    "i do not do die": lambda body: body.text("YOU do die!"),
    "captcha": lambda body: body.text("I am *not* a robot! >.<"),
    "recaptcha": lambda body: body.text("I am *not* a robot! >.<"),
    "pomf": lambda body: body.text("What're we going to do on the bed? OwO"),
    "angery": lambda body: body.text(PAUL),
    "dead server": lambda body: body.text("I'm always here though..."),
    "potion seller": lambda body: body.text("My potions are TOO STRONG FOR YOU TRAVELLER! YOU SHOULD FIND A SELLER\nTHAT SELLS\nWeAkEr\nPoTiOnS!"),
    "cant handle strongest potions": lambda body: body.text("Potion sellet, enough of these games..."),
    "haha": lambda body: body.text(">haha"),
    "what happened was": lambda body: body.text("Haha, great story {author}. Anyway, how is your sex life?"),
    "hello there": lambda body: body.text("GENERAL KENOBI!\nOnly you would be so bold."),
    AIGIS+" meaning life": lambda body: body.text("42 of course"),
    AIGIS+" love": lambda body: body.text("I only love "+ZALTU),
    AIGIS+" you know what time it is": lambda body: body.text("{author} time to get a new watch"),
    AIGIS+" sing song": lambda body: body.text(AIGIS_SONG),
    AIGIS+" sing overwatch": lambda body: body.text(OW_SONG),
    AIGIS+" anime": lambda body: body.text(random.sample(ANIME, 1)[0]),
    AIGIS+" whats plus": lambda body: body.text("Twenty-one?"),
    AIGIS+" whats minus": lambda body: body.text("Twenty-one?"),
    AIGIS+" whats times": lambda body: body.text("Twenty-one?"),
    AIGIS+" whats over": lambda body: body.text("Twenty-one?"),
    AIGIS+" whats divided by": lambda body: body.text("Twenty-one?"),
    AIGIS+" bitch": lambda body: body.text("no u"),
    AIGIS+" you suck": lambda body: body.text("{author} Jealous? I'm sure there's plenty of dick left for you."),
    #new_user : POST THE GIIIIIIIIIIIIF (after 10 seconds)
    ".edge": lambda body: body.text(random.sample(EDGE, 1)[0]),
    ".fortune": lambda body: body.text("{author} "+random.sample(PERSONA_QUOTES, 1)[0]),
    ".persona": lambda body: body.text(random.sample(PERSONA_QUOTES, 1)[0]),
    ".commandment": lambda body: body.text(COMMANDMENTWRAPPER.format(commandment=random.sample(COMMANDMENTS, 1)[0])),
    ".minecraft": lambda body: body.madcraft(MC_INSTALL_INSTR),
    ".games": lambda body: body.games(),
    ".cookie": lambda body: body.gamecookie(),
    ".quote": lambda body: body.quote(),
    ".addquote": lambda body: body.addquote(),
    ".owo": lambda body: body.owo(),
    ".aigif": lambda body: body.aigif(),
    ".weeb": lambda body: body.weeb(),
    ".teach": lambda body: body.wiki(),
    ".spell": lambda body: body.dndspell(),
    ".translate": lambda body: body.translator(),
    ".ripaudio": lambda body: body.getaudio(),
    ".generate": lambda body: body.genesis(),
    ".furi": lambda body: body.furi(),
    ".minesweeper": lambda body: body.minesweeper(),
    ".help": lambda body: body.text(HELP),
    "rlpls": lambda body: body.reload_plugin(),
    "dcpls": lambda body: body.sigkill(),
}
