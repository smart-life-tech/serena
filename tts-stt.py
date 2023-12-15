'''
run these two commands on the terminal
sudo apt-get update
sudo apt-get install espeak
sudo apt-get install --reinstall alsa-utils
sudo alsa force-reload


No Default Input Device Available:
The error "OSError: No Default Input Device Available" suggests that the script is
 unable to find a default microphone on your Raspberry Pi.
Make sure you have a functional microphone connected to your Raspberry Pi. 
Additionally, you can try specifying the microphone index explicitly in the Microphone constructor. 
First, identify the index of your microphone using the following command:

test this command on termianl

arecord -l
'''

import pyttsx3
import speech_recognition as sr

# Set up Text-to-Speech
engine = pyttsx3.init()

# Set up SpeechRecognition
recognizer = sr.Recognizer()

# Function to speak text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to capture speech and return text
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Processing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech not recognized"
    except sr.RequestError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Text-to-Speech
    text_to_speak = "Hello, how are you?"
    speak_text(text_to_speak)

    # Speech-to-Text
    recognized_text = recognize_speech()
    print(f"Recognized Text: {recognized_text}")
