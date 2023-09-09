#import os
import pyttsx3
import speech_recognition as sr
import psutil
from AppOpener import open,close
import whatsapp , change_bg

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id) 
    engine.say(text)
    engine.runAndWait()
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio,language="en-In")
        print(f"user said: {query}")
        return query

speak("Hello I am your Personal Assistant")

while True:
    print("Listening...")
    query = takeCommand()
    speak(query)
    '''
    if "hey Jarvis" in query:
        query = query[len("hey jarvis "):]
        speak(f"Your query is {query}")
        print(query)
    '''
    if "battery status" in query:
        battery = psutil.sensors_battery()
        speak(f" {battery.percent} % charged!!")

    elif "open" in query or "close" in query:
        ind = query.find("open")+5 if "open" in query else query.find("close")+6
        #ind = ind+5 if "open" in query else ind+6
        spc = query.find(" ",ind)
        open_or_close_app = query[ind:spc] if spc>-1 else query[ind:]
        
        open(f"{open_or_close_app}",match_closest=True) if "open" in query else close(f"{open_or_close_app}",match_closest=True)

    elif "play song" in query:
        open("spotify",match_closest=True)
    
    elif "send" in query:
        query = query.split() # list of words in a sentence , format: send message to Satya
        whatsapp.sendBdMsg(query[3])
    elif "change background" in query:
        change_bg.Main()
    elif "exit" in query:
        speak("Have a nice day Sir!!")
        break

