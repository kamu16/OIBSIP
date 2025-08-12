import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

# Initialize the engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def talk(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"You: {command}")
            return command
        except:
            talk("Sorry, I didn't get that.")
            return ""

def run_assistant():
    talk("Hello! I'm your assistant. How can I help you?")
    while True:
        command = listen()

        if 'play' in command:
            song = command.replace('play', '')
            talk(f'Playing {song}')
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f'Current time is {time}')

        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, sentences=2)
            talk(info)

        elif 'open youtube' in command:
            talk('Opening YouTube')
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in command:
            talk('Opening Google')
            webbrowser.open("https://www.google.com")

        elif 'exit' in command or 'stop' in command:
            talk("Goodbye!")
            break

        elif command:
            talk("I didn't understand that. Please say it again.")

# Run the assistant
run_assistant()
