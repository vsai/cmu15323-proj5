import numpy as np

signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=float)
fourier = np.fft.fft(signal)
n = signal.size
timestep = 0.1
freq = np.fft.fftfreq(n, d=timestep)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
p = ax.plot(freq, fourier, 'b')
ax.set_xlabel('frequencies')
ax.set_ylabel('fourier values')

fig.show()
plt.show()


