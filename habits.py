"""
Collection of habits, separated into arbitrary timechunk sections.
Timechunks should be randomized within themselves

DAILY:
	- luigifish: 20:30

"""
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger as Every

import consts


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


async def luigifish(discord):
    """
    Post luigifish

    :param obj discord: discord connection
    """
    channel = discord.get_channel(consts.GENERAL)
    #text = "@everyone I AM GOING TO POST THIS LUIGI EVERY DAY UNTIL YOU LIKE IT"
    await discord.send_file(destination=channel, fp="db/luigifish.png" content="testing")
