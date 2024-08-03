# AI-Empathetic-Chatbot-with-Multimodal-Fusion-


Welcome to the Empathetic Chatbot project! This innovative application combines emotion recognition from speech, text, and facial expressions to provide a personalized and empathetic conversational experience.

## Features

- **Speech Emotion Recognition (SER)**: Detects emotions from spoken words using advanced audio processing.
- **Text Emotion Recognition (TER)**: Analyzes and interprets emotions conveyed through text input.
- **Facial Emotion Recognition (FER)**: Utilizes camera input to detect and interpret facial expressions.
- **BlenderBot Response**: Generates contextually relevant and empathetic responses based on detected emotions and user input.

## Technologies Used

- **Models**:
  - **SER**: `wav2vec2-lg-xlsr-en-speech-emotion-recognition`
  - **TER**: `emotion_text_classifier`
  - **FER**: Custom model (`fer_model.h5`)
  - **Response Generation**: `facebook/blenderbot-400M-distill`
- **Libraries**:
  - `requests` - For API interactions
  - `opencv-python` - For facial detection and video processing
  - `customtkinter` - For creating the graphical user interface
  - `tensorflow` - For loading and using the FER model
  - `pillow` - For image processing
  - `numpy` - For numerical operations
  - `speech_recognition` - For converting speech to text
  - `pyttsx3` - For text-to-speech functionality

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/empathetic-chatbot.git
   cd empathetic-chatbot
