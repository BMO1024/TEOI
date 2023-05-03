# Elliptic nome function
import numpy as np
from scipy.integrate import quad_vec
from functools import partial

def integrand_first_kind(x, m):
    return 1/np.sqrt(1-m*np.sin(x)**2)

def ellipticK(m):
    return quad_vec(partial(integrand_first_kind, m=m), 0, np.pi/2)[0]

def ellipticNome(m):
    mm = 1-m
    return np.exp(-np.pi*ellipticK(mm)/ellipticK(m))
