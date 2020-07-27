import audioop
import pyaudio as pa
import wave

class speech():
    def __init__(self):
        # soundtrack properties
        self.format = pa.paInt16         # 16 bits per sample
        self.rate = 16000                # Record at 16000 samples per second
        self.channel = 1
        self.chunk = 1024                # Record in chunks of 1024 samples
        self.threshold = 100
        self.file = 'audio.wav'

        # intialise microphone stream
        self.audio = pa.PyAudio()        # Create an interface to PortAudio
        self.stream = self.audio.open(format=self.format,
                                  channels=self.channel,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk)


    def record(self):
        while True:
            data = self.stream.read(self.chunk)
            rms = audioop.rms(data,2)                 #get input volume
            if rms>self.threshold:                    #if input volume greater than threshold
                break

        frames = []                                        # array to store frames
        # record upto silence only
        while rms>self.threshold:
            data = self.stream.read(self.chunk)
            print(type(self.chunk))
            print(self.chunk)
            rms = audioop.rms(data,2)
            frames.append(data)

        print('finished recording.... writing file....')
        write_frames = wave.open(self.file, 'wb')
        write_frames.setnchannels(self.channel)
        write_frames.setsampwidth(self.audio.get_sample_size(self.format))
        write_frames.setframerate(self.rate)
        write_frames.writeframes(b''.join(frames))
        write_frames.close()


p1=speech()
print("Recording is started...")
p1.record()
print('recoding is done')
