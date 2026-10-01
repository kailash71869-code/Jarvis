import datetime
import logging
import os
import sys
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

#this is logger for the application

LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s ] - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

#taking the male voice from my system

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
if voices:
    engine.setProperty("voice", voices[0].id)  # pyright: ignore[reportIndexIssue]

def speak(text):
    """This function converts text to speech and speaks it out loud.
    
    Args:
       text
    returns:
       voice
    """
    try:
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        logging.exception("Text-to-speech failed")


def take_command():
    """This function takes microphone input from the user and returns it as a string.
    
    Returns:
        text as query.
    """
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
    except sr.WaitTimeoutError:
        print("I did not hear anything.")
        return ""
    except (OSError, sr.RequestError) as error:
        logging.exception("Microphone unavailable: %s", error)
        print("I cannot access the microphone. Check your microphone and PyAudio installation.")
        return ""

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")  # pyright: ignore[reportAttributeAccessIssue]
        print(f"User said: {query}\n")
        logging.info("User said: %s", query)
    except sr.UnknownValueError:
        print("Say that again please...")                  
        return ""
    except sr.RequestError as error:
        logging.exception("Speech recognition service failed: %s", error)
        print("Speech recognition is unavailable. Check your internet connection.")
        return ""
    return query

#this function will wish you

def wish_me():
    """This function will greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am JARVIS!! How can I help you today?")

def handle_command(query):
    """Execute one recognized command and return False when the app should stop."""
    query = query.lower().strip()

    if "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")
    elif "name" in query:
        speak("My name is JARVIS.")
    elif "exit" in query or "quit" in query:
        speak("Goodbye! Have a great day!")
        return False
    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "open leetcode" in query:
        webbrowser.open("https://leetcode.com/contest/")
        speak("Sir i Have opened Leetcode for you.")
    elif "wikipedia" in query:
        speak("I am Searching in Wikipedia...")
        topic = query.replace("wikipedia", "").strip()
        if not topic:
            speak("Please tell me what to search for.")
        else:
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak("According to Wikipedia...")
                print(result)
                speak(result)
            except wikipedia.exceptions.DisambiguationError:
                speak("That search has multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I could not find that Wikipedia page.")
            except wikipedia.exceptions.WikipediaException:
                logging.exception("Wikipedia request failed")
                speak("Wikipedia is unavailable right now.")
    return True


def main():
    """Start the voice assistant."""
    wish_me()
    while True:
        query = take_command()
        if query and not handle_command(query):
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nJARVIS stopped.")
        sys.exit(0)
