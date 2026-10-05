"""
STEP 2: Play a melody
----------------------
A melody is just a list of notes played one after another.
Game of Thrones Main Theme — Extended to over 25 seconds.
"""
import numpy as np
from scipy.io import wavfile

sample_rate = 44100

# Note frequencies (Hz) for the Game of Thrones Theme (Extended for higher octaves)
NOTES = {
    "G3": 196.00,
    "A#3": 233.08,
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
    "G5": 783.99,
    "A#5": 932.33,
    "C6": 1046.50
}

def tone(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * freq * t)
    # fade in/out slightly so notes don't "click"
    fade = int(0.01 * sample_rate)
    wave[:fade] *= np.linspace(0, 1, fade)
    wave[-fade:] *= np.linspace(1, 0, fade)
    return wave

# --- SECTION 1: THE EXTENDED INTRO (~9.6 seconds) ---
# Running this loop 16 times builds the foundational tension
intro_loop = [("G3", 0.2), ("C4", 0.2), ("D#4", 0.1), ("F4", 0.1)] * 16

# --- SECTION 2: THE MAIN MELODY (~8.4 seconds) ---
main_theme = [
    ("G4", 0.8), ("C4", 0.8),               # Dunnn... dunnn...
    ("D#4", 0.2), ("F4", 0.2), ("G4", 0.6), # da-da-dunnn...
    ("C4", 0.6), ("D#4", 0.2), ("F4", 0.2), # dunnn... da-da...
    ("D4", 1.2),                             # dunnn...
    
    ("F4", 0.8), ("A#3", 0.8),              # Dunnn... dunnn...
    ("D#4", 0.2), ("D4", 0.2), ("F4", 0.6), # da-da-dunnn...
    ("A#3", 0.6), ("D#4", 0.2), ("D4", 0.2), # dunnn... da-da...
    ("C4", 1.2)                              # dunnn...
]

# --- SECTION 3: THE HIGH OCTAVE CLIMAX (~8.4 seconds) ---
# Playing the theme an octave higher makes it feel like the full orchestra joined in
climax_theme = [
    ("G5", 0.8), ("C5", 0.8),               
    ("D#5", 0.2), ("F5", 0.2), ("G5", 0.6), 
    ("C5", 0.6), ("D#5", 0.2), ("F5", 0.2), 
    ("D5", 1.2),                             
    
    ("F5", 0.8), ("A#4", 0.8),              
    ("D#5", 0.2), ("D5", 0.2), ("F5", 0.6), 
    ("A#4", 0.6), ("D#5", 0.2), ("D5", 0.2), 
    ("C5", 1.2)                              
]

# Combine everything sequentially to pass the 25-second mark (~26.4 seconds total)
melody = intro_loop + main_theme + climax_theme

audio = np.concatenate([tone(NOTES[note], dur) for note, dur in melody])
wavfile.write("gameofthrones.wav", sample_rate, (audio * 32767).astype(np.int16))

print("Saved gameofthrones.wav — Extended Game of Thrones Theme (26+ seconds)!")
