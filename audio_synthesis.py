import numpy as np
import scipy.io.wavfile as wav
import librosa

# Convert byte sequences to audio frequencies
# 0-255 maps to 50Hz-20kHz
def bytes_to_frequencies(data):
    frequencies = np.interp(data, [0, 255], [50, 20000])
    return frequencies

# Generate sine wave audio at specified frequency
def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    sine_wave = np.sin(2 * np.pi * frequency * t)
    return sine_wave

# Generate square wave audio
def generate_square_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    square_wave = np.sign(np.sin(2 * np.pi * frequency * t))
    return square_wave

# Create audio by modulating through byte-based frequencies
def modulate_audio(frequencies, sample_rate):
    audio = np.zeros(int(sample_rate * len(frequencies) / sample_rate))
    for i, freq in enumerate(frequencies):
        audio[i:i+sample_rate] += generate_sine_wave(freq, 1, sample_rate)
    return audio

# Save numpy audio array to WAV/MP3 file using scipy/librosa
# Ensure you install librosa if saving as MP3
def save_audio(audio_data, output_file, sample_rate):
    # Normalize to 16-bit range
    audio_data = np.int16(audio_data/np.max(np.abs(audio_data)) * 32767)
    wav.write(output_file, sample_rate, audio_data)
    # For MP3, uncomment below:
    # if output_file.endswith('.mp3'):
    #    librosa.output.write_wav(output_file, audio_data, sample_rate)

# Apply ADSR envelope to audio
def apply_envelope(audio_data, attack, decay, sustain, release):
    total_length = len(audio_data)
    attack_length = int(attack * total_length)
    decay_length = int(decay * total_length)
    sustain_length = int(sustain * total_length)
    release_length = int(release * total_length)

    envelope = np.ones(total_length)
    envelope[:attack_length] *= np.linspace(0, 1, attack_length)
    envelope[attack_length:attack_length + decay_length] *= np.linspace(1, sustain, decay_length)
    envelope[attack_length + decay_length:attack_length + decay_length + sustain_length] *= sustain
    envelope[-release_length:] *= np.linspace(sustain, 0, release_length)

    return audio_data * envelope
