import queue
import pyflac
import soundfile as sf

class FlacAudioStream:

    def __init__(self):
        self.output = None
        self.queue = queue.SimpleQueue()
        self.decoder = pyflac.StreamDecoder(callback=self.callback)

    def process(self):
        while not self.queue.empty():
            self.decoder.process(self.queue.get())

    def callback(self, data, sample_rate, num_channels, num_samples):
        if self.output is None:
            self.output = sf.SoundFile(
                'output.wav', mode='w', channels=num_channels,
                samplerate=sample_rate
            )
        self.output.write(data)

audio = FlacAudioStream()
audio.decoder.process()