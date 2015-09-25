import numpy as np
import scipy.constants as sc
import scipy.integrate

def y(x):
    if x == 0:
        return 0
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

Integral = simpson(0,np.pi/2.0,y,100)

print("Integral numerica con mi algoritmo = " + str(Integral) + " (Notar que analiticamente es pi^4/15)")
print("Algoritmo de scipy = " + str(scipy.integrate.quad(y,0,np.pi/2.)))


Teff = 5778
P = 2*np.pi*sc.h/sc.c**2*(sc.k*Teff/sc.h)**4*Integral

Flujoti = 1366.09
Radio = sc.au*np.sqrt(Flujoti/P)
print("Radio solar =  " + str(Radio) + " [m]")
