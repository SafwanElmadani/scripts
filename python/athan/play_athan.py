import pygame
import sys

# Check if an argument was provided
if len(sys.argv) < 2:
    print("Usage: python script.py <audio_file>")
    sys.exit(1)

audio_file = sys.argv[1]  # Get the file from command-line arguments

# Initialize pygame mixer
pygame.mixer.init()

# Load and play the audio file
try:
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Keep the program running while the audio is playing
    while pygame.mixer.music.get_busy():
        pass

except pygame.error as e:
    print(f"Error loading audio file: {e}")
    sys.exit(1)

