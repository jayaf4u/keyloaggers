import time
import os
from PIL import ImageGrab
from datetime import datetime

# Create a folder to save screenshots
screenshot_folder = "screenshots"
os.makedirs(screenshot_folder, exist_ok=True)

def take_screenshot():
    """Captures and saves a screenshot with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(screenshot_folder, f"screenshot_{timestamp}.png")
    screenshot = ImageGrab.grab()
    screenshot.save(file_path)
    print(f"[+] Screenshot saved: {file_path}")

def start_screenshot_capture(interval=30):
    """Continuously takes screenshots every 'interval' seconds."""
    try:
        print(f"[+] Starting screenshot capture every {interval} seconds. Press Ctrl+C to stop.")
        while True:
            take_screenshot()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[!] Screenshot capture stopped by user.")

if __name__ == "__main__":
    start_screenshot_capture(interval=30)
