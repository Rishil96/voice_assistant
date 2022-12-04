# Voice Assistant
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

id1 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
id2 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"


# listen to the microphone and return the text
def transform_audio_into_string():

    # store recognizer in variable
    recognizer = sr.Recognizer()

    # set microphone
    with sr.Microphone() as source:

        # waiting time
        recognizer.pause_threshold = 0.8

        # recording start message
        print("You can now speak...")

        # save audio
        audio = recognizer.listen(source)

        try:
            # search on google
            request = recognizer.recognize_google(audio, language="en-US")

            print(f"You said: {request}")
            return request

        # does not understand audio
        except sr.UnknownValueError:
            print("Oops! I didn't understand")

            return "I am still listening..."

        # request cannot be resolved
        except sr.RequestError:
            print("Oops! There is no service")

            return "I am still listening..."

        # unexpected error
        except Exception as e:
            print("Oops! Something went wrong!", e)

            return "I am still listening..."


# Function for assistant reply
def speak(message):

    # start engine
    engine = pyttsx3.init()
    engine.setProperty("voice", id2)

    # deliver message
    engine.say(message)
    engine.runAndWait()


# Ask day of the week
def ask_day():

    # integer to week name
    weekly_calendar = {0: "Monday",
                       1: "Tuesday",
                       2: "Wednesday",
                       3: "Thursday",
                       4: "Friday",
                       5: "Saturday",
                       6: "Sunday"}

    today = datetime.date.today()

    # day of the week
    week_day = today.weekday()
    week_day = weekly_calendar[week_day]

    # assistant speaks the day of the week
    speak(f"Today is {week_day}!")


# Inform what time it is now
def ask_time():
    
    # Get the time
    time = datetime.datetime.now()
    hour = time.hour
    minute = time.minute
    noon = "A.M."

    if hour > 12:
        hour = hour % 12
        noon = "P.M."

    # assistant tells the time
    message = f"Hey Rishil, at this moment, it is {hour}:{minute} {noon}!"
    speak(message)


# Initial greeting
def initial_greeting():

    # Give initial greeting to the user
    speak("Hey there, I am Friday.")


# main function of the assistant
def my_assistant():

    # Activate the initial greeting
    initial_greeting()

    # Assistant active
    is_on = True

    while is_on:

        my_request = transform_audio_into_string().lower()

        # Open youtube
        if "open youtube" in my_request:
            speak("Sure, I am opening Youtube!")
            webbrowser.open("https://www.youtube.com")
            continue

        # Open google
        elif "open browser" in my_request or "open google" in my_request:
            speak("Of course, I am on it!")
            webbrowser.open("https://www.google.com")
            continue


my_assistant()
