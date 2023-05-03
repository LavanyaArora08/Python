import os
import face_recognition
from gtts import gTTS
from datetime import datetime
import cv2
import pygame
import argparse

def capture_photo(filename):
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera is open
    if not cap.isOpened():
        print("Could not open camera")
        return

    # Capture a frame from the camera
    ret, frame = cap.read()

    # Save the frame to a file
    cv2.imwrite(filename, frame)

    # Release the camera
    cap.release()

def play_audio(filename):
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the audio file
    audio = pygame.mixer.Sound(filename)

    # Play the audio file
    audio.play()

    # Wait for the audio to finish playing
    while pygame.mixer.get_busy():
        continue

    # Clean up Pygame mixer
    pygame.mixer.quit()

# Get user information
name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")

# Create a directory for the user if it doesn't exist
user_dir = f"user/{name}"
if not os.path.exists(user_dir):
    os.makedirs(user_dir)

# Access camera and take a picture
photo_filename = f"{user_dir}/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
print("Taking photo...")
capture_photo(photo_filename)
# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add an argument to specify the directory containing known face images
parser.add_argument('--known-dir', type=str, required=True, help='Path to directory containing known face images')

# Parse the command line arguments
args = parser.parse_args()

# Access the specified directory using the 'known_dir' attribute of the 'args' object
known_dir = args.known_dir

# Load the known face encodings
known_dir = "known"
known_face_encodings = []
known_face_names = []
for filename in os.listdir(known_dir):
    image = face_recognition.load_image_file(f"{known_dir}/{filename}")
    encoding = face_recognition.face_encodings(image)[0]
    name = os.path.splitext(filename)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(name)

# Load the user's face encoding
image = face_recognition.load_image_file(photo_filename)
user_face_encoding = face_recognition.face_encodings(image)[0]

# Compare the user's face encoding to the known face encodings
matches = face_recognition.compare_faces(known_face_encodings, user_face_encoding)

# Find the index of the matched face
matched_index = None
for i, match in enumerate(matches):
    if match:
        matched_index = i
        break

# Say the name of the matched person using Google text-to-speech and Pygame mixer
if matched_index is not None:
    matched_name = known_face_names[matched_index]
    tts = gTTS(f"Hello {matched_name}")
    tts.save("match.mp3")
    play_audio("match.mp3")
else:
    print("No match found.")
