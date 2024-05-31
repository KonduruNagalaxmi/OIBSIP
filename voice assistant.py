import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except:
            print("Sorry, I did not understand.")
            return None

def respond_to_hello():
    speak("Hello! How can I assist you today?")

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def tell_date():
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching the web for {query}")

while True:
    text = get_audio()
    if text is not None:
        if "hello" in text.lower():
            respond_to_hello()
        elif "time" in text.lower():
            tell_time()
        elif "date" in text.lower():
            tell_date()
        elif "exit" in text.lower():
            speak("Goodbye!")
            break
        else:
            search_web(text)
    