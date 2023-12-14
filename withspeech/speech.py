import time
import RPi.GPIO as GPIO
from rpi_lcd import LCD
import pyttsx3
import speech_recognition as sr

# Set up GPIO pins for touch sensing
touch_pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26]  # Adjust the number of pins as needed
GPIO.setmode(GPIO.BCM)
for pin in touch_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up LCD
lcd = LCD()

# Map sets of three characters to each sensor
alphabet_mapping = {
    2: ['ABC'],
    3: ['DEF'],
    4: ['GHI'],
    17: ['JKL'],
    27: ['MNO'],
    22: ['PQR'],
    10: ['STU'],
    9: ['VWX'],
    11: ['YZ '],
    5: ['DEL'],  # Delete button
    6: ['ENT'],  # Enter button
    13: ['   ']   # Space button (three spaces for clarity)
}

# Set up Text-to-Speech
engine = pyttsx3.init()

# Set up SpeechRecognition
recognizer = sr.Recognizer()

# Function to handle touch events
def handle_touch():
    pressed_chars = ""
    timeout_duration = 2  # Set the timeout duration in seconds
    last_touch_time = time.time()

    while True:
        for pin in touch_pins:
            if GPIO.input(pin) == GPIO.LOW:
                # Convert touch event to alphabet based on the mapping
                alphabet_set = alphabet_mapping.get(pin)
                if alphabet_set:
                    pressed_chars += alphabet_set[0]
                    lcd.text(f"Pressed: {alphabet_set[0]}", 1)
                    time.sleep(1)  # Avoid rapid consecutive touch events
                    last_touch_time = time.time()  # Update the last touch time
                else:
                    lcd.text("Invalid sensor", 1)
        
        # Check for timeout
        if time.time() - last_touch_time > timeout_duration:
            lcd.text(f"Sentence: {pressed_chars}", 1)
            speak_text(pressed_chars)
            time.sleep(1)  # Add a delay before resetting pressed_chars
            pressed_chars = ""

# Function to speak text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
try:
    handle_touch()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
    GPIO.cleanup()
