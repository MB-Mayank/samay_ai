from setuptools import find_packages, setup

setup(
    name="Samay AI",
    version="0.0.1",
    author="mayank",
    author_email="mayankbhushan26@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)