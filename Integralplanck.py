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

Integralyo = simpson(0,np.pi/2.0,y,100)
Integralsc = scipy.integrate.quad(y,0,np.pi/2.)



Teff = 5778
Pmialgortimo = 2*np.pi*sc.h/sc.c**2*(sc.k*Teff/sc.h)**4*Integralyo
Pscp = 2*np.pi**5*sc.h/sc.c**2*(sc.k*Teff/sc.h)**4/15.

print("Intensidad con mi algoritmo = " + str(Pmialgortimo) )
print("Intensidad con Scipy = " + str(Pscp))

Flujoti = 1366.09
Radio = sc.au*np.sqrt(Flujoti/Pmialgortimo)
print("Radio solar =  " + str(Radio) + " [m]")
