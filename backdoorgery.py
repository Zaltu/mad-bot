"""
Illegal API to access backloggery stats
"""
import requests
from pyquery import PyQuery

STATIC_URL = "https://backloggery.com"
USER_URL = "https://backloggery.com/{user}"
USER_CONSOLE_URL = "https://backloggery.com/games.php?user={user}&console={console}"
GAMES_TAG = "table#sysgrid"
CONSOLE_STATS_TAG = "div#maincolumn"

def _getHTML(url):
    """
    Makes the CURL request to the URL

    :param str url: the target URL

    :returns: the HTML returned from request get call
    :rtype: str
    """
    return requests.get(url).text


def _buildUrl(user=None, console=None):
    """
    Build the correct URL required to access certain stats.

    :param str user: optional user to get information from
    :param str console: optional console to get information from

    :returns: a backloggery.com URL containing the desired information
    :rtype: str
    """
    if user and console:
        return USER_CONSOLE_URL.format(user=user, console=console)
    if user:
        return USER_URL.format(user=user)
    return STATIC_URL


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
    html = _getHTML(_buildUrl(user, console))
    data = _getTag(html, CONSOLE_STATS_TAG)
    try:
        sumStr = ("{user} has the following stats for their {console}:\n"
                  "{unfinished} games unfinished\n{beaten} games beaten\n{complete} games completed")
        if len(data) > 9:
            return sumStr.format(user=user, console=console, unfinished=data[1], beaten=data[8], complete=data[11])
        else:
            return sumStr.format(user=user, console=console, unfinished=data[1], beaten=data[4], complete=data[7])
    except IndexError:
        return "Invalid user \"%s\" or console \"%s\"\n\n%s\n\n%s" % (user, console, html, data)




if __name__ == "__main__":
    print(getConsoleMetrics("zaltu", "pc"))
