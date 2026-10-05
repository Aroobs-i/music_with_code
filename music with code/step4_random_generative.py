"""
STEP 4: Generative melody (code "composes" for you)
------------------------------------------------------
Instead of writing notes by hand, pick them randomly from a musical
scale so they always sound "in key" even though it's random.
This is the gateway to algorithmic composition.
"""
import numpy as np
from scipy.io import wavfile
import random

sample_rate = 44100

def note_freq(semitones_from_a4):
    """Any note's frequency, counting half-steps away from A4 (440Hz)."""
    return 440.0 * (2 ** (semitones_from_a4 / 12))

# C major scale, built from semitone offsets relative to A4
# (C4, D4, E4, F4, G4, A4, B4, C5)
major_scale_offsets = [-9, -7, -5, -4, -2, 0, 2, 3]
scale = [note_freq(s) for s in major_scale_offsets]

def tone(freq, duration, sample_rate=44100, volume=0.4):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = volume * np.sin(2 * np.pi * freq * t)
    fade = int(0.01 * sample_rate)
    wave[:fade] *= np.linspace(0, 1, fade)
    wave[-fade:] *= np.linspace(1, 0, fade)
    return wave

random.seed(10)          # change or remove this to get a different tune each run
num_notes = 24
durations = [0.2, 0.3, 0.4]

melody = []
for _ in range(num_notes):
    freq = random.choice(scale)
    dur = random.choice(durations)
    melody.append(tone(freq, dur))

audio = np.concatenate(melody)
wavfile.write("step4_generative.wav", sample_rate, (audio * 32767).astype(np.int16))

print("Saved step4_generative.wav — a randomly generated melody in C major")
print("Tip: change random.seed(7) to any number to get a different tune")