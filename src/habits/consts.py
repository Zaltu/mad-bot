"""
Constants specifically for use with the Habits module.
"""
from src.consts import ZALTU, NASS, FRANK

SPECIAL_DAYS = {
    "01/01": "Happy New Year!",
    "14/02": "Happy Valentine's Day!",
    "03/05": "Memento Mori",
    #Easter's a bitch,
    "01/07": "Happy Canada Day eh?",
    "04/07": "God Bless America!",
    "11/07": "Happy Birthday %s!" % ZALTU,
    "24/10": "Happy Birthday %s!" % FRANK,
    "26/10": "Happy Birthday %s!" % NASS,
    "31/10": "Happy Halloween!",
    "25/12": "Merry Christmas!"
}
