import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import pyttsx3
import sounddevice as sd
import numpy as np

print("perfect!!")
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


def voice_input(duration=5):
    r = sr.Recognizer()

    # Record audio for the specified duration
    print("Listening...")
    audio_data = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Audio recording finished.")

    # Convert to bytes
    audio_data = audio_data.flatten()  # Flatten to 1D array
    audio_bytes = audio_data.tobytes()  # Convert to bytes

    # Create an AudioData object for use in speech recognition
    audio = sr.AudioData(audio_bytes, 44100, 2)  # Sample rate and width
    
    try:
        # Use Google's speech recognition API to recognize the audio
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request result from Google Speech Recognition service: {e}")


def text_to_speech(text):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    
    # Set parameters, like speed (words per minute)
    rate = 200  # Adjust this value for faster or slower speech
    engine.setProperty('rate', rate)

    # Save the speech to a file
    audio_file = "speech.mp3"
    engine.save_to_file(text, audio_file)
    engine.runAndWait()
    
    # Open the audio file and read bytes
    with open(audio_file, "rb") as f:
        audio_output = f.read()
    
    return audio_output


def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content(user_text)
    
    result = response.text
    
    return result
