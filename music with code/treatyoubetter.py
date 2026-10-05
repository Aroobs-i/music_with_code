"""
STEP 2: Play a melody
----------------------
A melody is just a list of notes played one after another.
Now extended to include the build-up leading into the chorus.
"""
import numpy as np
from scipy.io import wavfile

sample_rate = 44100

# Expanded Note frequencies (Hz) to cover the lower verse notes
NOTES = {
    "C4": 261.63,
    "D4": 293.66,
    "D#4": 311.13,
    "F4": 349.23,
    "G4": 392.00,
    "G#4": 415.30,
    "A#4": 466.16,
    "C5": 523.25,
    "D5": 587.33,
    "D#5": 622.25,
    "F5": 698.46,
    "G5": 783.99
}

def tone(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * freq * t)
    # fade in/out slightly so notes don't "click"
    fade = int(0.01 * sample_rate)
    wave[:fade] *= np.linspace(0, 1, fade)
    wave[-fade:] *= np.linspace(1, 0, fade)
    return wave

# --- SECTION 1: VERSE ("I won't lie to you, I know he's just not right for you...") ---
verse = [
    ("G4", 0.25), ("G4", 0.25), ("G4", 0.25), ("F4", 0.25), ("G4", 0.4), # "I won't lie to you"
    ("G4", 0.25), ("G4", 0.25), ("G4", 0.25), ("F4", 0.25), ("G4", 0.4), # "I know he's just not"
    ("F4", 0.25), ("D#4", 0.6),                                         # "right for you"
    
    ("G4", 0.25), ("G4", 0.25), ("G4", 0.25), ("F4", 0.25), ("G4", 0.4), # "And you can tell me if"
    ("G4", 0.25), ("G4", 0.25), ("G4", 0.25), ("F4", 0.25), ("G4", 0.4), # "I'm off but I see it on"
    ("F4", 0.25), ("D#4", 0.6),                                         # "your face"
]

# --- SECTION 2: PRE-CHORUS BUILD-UP ("Cause I know that you're standard...") ---
pre_chorus = [
    ("A#4", 0.3), ("A#4", 0.3), ("A#4", 0.3), ("A#4", 0.3), ("C5", 0.3), # "Cause I know that you're"
    ("A#4", 0.3), ("G4", 0.6),                                           # "stan-dard"
    ("A#4", 0.3), ("A#4", 0.3), ("A#4", 0.3), ("A#4", 0.3), ("C5", 0.3), # "Is way too high for us"
    ("A#4", 0.3), ("G4", 0.6),                                           # "to waste"
    
    ("A#4", 0.3), ("A#4", 0.3), ("A#4", 0.3), ("C5", 0.3),               # "Any more time"
    ("D5", 0.3), ("D5", 0.3), ("D5", 0.3), ("D#5", 0.4),                 # "on somebody who"
    ("F5", 0.3), ("G5", 0.8),                                            # "dis-likes..." (holding for the drop!)
]

# --- SECTION 3: THE BEST PART / CHORUS ("I know I can treat you better...") ---
chorus = [
    ("G5", 0.3), ("F5", 0.3), ("D#5", 0.3), ("F5", 0.3), ("G5", 0.4),    # "I know I can treat you"
    ("F5", 0.3), ("D#5", 0.6),                                           # "bet-ter"
    ("F5", 0.3), ("D#5", 0.3), ("F5", 0.3), ("G5", 0.4),                 # "than he can can"
    ("F5", 0.3), ("D#5", 0.6),                                           # "and a..."
    ("G5", 0.3), ("F5", 0.3), ("D#5", 0.3), ("F5", 0.3), ("G5", 0.4),    # "girl like you de-serves a"
    ("F5", 0.3), ("D#5", 0.4), ("D#5", 0.3), ("C5", 0.6)                 # "gen-tle-man"
]

# Combine all the parts together sequentially
melody = verse + pre_chorus + chorus

audio = np.concatenate([tone(NOTES[note], dur) for note, dur in melody])
wavfile.write("treatyoubetter.wav", sample_rate, (audio * 32767).astype(np.int16))

print("Saved treatyoubetter.wav — Full build-up to Chorus!")
