"""
STEP 2: Play a melody
----------------------
A melody is just a list of notes played one after another.
We'll write "Twinkle Twinkle Little Star" as frequencies.
"""
import numpy as np
from scipy.io import wavfile

sample_rate = 44100

# Note frequencies (Hz) — these are standard, you can look up any note
NOTES = {
    "C4": 261.63, "D4": 293.66, "E4": 329.63, "F4": 349.23,
    "G4": 392.00, "A4": 440.00, "B4": 493.88, "C5": 523.25,
}

def tone(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * freq * t)
    # fade in/out slightly so notes don't "click"
    fade = int(0.01 * sample_rate)
    wave[:fade] *= np.linspace(0, 1, fade)
    wave[-fade:] *= np.linspace(1, 0, fade)
    return wave

# "Twinkle Twinkle Little Star" — (note, duration in seconds)
melody = [
    ("C4", 0.4), ("C4", 0.4), ("G4", 0.4), ("G4", 0.4),
    ("A4", 0.4), ("A4", 0.4), ("G4", 0.8),
    ("F4", 0.4), ("F4", 0.4), ("E4", 0.4), ("E4", 0.4),
    ("D4", 0.4), ("D4", 0.4), ("C4", 0.8),
]

audio = np.concatenate([tone(NOTES[note], dur) for note, dur in melody])
wavfile.write("step2_twinkle_star.wav", sample_rate, (audio * 32767).astype(np.int16))

print("Saved step2_twinkle_star.wav — Twinkle Twinkle Little Star")