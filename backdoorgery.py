import requests
from pyquery import PyQuery

STATIC_URL = "https://backloggery.com"
GAMES_TAG = "table#sysgrid"

def _getHTML(url):
    return requests.get(url).text


def _buildUrl(user):
    if user:
        return STATIC_URL + "/" + user


def getTag(html):
    pq = PyQuery(html)
    tag = pq(GAMES_TAG)
    return tag.text().split("\n")


def getConsoleMetrics(user, console):
    html = _getHTML(_buildUrl(user))
    data = getTag(html)
    if not data:
        return "Invalid user \"%s\"" % user

    # This is probably very stupid. Check literally any alternate URL
    sumStr = "{user} has the following stats for their {console}:"
    sumStr += "\n{unfinished} games unfinished\n{beaten} games beaten\n{complete} games completed"
    "https://backlogger.com/games.php?user={user}&console={console}"