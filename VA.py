import pyttsx3
engine= pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("hello i am alexa, i am your personal assitant")