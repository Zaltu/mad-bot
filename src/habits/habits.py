"""
Collection of habits, separated into arbitrary timechunk sections.
Timechunks should be randomized within themselves

DAILY:
	- luigifish: 20:30
ANNUALY:
    - memento mori: 08:30

"""
import datetime
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger as Every

from src.consts import GENERAL, DBPATH, SPAMMYTESTS
from src.habits.consts import SPECIAL_DAYS


class Habits():
    """
    Defines all repetitive functionality

    :param DiscordSenses discord: the discord connection
    """
    def __init__(self, discord):
        self.discord = discord
        self.schedule = AsyncIOScheduler()
        self.schedule.start()
        self.populateScheduler()

    def populateScheduler(self):
        """
        Add all jobs to scheduler
        """
        self.schedule.add_job(
            luigifish,
            args=[self.discord],
            trigger=Every(days=1, start_date="2019-01-01T20:30:00")
        )

        self.schedule.add_job(
            memento,
            args=[self.discord],
            trigger=Every(days=365, start_date="2019-03-05T08:30:00")
        )

        self.schedule.add_job(
            special_day,
            args=[self.discord],
            trigger=Every(days=1, start_date="")
        )


async def luigifish(discord):
    """
    Post luigifish

    :param obj discord: discord connection
    """
    channel = discord.get_channel(SPAMMYTESTS)
    text = "I AM GOING TO POST THIS LUIGI EVERY DAY UNTIL YOU LIKE IT"
    await channel.send(text, file=discord.File(os.path.join(DBPATH, "luigifish.png")))


async def memento(discord):
    """
    Remember your mortality

    :param obj discord: discord connection
    """
    channel = discord.get_channel(GENERAL)
    text = "Memento Mori"
    await channel.send(text)


async def special_day(discord):
    """
    Wish all a merry Christmas

    :param obj discord: discord connection
    """
    channel = discord.get_channel(GENERAL)
    todayte = datetime.datetime.strftime(datetime.datetime.today(), "%m/%d/")
    text = SPECIAL_DAYS.get(todayte, None)
    if text:
        await channel.send(text)
