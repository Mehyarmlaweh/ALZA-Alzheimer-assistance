import streamlit as st
import speech_recognition as sr
import spacy
from gtts import gTTS
import tempfile
import os

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Patient data
patient_data = {
    "name": "John",
    "son": "Alex",
    "age": 64,
    "gender": "Male",
    "diabetes": True
}

def verify_response(audio_text):
    doc = nlp(audio_text)

    # Check if son's name mentioned
    son_name_mentioned = any(token.text.lower() == patient_data["son"].lower() for token in doc)

    return son_name_mentioned

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Speak now...")
        audio = recognizer.listen(source)

    try:
        st.write("Analyzing response...")
        # Google Web Speech API
        user_input = recognizer.recognize_google(audio)
        st.write("You said:", user_input)
        return user_input
    except sr.UnknownValueError:
        st.error("Unable to understand audio.")
        return ""
    except sr.RequestError as e:
        st.error("Error requesting Google Speech API: {0}".format(e))
        return ""

def speak_text(text):
    tts = gTTS(text=text, lang="en")
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_file.close()
    tts.save(temp_file.name)
    return temp_file.name

def main():
    st.title("Hello John, could you remind me what your son's name is? ")

    with st.spinner('Waiting for response...'):
        user_response = recognize_speech()

    if user_response:
        if verify_response(user_response):
            st.success("The response is correct. Good job! ✅")
            audio_file = speak_text("The response is correct. Good job!")
            st.audio(audio_file, format="audio/mp3")
            os.remove(audio_file)  
        else:
            st.error("The response is incorrect. Your son's name is Alex ❌")
            audio_file = speak_text("No John, sorry, but your son's name is Alex")
            st.audio(audio_file, format="audio/mp3")
            os.remove(audio_file) 

if __name__ == "__main__":
    main()

