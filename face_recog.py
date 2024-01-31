import cv2
import face_recognition
import pyttsx3
import sounddevice as sd
import numpy as np

# Load known faces and their corresponding names
known_face_encodings = []
known_face_names = []


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# Load the known face image (replace with the path to your known face image)
image1 = "nilesh.jpg"
known_image = face_recognition.load_image_file(image1)
known_encoding = face_recognition.face_encodings(known_image)[0]
known_face_encodings.append(known_encoding)
known_face_names.append("Nilesh Pathak")

# Open the video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Capture each frame from the camera
    ret, frame = video_capture.read()

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the detected face matches the known face
        results = face_recognition.compare_faces([known_encoding], face_encoding)
        name = "Unknown"
        if True in results:
            speak("Face detected. This is Nilesh Pathak who created the program")
            first_match_index = results.index(True)
            name = known_face_names[first_match_index]
        else:
            speak("Unknown Face detected.")

        # Draw a rectangle around the face and display the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 100, 50), 1)

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Check for user command to close the program
    if sd.query_devices()[0]['default_samplerate']:
        data = sd.rec(int(5 * 44100), samplerate=44100, channels=2, dtype=np.int16)
        sd.wait()
        if np.max(data) > 3000:  # Adjust this threshold as needed
            print("Please close the program.")
            speak("Please close the program.")
            break

    if cv2.waitKey(1) & 0xFF == ord('n'):
        break

video_capture.release()
cv2.destroyAllWindows()
