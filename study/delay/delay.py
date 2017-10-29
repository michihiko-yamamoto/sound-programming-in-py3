import wave
import struct
import numpy as np
# from matplotlib import pylab as plt

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

# source, fs = input_wav('guitar_D5.wav')
source, fs = input_wav('test.wav')

repeat = 10
a = 0.5
d = float(fs) * 0.5

delayed = []
for n in range(int(len(source) * 1.2)):
  if len(source) > n:
    tmp = source[n]
  else:
    tmp = 0
  for i in range(1, repeat + 1):
    m = int(float(n) - float(i) * d)
    if m >= 0 and m < len(source):
      tmp += int((a ** float(i)) * source[m])
  delayed.append(tmp)

# plot
# plt.plot(source)
# plt.plot(delayed)
# plt.show()

# output wav file
output_wav(delayed, fs, "delay.wav")
