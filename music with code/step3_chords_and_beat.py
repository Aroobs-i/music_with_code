"""
STEP 3: Chords + a simple drum beat
-------------------------------------
- A chord = multiple notes played AT THE SAME TIME (add the waves together).
- A drum hit = a short burst of noise or a low thump, not a pitched tone.
We'll layer a chord progression with a kick-drum pulse underneath.
"""
import numpy as np
from scipy.io import wavfile

sample_rate = 44100

NOTES = {
    "C3": 130.81, "E3": 164.81, "G3": 196.00,
    "A3": 220.00, "F3": 174.61,
    "C4": 261.63, "D4": 293.66, "E4": 329.63, "G4": 392.00, "A4": 440.00,
}

def tone(freq, duration, sample_rate=44100, volume=0.3):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = volume * np.sin(2 * np.pi * freq * t)
    fade = int(0.01 * sample_rate)
    wave[:fade] *= np.linspace(0, 1, fade)
    wave[-fade:] *= np.linspace(1, 0, fade)
    return wave

def chord(freqs, duration, sample_rate=44100):
    waves = [tone(f, duration, sample_rate) for f in freqs]
    mixed = np.sum(waves, axis=0)
    return mixed / len(waves)   # average so it doesn't clip

def kick(duration=0.15, sample_rate=44100):
    """A simple kick drum: a sine wave that drops in pitch fast."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    freq_sweep = 150 * np.exp(-15 * t)          # pitch falls from 150Hz down
    wave = 0.8 * np.sin(2 * np.pi * freq_sweep * t)
    wave *= np.exp(-8 * t)                       # volume fades out fast
    return wave

def silence(duration, sample_rate=44100):
    return np.zeros(int(sample_rate * duration))

# Chord progression: C - Am - F - G, one bar each (1.6s)
bar = 1.6
progression = [
    ["C3", "E3", "G4"],
    ["A3", "C4", "E4"],
    ["F3", "A3", "C4"],
    ["G3", "D4", "G4"],
]

chords_track = np.concatenate([
    chord([NOTES[n] for n in ch], bar) for ch in progression
])

# Drum track: kick on beat 1 and 3 of each bar (4 beats per bar, 0.4s each)
beat = bar / 4
drum_track = []
for _ in progression:
    for b in range(4):
        if b in (0, 2):
            k = kick(duration=beat)
            drum_track.append(k)
        else:
            drum_track.append(silence(beat))
drum_track = np.concatenate(drum_track)

# Mix the two tracks together (pad to equal length just in case)
length = min(len(chords_track), len(drum_track))
mix = chords_track[:length] * 0.6 + drum_track[:length] * 0.6

# Normalize to avoid clipping
mix = mix / np.max(np.abs(mix))
wavfile.write("step3_chords_beat.wav", sample_rate, (mix * 32767).astype(np.int16))

print("Saved step3_chords_beat.wav — chord progression + kick drum")