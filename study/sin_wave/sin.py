import wave
import struct
import numpy as np

fs = 8000
A = 1
f0 = 440
sec = 3

swav = []
for n in np.arange(fs * sec):
  s = A * np.sin(2. * np.pi * f0 * n / fs)
  swav.append(s)

swav = [int(x * 32767.0) for x in swav]

bin_out = struct.pack("h" * len(swav), *swav)

w = wave.Wave_write("sin.wav")
params = (1, 2, 8000, len(bin_out), 'NONE', 'not compressed')
w.setparams(params)
w.writeframes(bin_out)
w.close()
