"""
Collection of habits, separated into arbitrary timechunk sections.
Timechunks should be randomized within themselves
"""
DAILY = [luigifish]

def luigifish(discord):
    """
    Post luigifish

    :param obj discord: discord connection
    """
    text = "@everyone I AM GOING TO POST THIS LUIGI EVERY DAY UNTIL YOU LIKE IT"
    discord.post("image", text)
