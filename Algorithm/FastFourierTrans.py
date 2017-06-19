import matplotlib.pyplot as plt
import numpy as np
import sinClass


test1 = sinClass.sinWaveForm(amp = 1, freq=1, endTime = 5)
test2 = sinClass.sinWaveForm(amp = 2, freq=5, endTime = 5)
test3 = sinClass.sinWaveForm(amp = 4, freq=10, endTime = 5)

t = test1.calcDomain()
resultTest1 = test1.calcSinValue(t)
resultTest2 = test2.calcSinValue(t)
resultTest3 = test3.calcSinValue(t)

Ts = test1.sampleTime 					# sampling interval
Fs = 1/Ts 						# sampling rate
t = test1.calcDomain()					# time vector


