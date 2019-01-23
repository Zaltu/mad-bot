"""
Illegal API to access backloggery stats
"""
import requests
from pyquery import PyQuery

STATIC_URL = "https://backloggery.com"
USER_URL = "https://backloggery.com/{user}"

USER_CONSOLE_URL = "https://backloggery.com/games.php?user={user}&console={console}"
CONSOLE_STATS_TAG = "div#maincolumn"

COOKIE_URL = "https://backloggery.com/random.php?user={user}"
COOKIE_POST = "Open%20That%20Cookie!"
COOKIE_TAG = "table#fortune"

GAMES_TAG = "table#sysgrid"

def _getHTML(url):
    """
    Makes the CURL request to the URL

    :param str url: the target URL

    :returns: the HTML returned from request get call
    :rtype: str
    """
    return requests.get(url).text

def _postHTML(url, data):
    """
    Sends a POST request to a url with some data

    :param str url: url to poke
    :param str data: data to send as POST

    :returns: the HTML returned from the request
    :rtype: str
    """
    return requests.post(url, data=data).text

def _buildUrl(url, user=None, console=None):
    """
    Build the correct URL required to access certain stats.

    :param str url: the backloggery url to format
    :param str user: optional user to get information from
    :param str console: optional console to get information from

    :returns: a backloggery.com URL containing the desired information
    :rtype: str
    """
    return url.format(user=user, console=console)


def _getTag(html, tag):
    """
    Performs a very simple parse on HTML and returns a list of values matching the HTML tag given.
    See pyquery docs for more information.

    :param str html: the html to parse
    :param str tag: the html tag to search for

    :returns: values matching the tag
    :rtype: list
    """
    pq = PyQuery(html)
    tag = pq(tag)
    return tag.text().split("\n")


def getConsoleMetrics(user, console):
    """
    Get the Unfinished/Beaten/Completed metrics for a certain user on a certain console.

    :param str user: the user to analyze
    :param str console: the console to analyze

    :returns: formatted visual of game status metrics for the user
    :rtype: str
    """
    html = _getHTML(_buildUrl(USER_CONSOLE_URL, user, console))
    data = _getTag(html, CONSOLE_STATS_TAG)
    try:
        sumStr = ("{user} has the following stats for their {console}:\n"
                  "{unfinished} games unfinished\n{beaten} games beaten\n{complete} games completed")
        if len(data) > 9:
            return sumStr.format(user=user, console=console, unfinished=data[1], beaten=data[8], complete=data[11])
        else:
            return sumStr.format(user=user, console=console, unfinished=data[1], beaten=data[4], complete=data[7])
    except IndexError:
        return "Invalid user \"%s\" or console \"%s\"" % (user, console)


def getFortuneCookie(user):
    """
    Get a random game based on the default parameters.

    :param str user: the backloggery user

    :returns: formatted string with a random game in the user's backloggery
    :rtype: string
    """
    html = _postHTML(_buildUrl(COOKIE_URL, user=user), COOKIE_POST)
    data = _getTag(html, COOKIE_TAG)
    try:
        if not data[0]:
            raise IndexError("Actually no value")
        return "Time to play some {game}, my dude!".format(game=data[0])
    except IndexError:
        return "Invalid user \"%s\"" % user





if __name__ == "__main__":
    print(getConsoleMetrics("zaltu", "pc"))
    print(getFortuneCookie("zaltu"))
