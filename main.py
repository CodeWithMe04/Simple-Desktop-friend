import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme(name):
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning")
        print("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")

    speak(f"I am JARVIS {name}. How can I help you?")
    print(f"I am JARVIS {name}. How can I help you?")


def takecmd(name, command):
    if command == "How are you?" or command == "how are you":
        speak(f"I am fine {name}, how are you?")
        print(f"I am fine {name}, how are you?")
    elif command == "How you can help me?" or command == "how you can help me":
        speak(f"I can do anything like a your friend")
        print(f"I can do anything like a your friend")
    elif command == "Open google.com" or command == "open google":
        print("Opening google...")
        webbrowser.open("https://google.com")
    elif command == "wishme" or command == "wishme again":
        wishme(name)
    else:
        speak(f"Something want wrong while doing {command}...")
        print(f"Something want wrong while doing {command}...")


if __name__ == '__main__':
    name = "Arin"
    wishme(name)
    while True:
        cmd = str(input("Enter your prompt(q to quit): "))
        if cmd == "q":
            break
        takecmd(name, cmd)
