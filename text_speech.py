import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):                  
    tts = gTTS(text=text,lang='en')           #text to speech
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)      #reducing intencity of noise from input speech
        audio = r.listen(source)
        said = ""

        try:
            said  = r.recognize_google(audio)      #speech to text
            print(said)
        except Exception as e:
            print("Exception: "+str(e))

    return said        



text = get_audio()     #taking speech and convering it into text and then print that on console


if "hello" in text:
    speak("Good Evening")     #converting given argument into speech and answering back to input  
else:
    speak("Have a great day")

