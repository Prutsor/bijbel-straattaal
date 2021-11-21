import requests

FEED = "https://feed.dagelijkswoord.nl/api/json/1.0/"

class Verse():
    def __init__(self, language='bgt', day=0, username="", password=""):
        self.language = language
        self.day = day
        self.username = username
        self.password = password

        self.text = self.__get()

    def __get(self) -> str:
        """
            Get a the daily quot.
        """
        
        r = requests.get(FEED, auth=(self.username, self.password))

        return r.json()['data'][self.day]['text'][self.language]