import requests
import json

CONFIG = json.load(open('config.json'))
FEED = "https://feed.dagelijkswoord.nl/api/json/1.0/"

class Verse():
    def __init__(self, language='bgt', day=0):
        self.language = language
        self.day = day

        self.text = self.__get()

    def __get(self):
        r = requests.get(FEED, auth=(CONFIG['username'], CONFIG['password']))

        return r.json()['data'][self.day]['text'][self.language]