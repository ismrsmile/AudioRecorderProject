import sounddevice as sd
from scipy.io.wavfile import write

freq = 44100
duration = 5

print("You have 5 seconds to start talking.")
recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=2)
sd.wait()
print("You can shut up.")

write("recording0.wav", freq, recording)
