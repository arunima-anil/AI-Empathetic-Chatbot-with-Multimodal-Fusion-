import cv2
import tkinter as tk
from tensorflow.keras.models import load_model
#from functions2 import activate_camera
from functions import activate_microphone, activate_camera


# Load pre-trained FER model
try:
    fer_model = load_model(r"D:\JEC\MAIN PROJECT PHASE 2\project\new model\fer_model.h5")
    print("FER model is loaded")
except:
    print("FER model not loaded")

# Define face cascade classifier
try:
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    print("Cascade Classifier ready")
except:
    print("Cascade Classifier NOT ready")

# Create the main application window
root = tk.Tk()
root.title("Emotion Recognition Chatbot")
root.geometry("800x500")

# Create a frame to hold the UI elements
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create and add a label to the frame
label = tk.Label(frame, text="Emotion Recognition", font=("Arial", 18))
label.pack(pady=10)

# Create a rectangular box for displaying transcribed audio
transcription_text = tk.Text(frame, height=8, width=100)
transcription_text.pack()

# Create a label to indicate speaking
speak_label = tk.Label(frame, text="Click below to speak")
speak_label.pack()

# Create and add a button to activate the microphone
microphone_button = tk.Button(frame, text="Activate Microphone", command=lambda: activate_microphone(transcription_text, ser_emotion_label, ter_emotion_label, speak_label))
microphone_button.pack(pady=10)

# Create and add a label for SER emotion
ser_emotion_label = tk.Label(frame, text="SER Emotion: ")
ser_emotion_label.pack()

# Create and add a label for TER emotion
ter_emotion_label = tk.Label(frame, text="TER Emotion: ")
ter_emotion_label.pack()

fer_emotion_label = tk.Label(frame, text="FER Emotion: ")
fer_emotion_label.pack()

# Create and add a button to activate the camera
camera_button = tk.Button(frame, text="Activate Camera", command=lambda: activate_camera(video_display,fer_model,faceCascade,fer_emotion_label))
camera_button.pack(pady=10)

# Create and add a placeholder video display area
video_display = tk.Label(frame, text="Video Display Area", bg="lightgray", width=500, height=300)
video_display.pack()

# Start the Tkinter event loop
root.mainloop()