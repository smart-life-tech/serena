import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:#here the usb mic of the pi was automatically detected
        print("Say something...")
        audio_data = recognizer.listen(source)

    try:
        text_result = recognizer.recognize_google(audio_data)
        print("Speech-to-Text Result:", text_result)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    speech_to_text()
