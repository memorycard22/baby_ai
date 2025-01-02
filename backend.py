import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            command = None
        return command

def main():
    while True:
        command = listen()
        if command:
            if "exit" in command.lower():
                speak("Goodbye!")
                break
            elif "your name" in command.lower():
                speak("My name is Baby.")
            elif "time" in command.lower():
                from datetime import datetime
                current_time = datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}.")
            else:
                speak("Sorry, I can't do that yet.")

if __name__ == "__main__":
    main()
