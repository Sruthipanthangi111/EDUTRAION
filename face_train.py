import cv2
import os

cam = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_id = input('\nEnter user ID and press <Enter>: ')
print("[INFO] Initializing face capture... Look at the camera.")

count = 0
os.makedirs('dataset', exist_ok=True)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        count += 1
        cv2.imwrite(f"dataset/User.{face_id}.{count}.jpg", gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff
    if k == 27 or count >= 30:  # ESC key or 30 samples
        break

print("[INFO] Exiting and saving data...")
cam.release()
cv2.destroyAllWindows() 