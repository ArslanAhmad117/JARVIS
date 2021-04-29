import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import pyautogui
import  random
curr_music = random.randint(0, 31)
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
            return None
        return query

class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = "MP4"

if __name__ == '__main__':

    wishMe()

    while True:
        query = takeCommand().lower()
        if 'jarvis up' in query:
            movie = Movie_MP4(r"movie.mp4")
            movie.play()
    
        elif "who is" in query:
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
            music_dir = 'C:\\music'
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, song[curr_music]))


    