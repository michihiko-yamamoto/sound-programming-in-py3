import wave
import struct
import numpy as np
from matplotlib import pylab as plt

def square_wave(m, num, fs):
  amp = 0.1
  f0 = 440.0
  s = 0.
  for i in np.arange(m):
    x = np.sin(np.pi * float(i + 1) / 2.) * np.sin((float(i + 1) * f0 * float(num)) / fs ) 
    s += 8.0 * amp * x / float((i + 1) * (i + 1)) 
  return s

def fourier(fs, m, seconds):
  swav = []
  for n in np.arange(int(fs * seconds)):
    swav.append(square_wave(m, n, fs))
  return swav

def output_wav(sound, fileName):
  sound = [int(x * 32767.0) for x in sound]

  bin_out = struct.pack("h" * len(sound), *sound)

  w = wave.Wave_write(fileName)
  params = (1, 2, 8000, len(bin_out), 'NONE', 'not compressed')
  w.setparams(params)
  w.writeframes(bin_out)
  w.close()

frqs = 8000.0
sec = 3.0
tri = fourier(frqs, 100, sec)

# plot
plt.plot(tri[0:100])
plt.show()

# output wav file
output_wav(tri, "triangle.wav")
