"""
Simple example of generating a minesweeper field.
"""
#pylint: disable=invalid-name
from random import randint

DISCORD_MAP = {
    0: "||:zero:||",
    1: "||:one:||",
    2: "||:two:||",
    3: "||:three:||",
    4: "||:four:||",
    5: "||:five:||",
    6: "||:six:||",
    7: "||:seven:||",
    8: "||:eight:||",
    "B": "||:boom:||"
}


def _genField(x, y):
    """
    Generate a field of a certain dimension.

    :param int x: x dimension
    :param int y: y dimension

    :returns: empty field
    :rtype: list
    """
    field = []
    for i in range(0, x):
        field.append([])
        for _ in range(0, y):
            field[i].append(0)
    return field


def _placeBs(field, n):
    """
    Place n bombs in random spots on the field.

    :param list field: the field
    :param int n: number of bombs to place
    """
    xd = len(field)
    yd = len(field[0])
    generatedPos = []

    while len(generatedPos) < n:
        xr = randint(0, xd-1)
        yr = randint(0, yd-1)
        if (xr, yr) not in generatedPos:
            field[xr][yr] = "B"
            generatedPos.append((xr, yr))


def _setCount(field):
    """
    Generate the bomb count for every non-bomb square on the field.

    :param list field: the field
    """
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            closeCounter = 0
            #print("Counting %s %s" % (i, j))
            for irange in range(i-1, i+2):
                for jrange in range(j-1, j+2):
                    # This is because python list indexes wrap on negative values.
                    # Can be an interesting mechanic though lol
                    if irange < 0 or jrange < 0:
                        continue
                    try:
                        #print("Checking %s %s" % (irange, jrange))
                        if field[irange][jrange] == "B":
                            #print("Found Bomb")
                            closeCounter += 1
                    except IndexError:
                        continue
            #print()
            if field[i][j] != "B":
                field[i][j] = closeCounter


def _discordify(field):
    """
    Convert a minefield to spoilered discord emojis.

    :param list field: the minefield

    :returns: formatted string for discord
    :rtype: str
    """
    stringVer = ""
    for x in field:
        for y in x:
            stringVer += DISCORD_MAP[y]
        stringVer += "\n"
    return stringVer


def getMineField(x=5, y=5):
    """
    Get a minefield that can be posted to discord.

    :param int x: x dimension, default 5
    :param int y: y dimension, default 5

    :returns: x-by-y minesweeper field
    :rtype: str
    """
    f = _genField(x, y)
    _placeBs(f, x-1)
    _setCount(f)
    return _discordify(f)



if __name__ == "__main__":
    print(getMineField())
