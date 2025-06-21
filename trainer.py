import cv2
import numpy as np
from PIL import Image
import os

# Dataset path
dataset_path = 'dataset'

# Create face recognizer and cascade
recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []

    for image_path in image_paths:
        try:
            # Load image and convert to grayscale
            pil_img = Image.open(image_path).convert('L')
            img_numpy = np.array(pil_img, 'uint8')

            # Extract user ID from filename like User.10.1.jpg
            filename = os.path.split(image_path)[-1]

            if not filename.startswith("User"):
                continue  # Skip unrelated files like desktop.ini

            try:
                id = int(filename.split('.')[1])
            except:
                continue  # Skip if ID is not a valid number

            # Detect faces in the image
            faces = face_cascade.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                face_samples.append(img_numpy[y:y+h, x:x+w])
                ids.append(id)
        except:
            continue

    return face_samples, ids

# Get faces and IDs
print("[INFO] Training faces. Please wait...")
faces, ids = get_images_and_labels(dataset_path)

# Train and save
recognizer.train(faces, np.array(ids))
recognizer.save('trainer.yml')
print(f"[INFO] {len(np.unique(ids))} faces trained. Model saved as 'trainer.yml'")