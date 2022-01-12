import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
# webbrowser.get(chrome_path).open('http://docs.python.org/')
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")

    speak("I am Alexa Mam, Please tell me How may I help you!")

def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer() 
    with sr.Microphone(device_index=0) as source:
        # global query
        print("Listining......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('pallabibehera33@gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pallabibehera33@gmail.com','pallabi100')
    server.sendmail('pallabibehera33@gmail.com',to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    # while True:
    if 1:
        query = takeCommand().lower() 

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("Accoding to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\PALLAVI\\Desktop\\New folder (5)'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Mam the time is {strTime}")

        elif 'open Code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to pallabi' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "pallabibehera33@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am unable to send the Email")
            