import wave
import struct
import numpy as np
from matplotlib import pylab as plt
import random

def output_wav(sound, fileName):
  bin_out = struct.pack("h" * len(sound), *sound)

  w = wave.Wave_write(fileName)
  params = (1, 2, 8000, len(bin_out), 'NONE', 'not compressed')
  w.setparams(params)
  w.writeframes(bin_out)
  w.close()

def noise(amp, fs, sec):
  noise = []
  amp = int(amp)
  for n in range(int(fs * sec)):
    noise.append(random.randint(-amp,amp))
  return noise

frqs = 8000.0
sec = 3.0
amp = 10000
noised = noise(amp, frqs, sec)

# plot
# plt.plot(noised)
# plt.show()

# output wav file
output_wav(noised, "noise.wav")
