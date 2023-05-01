import numpy as np
from scipy.integrate import quad_vec

def integrand_first_kind(x, m):
    return 1/np.sqrt(1-m*np.sin(x)**2)

def integrand_second_kind(x, m):
    return np.sqrt(1-m*np.sin(x)**2) 

def elliptic_integral_first_kind(m):
    return quad_vec(integrand_first_kind, 0, np.pi/2, args=(m,))[0]

def elliptic_integral_second_kind(m):
    return quad_vec(integrand_second_kind, 0, np.pi/2, args=(m,))[0]

def ellipke(n, m):
    return elliptic_integral_first_kind(m), elliptic_integral_second_kind(m)