import pyttsx3
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
import datetime
import cv2
import sys
import numpy
import face_recognition
from datetime import timedelta
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',170)

def Speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



# def Speak_Assis(audio):
#     kk = gTTS(audio)
#     kk.save('Assis.mp3')
#     playsound('Assis.mp3')

# Speak("How can i help you")

def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening.......")

        r.pause_threshold = 1

        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        

        query = r.recognize_google(audio, language='en-in')

        print(f"user said: {query}")

    except Exception as e:

        # Speak("Say that again please......")


        return "none"

    query = query.lower()
    return query

def TaskExcution():
    while True:
        Speak ("How can i help you")
        query = TakeCommand()
        if 'hi' in query:
            engine.say("how can i help you")
            engine.runAndWait()
        elif 'how was your day' in query:
            engine.say("it's been ok, thanks for asking")
            engine.runAndWait()
        elif 'you can sleep' in query:
            Speak("Ok , i am gonna sleep now you can call me anytime")
            break  

# def TaskExcution():
#     Speak("How can i help you?")
#     query = TakeCommand().lower()

#     if 'hi' in query:
#         engine.say("hello, what can i do for you?")
#         engine.runAndWait()
        
#     elif 'how was your day' in query:
#         engine.say('its been ok, thanks for asking')
#         engine.runAndWait()
        
#     elif'what is the time' in query:
#         time = datetime.datetime.now().strftime('%H, %M, %S')
#         print(time)
#         Speak('Current time is' + time)

#     elif 'open camera' in query:
#         cap = cv2.VideoCapture(0)
#         while True:
#             ret, img = cap.read()
#             cv2.imshow('webcam', img)
#             k = cv2.waitKey(50)
#             if k==27:
#                 break
#             cap.release()
#             cv2.destroyAllWindows()
#     elif 'bye' in query:
#         Speak("thanks for using me, have a good day")
#         sys.exit()
        
#     Speak("what else do you want me to do?")

if __name__ == "__main__":
    while True:
        permission = TakeCommand()
        if "hello disha" in permission:
            TaskExcution()
        elif "bye" in permission:
            Speak("thanks for using me, have a good day")
            sys.ext()
# if __name__ == "__main__":
#     # TakeCommand()
    
#     while True:
#         permission = TakeCommand()
#         if "hello" in permission:
#             TaskExcution()
#         elif "goodbye" in permission:
#             sys.exit()

        # if 'hello' or 'hi' or 'good morning' or 'good afternoon' or 'good evening' in query:
        #     engine.say('hello, what can i do for you?')
        #     engine.runAndWait()
        # elif 'how was your day' in query:
        #     engine.say('its been ok, thanks for asking')
        #     engine.runAndWait()
        # elif 'what is the time'in query:
        #     time = datetime.datetime.now().strftime('%H %M %S')
        #     print(time)
        #     Speak('Current time is' + time)
        # elif "open camera" in query:
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #         ret, img = cap.read()
        #         cv2.imshow('webcam', img)
        #         k = cv2.waitKey(50)
        #         if k==27:
        #             break
        #         cap.release()
        #         cv2.destroyAllWindows()


    # kk = open('Data.txt', 'rb')
    # kk.write(f": {query}")
    # kk.close()


    # return query.lower()
# def TakeExecution():
#     while True:
#         permission = TakeCommand()
#         if "wake up" in permission:
#             TakeExecution()
#         elif "goodbye" in permission:
#             Speak("thanks for using me, have a good day")
#             sys.exit()


