import cv2
import os
from datetime import datetime

def save_intruder_img(frame):
    if not os.path.exists('intruders'):
        os.makedirs('intruders')
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"intruders/intruder_{timestamp}.jpg"
    cv2.imwrite(file_path, frame)
    print(f"Alert: Intruder image saved at {file_path}")
    return file_path
