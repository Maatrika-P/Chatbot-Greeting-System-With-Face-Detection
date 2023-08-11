from vosk import Model, KaldiRecognizer
import pyttsx3
import datetime
import pyaudio
import json
import os
import time
import playsound
from playsound import playsound
import msvcrt as m

def wait():
    m.getch()

Disha=pyttsx3.init()  # initializing text to speech
voice=Disha.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0' 
Disha.setProperty('voice',assistant_voice_id)

def speak(audio):
    print('Disha: ' + audio)
    Disha.say(audio)
    Disha.runAndWait()

# Function definitions
def time():
    Time=datetime.datetime.now().strftime('%I:%M: %p')
    speak('It is')
    speak(Time)

def date():
    today=datetime.datetime.now().strftime('the date today is %d %m %Y, please notice that the format is day, month, year')
    speak(today)
    

def welcome():
    hour=datetime.datetime.now().hour
    if hour >=3 and hour <12:
        speak('Good morning')
    elif hour >=12 and hour <18:
        speak('Good afternoon')
    elif hour >=18 and hour <21:
        speak('Good evening')
    elif hour >=21 and hour <24:
        speak('Good night and have a nice dream!')
    elif hour >=0 and hour <3:
        speak('It is late, let us take a nap')
    speak('How can I help you now')
    print('')
    print('listening ...')
    print('')


playsound(r'C:\Users\alsaf\OneDrive\Desktop\assets\.venv\PTNK-on.mp3') #assets/PTNK-on.mp3_start_sound
model=Model(r".venv\vosk_models_in")   #assets/vosk-model-small-en-in-0.4 ## assets/vosk_models_indian_en
#model1= Model(r".venv\vosk_models1_us")
os.system('cls')
welcome()
rec = KaldiRecognizer(model, 16000)

cap=pyaudio.PyAudio()
stream=cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

stream.start_stream()

a=0

while True:
    data=stream.read(4000, exception_on_overflow=False)
    if len(data)==0:
        break

    if rec.AcceptWaveform(data):
        result=rec.Result()
        result=json.loads(result)
        print('Boss: ' + result['text'])
        
        if "hello" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Hello I am Disha, how can I help you?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        
        # Conditions for assistant introduction
        elif "who are you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Hi, I am your virtual assistant. How can I help you now?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        
        elif "who made you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Miki created me. Is there something else you need help with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        
        elif "created" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Miki created me. Is there something else you need help with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        
        elif "where are you from" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('I am from Woxsen University. Is there something else you need help with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        
        
        # Conditions for date & time
        elif "time" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            time()
            speak(f'What else would you like me to do?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        
        elif "date" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            date()
            speak(f'What else would you like me to do?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        
       
        # Conditions for playing music
        elif "music" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'Some music for you, enjoy')
            os.startfile(r'C:\Users\alsaf\OneDrive\Desktop\assets\.venv\RHTDM - Zara Zara.mp3')
            speak('Assistant is paused. You canclick on me and press any key on keyboard to resume me')
            wait()
            speak(f'What else would you like me to do?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        
        elif "stress" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'Some music for you, enjoy')
            os.startfile(r'C:\Users\alsaf\OneDrive\Desktop\assets\.venv\06. Kajra Re.mp3')
            speak('Assistant is paused. You can click on me and press any key on keyboard to resume me')
            wait()
            speak(f'What else would you like me to do?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        
        elif "relax" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'Some music for you, enjoy')
            os.startfile('RHTDM - Zara Zara.mp3')
            speak('Assistant is paused. You can click on me and press any key on keyboard to resume me')
            wait()
            speak(f'What else would you like me to do?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        
        # Condition for stopping the assistant
        elif "computer" in result['text']:
            speak("Assistant is off. Goodbye")
            playsound(r'C:\Users\alsaf\OneDrive\Desktop\assets\.venv\Windows Notify Calendar.wav') #absolute path turnoff_sound
            quit()
        
        else:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('I am sorry. I do not know that.')
            speak('Is there anything else I can help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('') 