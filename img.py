import cv2
import os
import time
from datetime import datetime

# Folder to store captured images
output_folder = "captured_images"
os.makedirs(output_folder, exist_ok=True)

def capture_image():
    """Captures a single image from the default webcam."""
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
        filepath = os.path.join(output_folder, filename)
        cv2.imwrite(filepath, frame)
        print(f"[+] Captured image: {filepath}")
        cap.release()
        return filepath
    else:
        cap.release()
        print("[!] Failed to capture image.")
        return None

def main_loop(interval=20):
    """Main loop to capture and save images every `interval` seconds."""
    print(f"[+] Starting webcam capture every {interval} seconds. Press Ctrl+C to stop.")
    try:
        while True:
            capture_image()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")

if __name__ == "__main__":
    main_loop(interval=20)
