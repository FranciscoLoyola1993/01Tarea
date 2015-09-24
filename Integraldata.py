import numpy as np
import scipy.integrate
import scipy.constants

wave = np.loadtxt("sun_AM0.dat", usecols = (0,))
intens = np.loadtxt("sun_AM0.dat", usecols = (1,))

def trapez(x,y):
    I = 0
    for j in range(1,len(x)-1,1):
        h = x[j+1] - x[j]
        s = h*(y[j+1] + y[j])/2.0
        I += s
    return I

Flux = trapez(wave,intens)

print("Mi algoritmo: " + str(Flux) + "( W*m^-2)" )
print("Algoritmo de scipy: " + str(scipy.integrate.trapz(intens,wave)) + "( W*m^-2)")

Lum = 4.0*np.pi*scipy.constants.au**2*Flux
Teff = 5778
Radio = (scipy.constants.au/(Teff)**2)*np.sqrt(Flux/scipy.constants.sigma)
