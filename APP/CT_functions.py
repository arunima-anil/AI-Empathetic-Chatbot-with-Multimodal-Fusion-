import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import numpy as np
import speech_recognition as sr
import pyttsx3
from api import query_SER, query_TER, query_response

# Global variable to track the camera state
camera_active = False
cap = None

# Function to activate camera with FER
def activate_camera(video_display, fer_model, faceCascade, fer_emotion_label):
    global camera_active, cap
    print("Camera Toggled")
    if camera_active:
        # Release the camera and close the window
        cap.release()
        cv2.destroyAllWindows()
        camera_active = False
        # Clear the video display area
        video_display.configure(image=None)
    else:
        # Initialize the camera
        cap = cv2.VideoCapture(0)  # 0 for the default camera
        if not cap.isOpened():
            print("Error: Unable to access the camera.")
            return
        camera_active = True
        # Create a function to update the video display area with facial emotion recognition
        def update_display():
            ret, frame = cap.read()
            if ret:
                # Convert the OpenCV BGR frame to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Detect faces in the frame
                faces = faceCascade.detectMultiScale(rgb_frame, 1.1, 4)
                # Iterate over detected faces
                for x, y, w, h in faces:
                    # Extract face ROI
                    face_roi = rgb_frame[y:y+h, x:x+w]
                    # Resize and preprocess the face ROI for prediction
                    resized_face = cv2.resize(face_roi, (48, 48))
                    resized_face = np.expand_dims(resized_face, axis=0) / 255.0
                    # Perform prediction using the pre-loaded FER model
                    prediction = fer_model.predict(resized_face)
                    # Determine the emotion label
                    emotion_label = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"][np.argmax(prediction)]
                    # Draw bounding box around the face and display emotion label
                    cv2.rectangle(rgb_frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    cv2.putText(rgb_frame, emotion_label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                    fer_emotion_label.configure(text="FER Emotion: " + emotion_label)
                # Convert the RGB frame to a PIL Image
                img = Image.fromarray(rgb_frame)
                # Convert the PIL Image to a Tkinter-compatible PhotoImage
                imgtk = ImageTk.PhotoImage(image=img)
                # Update the video display area with the new frame
                video_display.configure(image=imgtk)
                video_display.imgtk = imgtk
                # Schedule the update function to be called again after 10 milliseconds
                video_display.after(10, update_display)
            else:
                print("Error: Failed to read frame.")
                # Release the camera and close the window
                cap.release()
                cv2.destroyAllWindows()
                camera_active = False
                # Clear the video display area
                video_display.configure(image=None)

        # Call the update_display function to start displaying the video feed
        update_display()

def activate_microphone(transcription_text, ser_emotion_label, ter_emotion_label, speak_label):
    # Initialize the recognizer
    r = sr.Recognizer()
    print("Speak now")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Function to transcribe audio and process emotions
    def transcribe_and_detect_emotion():
        with sr.Microphone() as source:
            speak_label.configure(text="Click below to speak")
            audio = r.listen(source)
            print("Processing")

            # Query SER model to process emotions
            try:
                ser_output = query_SER(audio)
                print("\nSER_Output: \n", ser_output)
                ser_emotion_label.configure(text="SER Emotion: " + ser_output[0].get('label', 'Unknown') + ' ('+str(ser_output[0]['score']*100)[:4]+'%)')
            except:
                ser_emotion_label.configure(text="SER Emotion: Unknown")

            try:
                # Recognize the speech using Google Web Speech API
                text = r.recognize_google(audio)
                # Display the transcribed text
                transcription_text.insert(ctk.END, f'YOU: {text}' + "\n")

                # Query TER model to process text emotions
                try:
                    ter_output = query_TER(text)
                    print("\nTER_Output: \n", ter_output)
                    ter_emotion_label.configure(text="TER Emotion: " + ter_output[0][0].get('label', 'Unknown') + ' ('+str(ter_output[0][0]['score']*100)[:4]+'%)')
                except:
                    ter_emotion_label.configure(text="TER Emotion: Unknown")

                # Query Blenderbot model with transcribed text
                try:
                    response_output = query_response(text)
                    print("\nResponse_Output: \n", response_output)
                    response_text = 'BOT: ' + str(response_output[0]['generated_text'])
                except:
                    response_text = "Response not generated, please try again\n"

                transcription_text.insert(ctk.END, response_text + "\n")

                # Output the response as speech
                engine.say(response_text)
                engine.runAndWait()

            except sr.UnknownValueError:
                print("Google Web Speech API could not understand the audio.")
            except sr.RequestError as e:
                print("Could not request results from Google Web Speech API; {0}".format(e))

    transcribe_and_detect_emotion()
