import numpy as np
import cv2
import pyaudio
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

class Che5848Encoder:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.video_out = cv2.VideoWriter('output.avi', self.fourcc, 30, (self.width, self.height))

    def bytes_to_frequency_visual(self, byte_data):
        # Create a visual representation of byte_data
        visual = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        for i, byte in enumerate(byte_data):
            x = (i % (self.width // 10)) * 10
            y = (i // (self.width // 10)) * 10
            byte_value = byte % 256
            color = hsv_to_rgb(np.array([byte_value / 256, 1, 1])) * 255
            cv2.rectangle(visual, (x, y), (x + 10, y + 10), color.astype(int).tolist(), -1)
        return visual

    def create_audio(self, byte_data):
        # Generate audio data modulated by byte values
        audio_stream = np.zeros(44100)
        for i, byte in enumerate(byte_data):
            frequency = 440 + (byte % 256)  # Base frequency + modulation
            t = np.linspace(i / 44100, (i + 1) / 44100, 44100, False)
            audio_stream[i] = 0.5 * np.sin(2 * np.pi * frequency * t)
        return audio_stream

    def encode(self, file_path):
        with open(file_path, 'rb') as f:
            byte_data = f.read()
        visual = self.bytes_to_frequency_visual(byte_data)
        audio_data = self.create_audio(byte_data)

        for frame in range(0, len(byte_data), 10):
            visual_frame = visual[frame:frame+10]  # Slice visual for animation
            self.video_out.write(visual_frame)

        self.video_out.release()

if __name__ == '__main__':
    encoder = Che5848Encoder()
    encoder.encode('sample_file.bin')