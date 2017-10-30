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

def sig_distort(x, r, lim):
  sig = 1.0 / (1.0 + np.exp(-x / (float(lim) * r)))
  return sig * float(lim)

source, fs = input_wav('guitar_D5.wav')

gain = 10.0
level = 0.5
lim = 30000
r = 0.1

# soft distortion
distorted = []
for n in range(int(len(source))):
  s = source[n] * gain
  s = sig_distort(s, r, lim)
  distorted.append(int(s * level))

# plot
# plt.plot(source)
# plt.plot(distorted)
# plt.show()

# output wav file
output_wav(distorted, fs, "soft_distortion.wav")
