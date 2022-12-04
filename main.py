# Voice Assistant
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


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

    # deliver message
    engine.say(message)
    engine.runAndWait()
