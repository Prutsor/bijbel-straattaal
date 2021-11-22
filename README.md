# straattaal-bijbel

To make an account go to https://www.dagelijkswoord.nl/verspreiden/json-feed and scroll down until you see "API Key aanvragen".

## Example

```
import straattaal_bijbel

verse = straattaal_bijbel.Verse(username="username", password="password") # https://www.dagelijkswoord.nl/verspreiden/json-feed

dictionary = straattaal_bijbel.Dictionary()
dictionary.load('dictionary')

dictionary.apply(verse)

print(verse.text)
```

## Example with Text-to-Speech

```
import straattaal_bijbel

verse = straattaal_bijbel.Verse(username="username", password="password") # https://www.dagelijkswoord.nl/verspreiden/json-feed

dictionary = straattaal_bijbel.Dictionary()
dictionary.load('dictionary')

dictionary.apply(verse)

tts = straattaal_bijbel.TextToSpeech()
tts.say(verse, language="nl", slow=False)

print(verse.text)
```
