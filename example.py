import straattaal_bijbel

verse = straattaal_bijbel.Verse(username="username", password="password") # https://www.dagelijkswoord.nl/verspreiden/json-feed

dictionary = straattaal_bijbel.Dictionary()
dictionary.load('dictionary')

dictionary.apply(verse)

print(verse.text)
