import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import pyttsx3

print("perfect!!")
load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY



def voice_input():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))
    

def text_to_speech(text):
    # tts=gTTS(text=text, lang="en",slow=False)
    
    # #save the speech from the given text in the mp3 format
    # tts.save("speech.mp3")
    
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
    #model = "models/gemini-pro"
    
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-pro')
    
    response=model.generate_content(user_text)
    
    result=response.text
    
    return result
    
    
    
    
