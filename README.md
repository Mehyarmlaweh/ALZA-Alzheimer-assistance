# Alzheimer's Assistance Prototype : ALZA

## Overview
ALZA Voice Interactive Prototype is a demonstration of a feature prototype for the ALZA application. This prototype utilizes machine learning and natural language processing (NLP) to create an interactive system for Alzheimer's patients. The system takes vocal input from the patient, analyzes it, and responds to provide assistance and feedback.


## How to Run
1. First, ensure you have Python installed on your system.
2. Install the required dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```
3. Once the dependencies are installed, you can run the project using Streamlit. Execute the following command:
    ```
    streamlit run alza.py
    ```

## Brief Explanation of the Code
- `alza.py`: This Python script contains the main functionality of the application.
    - It utilizes Streamlit for creating a web-based user interface.
    - Speech recognition is implemented using the `SpeechRecognition` library to capture user input.
    - The `spacy` library is used for natural language processing to verify user responses.
    - Text-to-speech functionality is provided by the `gtts` library to provide feedback to the user.
    - The application prompts the user to provide information about their son's name and verifies the response through voice interaction.
    - It demonstrates a basic interaction flow for assisting Alzheimer's patients.

## Note
This project is a prototype and serves as a demonstration of how technology can be used to assist Alzheimer's patients in their daily lives. Further development and refinement would be necessary for a complete and robust application.

