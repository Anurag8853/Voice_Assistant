import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            return command.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble understanding you right now.")
            return ""

# Main program loop
while True:
    command = listen()

    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak("The current time is " + current_time)

    elif "search" in command:
        speak("What would you like to search for?")
        search_query = listen()
        if search_query:
            url = "https://www.google.com/search?q=" + search_query
            webbrowser.open(url)
            speak("Here are the search results for " + search_query)

    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "exit" in command:
        speak("Goodbye!")
        break




