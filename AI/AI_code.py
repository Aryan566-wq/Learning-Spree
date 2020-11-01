import pyttsx3
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Karen. Please tell me how may I help you")

def takeCommand():
    query = input("")
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        try:
            if 'wikipedia' in query:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak('Searching Wikipedia...')
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak("opening youtube...")
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                speak("opening google...")
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                speak("opening stackoverflow")
                webbrowser.open("stackoverflow.com")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'help' in query:
                print("""valid commands:
                      open youtube
                      open google
                      open stackoverflow
                      what is the time("the time" in short)
                      "search topic" wikipedia(eg: shah rukh khan wikipedia)""")

        except Exception as e:
            speak("sorry i do not understand you, please type help for knowing what I can do")
