"""
STEP 2: Play a melody
----------------------
A melody is just a list of notes played one after another.
"""
import numpy as np
from scipy.io import wavfile

sample_rate = 44100

# Note frequencies (Hz) including all required notes for Interstellar
NOTES = {
    "A4": 440.00,
    "B4": 493.88,
    "C5": 523.25,
    "D5": 587.33,
    "E5": 659.25
}

def tone(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * freq * t)
    # fade in/out slightly so notes don't "click"
    fade = int(0.01 * sample_rate)
    wave[:fade] *= np.linspace(0, 1, fade)
    wave[-fade:] *= np.linspace(1, 0, fade)
    return wave

# Interstellar Main Theme (First Step) Motif
# Format: (note, duration in seconds)
melody = [
    ("A4", 0.4), ("E5", 0.4), ("A4", 0.4), ("E5", 0.4),  # First phrase
    ("B4", 0.4), ("E5", 0.4), ("B4", 0.4), ("E5", 0.4),  # Second phrase
    ("C5", 0.4), ("E5", 0.4), ("C5", 0.4), ("E5", 0.4),  # Third phrase
    ("D5", 0.4), ("E5", 0.4), ("D5", 0.4), ("B4", 0.6)   # Resolution
]

audio = np.concatenate([tone(NOTES[note], dur) for note, dur in melody])
wavfile.write("interstellar.wav", sample_rate, (audio * 32767).astype(np.int16))

print("Saved interstellar.wav — Interstellar Motif")
