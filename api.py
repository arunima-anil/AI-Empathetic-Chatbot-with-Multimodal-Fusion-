import requests

# SER (Speech Emotion Recognition) model API details
SER_API_URL = "https://api-inference.huggingface.co/models/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition"
SER_HEADERS = {"Authorization": "Bearer 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"}

# TER (Text Emotion Recognition) model API details
TER_API_URL = "https://api-inference.huggingface.co/models/michellejieli/emotion_text_classifier"
TER_HEADERS = {"Authorization": "Bearer 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"}

# BlenderBot Response model API details
RESPONSE_API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
RESPONSE_HEADERS = {"Authorization": "Bearer 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"}

# Function to query SER model
def query_SER(audio):
    response = requests.post(SER_API_URL, headers=SER_HEADERS, data=audio.get_wav_data())
    return response.json()

# Function to query TER model
def query_TER(text):
    response = requests.post(TER_API_URL, headers=TER_HEADERS, json={"inputs": text})
    return response.json()

# Function to query the Blenderbot model
def query_response(text):
    print("Blenderbot accessed")
    response = requests.post(RESPONSE_API_URL, headers=RESPONSE_HEADERS, json={'inputs':text})
    print("Blenderbot exited")
    return response.json()
