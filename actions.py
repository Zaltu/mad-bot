"""
Functions for all possible actions
"""
import random
import json
import backdoorgery

JSON_PATH = "db/"
QUOTES_FILE = "quotes.json"

class DiscordBody(object):
    """
    Possible 'actions' the bot may take.
    """
    def __init__(self, mind):
        self.mind = mind
        self.vars = {}

    def interface(self, command):
        """
        Call the given command

        :returns: the result of the command
        :rtype: obj
        """
        return command()

    def text(self, text):
        """
        1 Billion IQ Developer

        :param str text: the text to return

        :returns: the text param
        :rtype: str
        """
        return text.format(author=self.vars['author'],
                           channel=self.vars['channel'],
                           input=self.vars['input'])

    def nyx(self):
        """
        Generate a random Nyx quote

        :returns: one of Nyx's final battle quotes.
        :rtype: str
        """
        return random.sample({
            "Celebrate life's grandeur. Its brilliance. Its magnificence.",
            "There is both joy and wonder in coming to understand another.",
        }, 1)[0]

    def owo(self):
        """
        NYI
        See Sagiri's owo command implementation

        :returns: "OwO"
        :rtype: str
        """
        return "OwO"

    def games(self):
        """
        Show some stats based off of a user and a console

        :returns: the command terms if improperly called or a user's console metrics
        :rtype: str
        """
        terms = self.vars['text'].split(" ")[1:]
        if len(terms) < 2:
            return ".games takes a {user} and a {console}"
        return backdoorgery.getConsoleMetrics(terms[0], terms[1])

    def quote(self):
        """
        Fetch a user's quote

        :returns: a quote or an appropriate error
        :rtype: str
        """
        try:
            quotee = self.vars['text'].split(" ")[1]
        except (KeyError, IndexError):
            return "No one to quote"
        with open(JSON_PATH+QUOTES_FILE, 'r+') as quote_file:
            quotes = json.load(quote_file)

        try:
            userquotes = quotes[quotee]
        except KeyError:
            return "{user} has no registered quotes".format(user=quotee)
        return random.sample(userquotes, 1)[0]

    def addquote(self):
        """
        Add a quote to a user's quote bank

        :returns: confirmation of receipt
        :rtype: str
        """
        terms = self.vars["text"].split(" ")
        try:
            quotee = terms[1]
            quote = " ".join(terms[2:])
        except (KeyError, IndexError):
            return "Woah there son, you aren't even quoting anything."
        formattedQuote = quote + "\n    - " + quotee
        with open(JSON_PATH+QUOTES_FILE, 'r+') as quote_file:
            quotes = json.load(quote_file)
        if quotee in quotes:
            quotes[quotee].append(formattedQuote)
        else:
            quotes.setdefault(quotee, [formattedQuote])
        with open(JSON_PATH+QUOTES_FILE, 'w+') as quote_file:
            quote_file.write(json.dumps(quotes))

        return "I'll remember that."


if __name__ == "__main__":
    B = DiscordBody('test')
    B.vars = {"text": ".quote"}
    print(B.quote())
    B.vars = {"text": ".quote @Zaltu"}
    print(B.quote())
    B.vars = {"text": ".addquote"}
    print(B.addquote())
    B.vars = {"text": ".addquote @Zaltu all games are bad"}
    print(B.addquote())
    B.vars = {"text": ".quote @Zaltu"}
    print(B.quote())
