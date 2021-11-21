import validators
import requests
import os
from .verse import Verse

class Dictionary:
    def load(self, file:str='dictionary'):
        """
            Load the file that contains the meaning of certain words.
        """
        
        if os.path.isfile(file):
            self.__file = open(file, 'r')
            self.__lines = self.__file.readlines()
        elif validators.url(file):
            self.__file = requests.get(file).text
            self.__lines = self.__file.splitlines()
        self.__dict = {}

        for line in self.__lines:
            line = line.strip()

            words, meaning = line.split('=')

            for word in words.split(','):
                self.__dict[word] = meaning
        
    def apply(self, verse: Verse):
        """
            Apply the meaning of the words to a Verse object
        """
        
        text = verse.text.lower()

        for word in self.__dict:
            text = text.replace(word, self.__dict[word])

        verse.text = text

