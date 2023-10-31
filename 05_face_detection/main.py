# Task-5 FACE DETECTION AND RECOGNITION

import datetime
import tkinter as tk
from tkinter import filedialog
import cv2
import os

debug = True

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# create folder for output images
os.makedirs("output/cam_images", exist_ok=True)
os.makedirs("output/photo_images", exist_ok=True)
os.makedirs("output/vid_images", exist_ok=True)
os.makedirs("output/video", exist_ok=True)

# -------------------------from_camera-----------------------
def detect_faces_from_camera():
    cap = cv2.VideoCapture(0)
    capture_flag = False

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            if capture_flag:
                face = frame[y:y + h, x:x + w]
                cv2.imwrite(os.path.join(
                    "output/cam_images", f"captured_face_{len(os.listdir('output/cam_images')) + 1}.jpg"), face)
                capture_flag = False
        
        cv2.imshow('Face Detection from Camera', frame)

        key = cv2.waitKey(1)

        if key & 0xFF == ord('q'):
            print('Camera closed by user')
            break
        elif key & 0xFF == ord('c'):
            print('Camera caputred the image')
            capture_flag = True

    cap.release()
    cv2.destroyAllWindows()

    if debug:
        print("Camera capture completed")

# ------------------------------------capture_face_from_images---------------------------------------
def detect_face_from_image():

    file_path = filedialog.askopenfilename()

    if file_path:
        image = cv2.imread(file_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

            face = image[y:y + h, x:x + w]
            cv2.imwrite(os.path.join("output/photo_images",
                        f"captured_face_{len(os.listdir('output/photo_images')) + 1}.jpg"), face)

        cv2.imshow('Face Detection from Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if debug:
        print("Image capture completed")

# -----------------------------detect_face_from_video-----------------------------------------------------
def detect_face_from_video():
    file_path = filedialog.askopenfilename()

    if not file_path:
        return

    cap = cv2.VideoCapture(file_path)

    # define the codec and create a VideoWriter object to save the output video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_file = os.path.join(
        "output/video", f"output_video_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.avi")
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    if debug:
        print("Video capture started")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            face = frame[y:y + h, x:x + w]
            cv2.imwrite(os.path.join("output/vid_images",
                        f"captured_face_{len(os.listdir('output/vid_images')) + 1}.jpg"), face)

        out.write(frame)

        cv2.imshow('Face Detection from Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    if debug:
        print("Video capture completed")

# -------------------------------------------Dashboard------------------------------------------------------------
def main():
    root = tk.Tk()
    root.title("Face Detection Dashboard")

    button_height = 2
    button_width = 15

    root.geometry("300x300")

    label1 = tk.Label(root, text="WELCOME!",
                      font=("Helvetica", 16), fg='green')
    label1.pack(pady=20)

    camera_button = tk.Button(
        root, text="Open Camera", command=detect_faces_from_camera, width=button_width, height=button_height)
    camera_button.pack(pady=10)

    image_button = tk.Button(
        root, text="Upload Image", command=detect_face_from_image, width=button_width, height=button_height)
    image_button.pack(pady=10)

    video_button = tk.Button(root, text="Upload Video",
                             command=detect_face_from_video, width=button_width, height=button_height)
    video_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
