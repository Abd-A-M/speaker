    def speaker(personName):
        engine = pyttsx3.init()
        engine.setProperty('rate', 0.9)
        # volume = engine.getProperty('volume')
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
        voices = engine.getProperty('voices')  # getting details of current voice
        engine.setProperty('voice', voices[40].id)  # changing index, changes voices. 1 for female
        engine.say("wanted ")
        engine.say("wanted ")
        engine.say(personName)
        engine.runAndWait()
        engine.stop()
speaker(personName)
