"""
STEP 1: Play a single note
---------------------------
Sound is just numbers that go up and down very fast (a "wave").
A sine wave at 440 Hz vibrates 440 times per second = musical note A4.
"""
import numpy as np
from scipy.io import wavfile

sample_rate = 44100          # how many numbers per second (CD quality)
duration = 1.0                # seconds
frequency = 440.0             # Hz, this is note A4

# Create a list of time points: 0, 1/44100, 2/44100, ...
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# The actual wave: height = sin(2*pi*freq*time)
wave = np.sin(2 * np.pi * frequency * t)

# Turn the -1..1 numbers into 16-bit audio and save
audio = (wave * 32767).astype(np.int16)
wavfile.write("step1_note.wav", sample_rate, audio)

print("Saved step1_note.wav — a 1 second 'A' note")