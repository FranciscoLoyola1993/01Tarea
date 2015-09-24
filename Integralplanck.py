import numpy as np
import scipy.constants as sc

def y(x):
    u = np.tan(x)**3/(np.cos(x)**2)/(np.exp(np.tan(x)) - 1.0)
    return u

def simpson(a,b,f,N):
    I = 0
    dx = (b-a)/N
    I += dx*(f(a) + f(b))/3.0
    for j in range(2,N-2,1):
        s = dx*f(a + j*dx)*2.0/3.0
        if j%2 == 1:
            s *= 2
        I += s
    return I

Integral = simpson(0.01,np.pi/2.0,y,100)
Teff = 5778
P = 2*np.pi*sc.h/sc.c**2*(sc.k*Teff/sc.h)**4*Integral
