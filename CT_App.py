import cv2
import customtkinter as ctk
from tensorflow.keras.models import load_model
#from functions2 import activate_camera
from CT_functions import activate_microphone, activate_camera


# Load pre-trained FER model
try:
    fer_model = load_model(r"new model\fer_model.h5")
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
root = ctk.CTk()
root.title("Emotion Recognition Chatbot")
root.geometry("800x600")


# Create a frame to hold the heading and description
header_frame = ctk.CTkFrame(root)
header_frame.pack(pady=10)

# Create and add the heading
heading = ctk.CTkLabel(header_frame, text="Empathetic Chatbot", font=("calibri",25,"bold"))
heading.pack(pady=10)

# Create and add the description
description = ctk.CTkLabel(header_frame, text="*** This chatbot uses emotion recognition to provide empathetic responses ***\n\n*** You can use the application with or without activating the camera ***\n\n*** Interact with the bot by activating the microphone ***", wraplength=600,font=("arial",11))
description.pack(padx=10,pady=(0,10))

# Create the left and right frames
left_frame = ctk.CTkFrame(root)
left_frame.pack(side="left", padx=10, expand=True)

right_frame = ctk.CTkFrame(root)
right_frame.pack(side="right", padx=10, expand=True)

# Create a rectangular box for displaying transcribed audio
transcription_text = ctk.CTkTextbox(right_frame, height=190, width=500)
transcription_text.pack(padx=(10,10),pady=10)

# Create a label to indicate speaking
speak_label = ctk.CTkLabel(right_frame, text="Click below to speak")
speak_label.pack()

# Create and add a button to activate the microphone
microphone_button = ctk.CTkButton(right_frame, text="Activate Microphone", command=lambda: activate_microphone(transcription_text, ser_emotion_label, ter_emotion_label, speak_label))
microphone_button.pack(pady=10)

# Create and add a label for SER emotion
ser_emotion_label = ctk.CTkLabel(right_frame, text="SER Emotion: ")
ser_emotion_label.pack()

# Create and add a label for TER emotion
ter_emotion_label = ctk.CTkLabel(right_frame, text="TER Emotion: ")
ter_emotion_label.pack()

# Create and add a label for FER emotion
fer_emotion_label = ctk.CTkLabel(right_frame, text="FER Emotion: ")
fer_emotion_label.pack(pady=(0,10))

# Create and add a placeholder video display area
video_display = ctk.CTkLabel(left_frame, text=" ", fg_color="lightgray", width=500, height=320)
video_display.pack(padx=(10,10),pady=10)

# Create and add a button to activate the camera
camera_button = ctk.CTkButton(left_frame, text="Activate Camera", command=lambda: activate_camera(video_display, fer_model, faceCascade, fer_emotion_label))
camera_button.pack(pady=(0,10))

# Start the CustomTkinter event loop
root.mainloop()