import pygame
import threading
from pynput import keyboard

# Initialize pygame mixer for sound playback
pygame.mixer.init()

# Path to your sound file (e.g., "sound.wav" or "beep.mp3")
SOUND_FILE = "sounds/mech.mp3"  # as an option, use "sounds/CLICK.WAV
SOUND_FILE2 = "sounds/return1.mp3"
print("Initializing sound system...")
print(f"Using sound file: {SOUND_FILE}")
print(f"Press any key to play the sound. Press 'Esc' to exit.")
print(f"-------------------------------------------------------")
print("Listening for key presses...")  # Corrected

# Load the sound
try:
    sound = pygame.mixer.Sound(SOUND_FILE)
    sound2 = pygame.mixer.Sound(SOUND_FILE2)
except pygame.error as e:
    print(f"Error loading sound file: {e}")
    print("Please ensure the sound file path is correct and the file exists.")
    exit()

def play_sound_async():
    """Plays the sound in a separate thread to avoid blocking."""
    sound.play()

def on_press(key):
    """Callback function for key press events."""
    if key == keyboard.Key.enter:
        sound2.play()  # Play a different sound on Enter key
        
    try:
        # Start a new thread to play the sound asynchronously
        threading.Thread(target=play_sound_async).start()
    except AttributeError:
        if key in [keyboard.Key.shift]: # Handle special keys (e.g., Key.space, Key.enter)
        # Special key pressed, optionally handle here
         print(f"Excluding key: {key}")
         return False

def on_release(key):
    """Callback function for key release events (optional)."""
    if key == keyboard.Key.esc:
        # Stop listener if 'esc' is pressed
        return False

# Set up the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()