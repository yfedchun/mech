import pygame
import threading
from pynput import keyboard

# Initialize pygame mixer for sound playback
pygame.mixer.init()

# Path to your sound file (e.g., "sound.wav" or "beep.mp3")
SOUND_FILE = "sounds/CLICK.WAV"
print("Initializing sound system...")
print(f"Using sound file: {SOUND_FILE}")
print(f"Press any key to play the sound. Press 'Esc' to exit.")
print(f"-------------------------------------------------------")
print("Listening for key presses...")  # Corrected

# Load the sound
try:
    sound = pygame.mixer.Sound(SOUND_FILE)
except pygame.error as e:
    print(f"Error loading sound file: {e}")
    print("Please ensure the sound file path is correct and the file exists.")
    exit()

def play_sound_async():
    """Plays the sound in a separate thread to avoid blocking."""
    sound.play()

def on_press(key):
    """Callback function for key press events."""
    try:
        # Exclude function buttons and special keys
        if key in [keyboard.Key.shift, keyboard.Key.fn, keyboard.Key.ctrl,
                   keyboard.Key.alt, keyboard.Key.cmd, keyboard.Key.left,
                   keyboard.Key.right, keyboard.Key.up, keyboard.Key.down]:
            print(f"Excluding key: {key}")
            return

        # Start a new thread to play the sound asynchronously
        threading.Thread(target=play_sound_async).start()
    except AttributeError:
        # Handle special keys (e.g., Key.space, Key.enter)
        pass

    # Check for Ctrl+~ combination
    if key == keyboard.Key.ctrl and '~' in [k.char for k in keyboard.Controller().pressed_keys]:
        return False

def on_release(key):
    """Callback function for key release events (optional)."""
    if key == keyboard.Key.esc:
        # Stop listener if 'esc' is pressed
        return False

# Set up the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()