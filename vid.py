import cv2
import os
import time
from datetime import datetime

# Folder to store captured videos
output_folder = "captured_videos"
os.makedirs(output_folder, exist_ok=True)

# Video settings
video_duration = 20  # seconds
fps = 20.0           # frames per second
frame_size = (640, 480)  # Default resolution (can change to 1280x720)

def record_video(duration=20):
    """Records video from webcam for the given duration (in seconds)."""
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_size[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_size[1])

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Use 'XVID' for .avi or 'mp4v' for .mp4
    filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.avi"
    filepath = os.path.join(output_folder, filename)
    out = cv2.VideoWriter(filepath, fourcc, fps, frame_size)

    print(f"[+] Recording video: {filepath}")
    start_time = time.time()

    while int(time.time() - start_time) < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            print("[!] Failed to read frame from webcam.")
            break

    cap.release()
    out.release()
    print(f"[+] Saved video: {filepath}")

def main_loop(interval=20):
    """Continuously records video clips every `interval` seconds."""
    print(f"[+] Starting webcam video capture in {interval}-second clips. Press Ctrl+C to stop.")
    try:
        while True:
            record_video(duration=interval)
            # Optional: add a break or pause if needed between recordings
    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")

if __name__ == "__main__":
    main_loop(interval=20)
