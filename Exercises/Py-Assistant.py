"""
Demo Assistant that still under going development
"""
import time
import os
import webbrowser
# from gtts import gTTS
import speech_recognition as sr
import playsound
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def Assistant_Sound(sentence):
    engine.say(sentence)
    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


recognizer = sr.Recognizer()


def Assistant_record():
    with sr.Microphone(device_index=None) as Mic:
        recognizer.adjust_for_ambient_noise(Mic, duration=2)
        input_voice = recognizer.listen(Mic, phrase_time_limit=5)
        voice_str = ""
        try:
            voice_str = recognizer.recognize_google(
                input_voice, language='en-US')
        except sr.UnknownValueError:
            Assistant_Sound("Sorry I did not get that")
        except sr.RequestError:
            Assistant_Sound("Sorry, Down Service")

    return voice_str.lower()


def Assistant_Respond(voice_str):
    if 'name' in voice_str:
        Assistant_Sound("you are the My Nice Friend Ahmed H")


while True:
    voice_str = Assistant_record()
    Assistant_Respond(voice_str)
