import numpy as np
import matplotlib.pyplot as plt


wave = np.loadtxt("sun_AM0.dat", usecols = (0,))
wave *= 10
intens = np.loadtxt("sun_AM0.dat", usecols = (1,))
intens *= 100

plt.plot(wave[0:1470],intens[0:1470])
plt.xlabel('Longitud de Onda  '+'$ A $', fontsize=13)
plt.ylabel('Intensidad  '+'$ ergs*s^{-1}*cm^{-2}*A^{-1} $', fontsize=13)
plt.savefig('planck.png')
