# mad-bot
Averagely poorly overdesigned Bot for MAD. Includes two main features: `actions` and `habits`.
The bot itself is named Aigis. My waifu UwU. Currently a private bot and not likely to change.

This repo also contains a functional wrapper around the Python `discord` package. This is to add features such as
- sync -> async message sending
- auto-chunking of large messages
- simple connect/disconnect
- simplified callback management


## Future
Aigis will eventually branch out far beyond a simple discord bot, meaning everything here will very likely get largely reorganized and rewritten in the mid-term future. It is unclear whether this will stay a pure discord bot repo, or it will be replaced by something else.


# Requirements
__Python 3.6 :luigihands:__
- discord 1.0.1
- APScheduler 3.6.0
- pyquery 1.4.0
- wikipedia 1.4.0
- zaltu/backdoorgery | master branch (bundled)
