import pyttsx3
from gtts import gTTS
from pyaudio import PyAudio
import speech_recognition as sr
import os
import datetime
import cv2
import sys
import numpy as np
import face_recognition
from datetime import timedelta
import time

currentTime = datetime.datetime.now()
currentTime.hour


firstRun = True
time1 = datetime.datetime.now()

Listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# previousName = " "

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[0].id)
# engine.setProperty('rate',170)

def Speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



# def Speak_Assis(audio):
#     kk = gTTS(audio)
#     kk.save('Assis.mp3')
#     playsound('Assis.mp3')

# Speak("How can i help you")
def OpenCamera():
    currentTime = datetime.datetime.now()
    currentTime.hour


    firstRun = True
    time1 = datetime.datetime.now()

    # Listener = sr.Recognizer()
    # engine = pyttsx3.init()

    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)


    previousName = " "

    # engine = pyttsx3.init()
    # rate = engine.getProperty('rate')
    # engine.setProperty('rate', rate-40)

    path = (r'C:\Users\alsaf\OneDrive\Desktop\Disha\\images')
    images = []
    personName = []
    myList = os.listdir(path)
    print(myList)

    for cur_img in myList:
        current_Img = cv2.imread(f'{path}/{cur_img}')
        images.append(current_Img)
        personName.append(os.path.splitext(cur_img)[0])
    print(personName)


    def faceEncoding(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnown = faceEncoding(images)
    print("All Encoding complete!!!")

    cap = cv2.VideoCapture(0)

    if 1:
        ret, frame = cap.read()
        faces = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)


        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches =face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)


            if matches[matchIndex]:
                name = personName[matchIndex].title()
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0), 2)
                cv2.rectangle(frame, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 2)
                diff = datetime.datetime.now() - time1
                delta = timedelta(seconds = 120)
                if (name != previousName) and (diff > delta or firstRun):
                    if 5 <= currentTime.hour < 12:
                        result = ('Good Morning' + name)
                    elif 12 <= currentTime.hour < 18:
                        result = ('Good Afternoon' + name)
                    else:
                        result = ('Good Evening' + name)
                    if(previousName == " "):
                        firstRun = True
                    else:
                        firstRun = False
                        time1 = datetime.datetime.now()

                    engine.say(result + 'Nice to meet you')
            
                previousName = name
                time.sleep(0.3)
                engine.runAndWait()
            else:
                previousName = " "

        cv2.imshow("Camera", frame)
        if cv2.waitKey(10) == 13:
            sys.exit()
    
    cap.release()
    cv2.destroyAllWindows()

    # exit()



def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening.......")

        r.pause_threshold = 1

        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        

        query = r.recognize_google(audio, language='en')

        print(f"user said: {query}")

    except Exception as e:

        # Speak("Say that again please......")


        return "none"

    query = query.lower()
    return query

def TaskExcution(): 
    if 1:
        query = OpenCamera()
    while True:
        # if 1:
        #     query = OpenCamera()
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
        if "hello" in permission:
            TaskExcution()
        elif "bye" in permission:
            Speak("thanks for using me, have a good day")
            sys.exit()
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


