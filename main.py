import cv2
import face_recognition
import os
import numpy as np
from ultralytics import YOLO
from utils.tracker import save_intruder_img

# 1. Load Known Faces (Aapka chehra)
known_face_encodings = []
known_face_names = []

# 'known_faces' folder se images load karein
for image_name in os.listdir('known_faces'):
    image = face_recognition.load_image_file(f"known_faces/{image_name}")
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(image_name.split(".")[0])

# 2. Load YOLO Model (Person Detection ke liye)
model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # YOLO se person detect karein
    results = model(frame, verbose=False)
    
    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:  # Class 0 is 'person'
                
                # 3. Face Recognition Logic
                # Frame se faces dhundhein
                face_locations = face_recognition.face_locations(frame)
                face_encodings = face_recognition.face_encodings(frame, face_locations)

                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]
                    
                    # 4. Screenshot Logic (Agar unknown hai toh)
                    if name == "Unknown":
                        save_intruder_img(frame)
                        cv2.putText(frame, "ALERT: INTRUDER", (50, 50), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    else:
                        cv2.putText(frame, f"Welcome {name}", (50, 50), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Security Feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
