import bible

verse = bible.Verse()

dictionary = bible.Dictionary()
dictionary.load('dictionary')

dictionary.apply(verse)

print(verse.text)