import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import pyautogui
import  random
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("GOOD MORNING SIR ")
    elif hour <= 12 and hour > 18:
        speak("GOOD AFTERNOON SIR")
    else:
        speak("GOOD EVENING SIR")
def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            query = query.lower()
            print(f"User said {query}\n")
        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query
def start():
    print("JARVIS POWERING UP")
    speak("JARVIS POWERING UP")
    print("CONNECTING TO SERVERS...")
    speak("CONNECTING TO SERVERS")
    print("DOWNLOADING DRIVERS...")
    speak("DOWNLOADING DRIVERS")
    print("INSTALLING DRIVERS...")
    speak("INSTALLING DRIVERS")
    print("JARVIS ON SIR HOW MAY I HELP YOU")
    speak("JARVIS ON SIR HOW MAY I HELP YOU")

if __name__ == '__main__':


    password = pyautogui.password('ENTER THE PASSWORD')
    if password=='arslan':
        wishMe()
        start()

        while True:
            query = takeCommand().lower()

            if "who is" in query:
                query = query.replace("who is ", " ")
                # print(query)
                query = wikipedia.summary(query, sentences=2)
                print(query)
                speak(query)
            elif "what is" in query:
                query = query.replace("what is ", " ")
                query = wikipedia.summary(query, sentences=2)
                print(query)
                speak(query)
            elif 'open youtube' in query:
                webbrowser.open_new("youtube.com")
            elif 'play music' in query:
                music_1 = random.randint(0, 2)
                music_dir = 'C:\\music'
                song = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, song[music_1]))


    else:
        speak('WRONG PASSWORD..... PLEASE TRY AGAIN')
        pyautogui.keyDown('shift')
        pyautogui.press('f10')
        pyautogui.keyUp('shift')