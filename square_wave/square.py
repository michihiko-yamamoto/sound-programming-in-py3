import wave
import struct
import numpy as np
from matplotlib import pylab as plt

def square_wave(m, num, fs):
  amp = 0.5
  f0 = 250.0
  s = 0.
  for i in np.arange(m):
    k = float(2 * (i + 1) - 1)
    x = np.sin((4.0 * np.pi * f0 * k * float(num)) / fs ) 
    s += amp * x / k
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
square = fourier(frqs, 100, sec)

# plot
plt.plot(square[0:100])
plt.show()

# output wav file
output_wav(square, "square.wav")
