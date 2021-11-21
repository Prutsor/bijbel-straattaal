import validators
import requests
import os

class Dictionary:
    def __init__(self):
        pass

    def load(self, file='dictionary'):
        if os.path.isfile(file):
            self.__file = open(file, 'r')
            self.__lines = self.__file.readlines()
        elif validators.url(file):
            self.__file = requests.get(file).text
            print(self.__file)
            self.__lines = self.__file.splitlines()
        self.__dict = {}

        for line in self.__lines:
            line = line.strip()

            words, meaning = line.split('=')

            for word in words.split(','):
                self.__dict[word] = meaning
        
    def apply(self, verse):
        text = verse.text.lower()

        for word in self.__dict:
            text = text.replace(word, self.__dict[word])

        verse.text = text

