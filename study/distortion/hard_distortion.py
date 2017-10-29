import wave
import struct
import numpy as np
from matplotlib import pylab as plt

def input_wav(filePath):
  wr = wave.open(filePath, "r")
  buf = wr.readframes(wr.getnframes())
  fs = wr.getframerate()
  wr.close()
  data = data = np.frombuffer(buf, dtype='int16')
  return data, fs

def output_wav(sound, fs, fileName):
  bin_out = struct.pack("h" * len(sound), *sound)

  w = wave.Wave_write(fileName)
  params = (1, 2, fs, len(bin_out), 'NONE', 'not compressed')
  w.setparams(params)
  w.writeframes(bin_out)
  w.close()

source, fs = input_wav('guitar_D5.wav')

gain = 100.0
level = 0.5
lim = 30000

# hard distortion
distorted = []
for n in range(int(len(source))):
  s = source[n] * 100
  if s > lim:
    s = lim
  elif s < -lim:
    s = -lim
  distorted.append(int(s * level))

# plot
# plt.plot(source)
# plt.plot(distorted)
# plt.show()

# output wav file
output_wav(distorted, fs, "hard_distortion.wav")
