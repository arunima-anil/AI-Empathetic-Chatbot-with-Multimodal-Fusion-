# AI-Empathetic-Chatbot-with-Multimodal-Fusion

Welcome to the **AI Empathetic Chatbot with Multimodal Fusion** project! This innovative application combines emotion recognition from speech, text, and facial expressions to provide a personalized and empathetic conversational experience. The chatbot integrates various modalities to deliver contextually relevant responses, enhancing user interaction through emotional intelligence.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)
- [Acknowledgments](#acknowledgments)

---

## Features

- **Speech Emotion Recognition (SER):** Detects emotions from spoken words.
- **Text Emotion Recognition (TER):** Analyzes emotions in text input.
- **Facial Emotion Recognition (FER):** Identifies emotions from facial expressions.
- **BlenderBot Response:** Provides empathetic responses based on detected emotions.

---

## Technologies Used

- **Models:**
  - **SER:** `wav2vec2-lg-xlsr-en-speech-emotion-recognition`
  - **TER:** `emotion_text_classifier`
  - **FER:** Custom model (`fer_model.h5`)
  - **Response Generation:** `facebook/blenderbot-400M-distill`
  
- **Libraries:**
  - `requests`, `opencv-python`, `customtkinter`, `tensorflow`, `pillow`, `numpy`, `speech_recognition`, `pyttsx3`

---

## Installation

### Prerequisites

- **Python 3.7 or higher**
- **Pip package manager**

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/AI-Empathetic-Chatbot-with-Multimodal-Fusion.git
   cd AI-Empathetic-Chatbot-with-Multimodal-Fusion


