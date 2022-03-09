import queue
import pyflac
import sounddevice as sd


class FlacAudioStream:
    def __init__(self):
        self.stream = sd.InputStream(dtype='int16', callback=self.audio_callback)
        self.encoder = pyflac.FileEncoder(write_callback=self.encoder_callback, sample_rate=5)
        self.queue = queue.SimpleQueue()

    def audio_callback(self, indata, frames, sd_time, status):
        self.encoder.process(indata)

    def encoder_callback(self, buffer, num_bytes, num_samples, current_frame):
        self.queue.put(buffer)

audio = FlacAudioStream()
audio.stream.start()

def compressor(input_file, output_path):
