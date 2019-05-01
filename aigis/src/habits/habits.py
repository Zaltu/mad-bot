"""
Collection of habits, separated into arbitrary timechunk sections.
Timechunks should be randomized within themselves

DAILY:
	- luigifish: 20:30
ANNUALY:
    - memento mori: 08:30

"""
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger as Every

from src.consts import GENERAL, DBPATH


class Habits(object):
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


async def luigifish(discord):
    """
    Post luigifish

    :param obj discord: discord connection
    """
    channel = discord.get_channel(GENERAL)
    text = "I AM GOING TO POST THIS LUIGI EVERY DAY UNTIL YOU LIKE IT"
    await discord.send_file(
        destination=channel,
        fp=os.path.join(DBPATH, "luigifish.png"),
        content=text
    )

async def memento(discord):
    """
    Remember your mortality

    :param obj discord: discord connection
    """
    channel = discord.get_channel(GENERAL)
    text = "Memento Mori"
    await discord.send_message(channel, text)
