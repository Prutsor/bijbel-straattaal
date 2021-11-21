import requests

FEED = "https://feed.dagelijkswoord.nl/api/json/1.0/"

class Verse():
    """ 
        A class used to represent a Verse from Dagelijkswoord.nl
    """
    def __init__(self, language:str='bgt', day:int=0, username:str="", password:str=""):
        self.language = language
        self.day = day
        self.username = username
        self.password = password

        self.text = self.__get()

    def __get(self) -> str:
        """
            Get a the daily quote.
        """
        
        r = requests.get(FEED, auth=(self.username, self.password))

        return r.json()['data'][self.day]['text'][self.language]