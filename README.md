# mad-bot
Averagely poorly overdesigned Bot for MAD. Includes two main features: `actions` and `habits`.
The bot itself is named Aigis. My waifu UwU. Currently a private bot and not likely to change.

##Actions
Actions are functionality that is brought about as a reaction to user input. While these are all lumped into one category code-wise for now, there are a few different semantical types of actions.

- butt-ins: The bot butts in to your conversation, recognizing certain words and immediately posting a response.
- commands: There are two types of these, one being commands directed directly at the bot (@Aigis do this), and the other being known `.command` keywords.

- functions: Features that actually serve a purpose and/or can be useful
- jff: Just For Fun. Most butt-ins fall in this category

###Currently Available
Since most jffs are meant as semi-easter eggs, they will not be listed here. Functions are:
- `.cookie`: Pull a single game from a person's backloggery
- `.games`: Pull a user's stats for a specific game console
- `.addquote`: Store a quote related to a user
- `.quote`: Post a quote from a user
- `.commandment`: Post one of the N Commandments
En suite, the are approximately 35 easter eggs of varying obscurity.

##Habits
Habits are repeated actions that are processed independantly of user input, generally on a daily or so basis. There is no user input invloved, but the other semantical types still apply.

- functions: Features that actually serve a purpose and/or can be useful
- jff: Just For Fun. Most butt-ins fall in this category

###Currently Available
Currently, there is only one habbit:
- luigifish: Posts luigifish every day until you like it


#Requirements
- Python 3.6 :luigihands:
- APScheduler
- discord
- zaltu/backdoorgery (bundled)
