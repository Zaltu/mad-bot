# mad-bot
Averagely poorly overdesigned Bot for MAD. Includes two main features: `actions` and `habits`.
The bot itself is named Aigis. My waifu UwU. Currently a private bot and not likely to change.

## Actions
Actions are functionality that is brought about as a reaction to user input. While these are all lumped into one category code-wise for now, there are a few different semantical types of actions.

- butt-ins: The bot butts in to your conversation, recognizing certain words and immediately posting a response.
- commands: There are two types of these, one being commands directed directly at the bot (@Aigis do this), and the other being known `.command` keywords.

- functions: Features that actually serve a purpose and/or can be useful
- jff: Just For Fun. Most butt-ins fall in this category


## Habits
Habits are repeated actions that are processed independantly of user input, generally on a daily or so basis. There is no user input invloved, but the other semantical types still apply. Currently, they're all JFF

- functions: Features that actually serve a purpose and/or can be useful
- jff: Just For Fun. Most butt-ins fall in this category


# Requirements
__Python 3.6 :luigihands:__
- discord 1.0.1
- APScheduler 3.6.0
- pyquery 1.4.0
- wikipedia 1.4.0
- zaltu/backdoorgery | master branch (bundled)
