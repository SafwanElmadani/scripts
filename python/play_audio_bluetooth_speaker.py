import sounddevice as sd
import soundfile as sf
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <audio_file>")
    sys.exit(1)

file_path = sys.argv[1]  # Get the file path from the command-line argument
device_name = "Bedroom speaker"  # Your target audio device

try:
    # Load audio file
    data, samplerate = sf.read(file_path)

    # Play the audio on the specified device
    sd.play(data, samplerate, device=device_name)
    sd.wait()  # Wait until playback is complete
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

