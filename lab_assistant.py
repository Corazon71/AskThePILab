import os
from RAG import start
from openai import OpenAI
import time
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import pygame
import sys
import RPi.GPIO as GPIO
from RPLCD import i2c

led_pin = 17
button1_pin = 4  
button2_pin = 27 
button3_pin = 22  

lcd_columns = 16
lcd_rows = 2
i2c_expander = 'PCF8574'
i2c_address = 0x27  

r = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)
pygame.mixer.init()
lcd = i2c.CharLCD(i2c_expander, i2c_address, cols=lcd_columns, rows=lcd_rows)

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "response.mp3"
    tts.save(filename)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  
        pygame.time.Clock().tick(10)

def lcd_display(text):
    lcd.clear()
    lcd.write_string(text)

def button1_pressed_callback(channel):
    global listening
    listening = True
    lcd_display("Listening...")

def button2_pressed_callback(channel):
    if last_response:
        speak(last_response)

def button3_pressed_callback(channel):
    if last_text:
        speak(f"You said: {last_text}")

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
for pin in [button1_pin, button2_pin, button3_pin]:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(button1_pin, GPIO.RISING, callback=button1_pressed_callback, bouncetime=200)
GPIO.add_event_detect(button2_pin, GPIO.RISING, callback=button2_pressed_callback, bouncetime=200)
GPIO.add_event_detect(button3_pin, GPIO.RISING, callback=button3_pressed_callback, bouncetime=200)

listening = False
last_response = ""
last_text = ""
while True:
    if listening:
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio).lower()
            print(f"You said: {text}")
            last_text = text
            if text in ["yes", "no"]:
                speak(f"You said {text}.")
            else:
                lcd_display("Processing...")
                response_text = start(text)
                print(response_text)
                last_response = response_text
                lcd_display("Answering...")
                speak(response_text)
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            speak("Sorry, I didn't understand that.")
        finally:
            listening = False
    else:
        lcd_display("Standby")
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.5)

GPIO.cleanup()
lcd.clear()
