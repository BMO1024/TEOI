import numpy as np
from scipy.integrate import quad_vec
from functools import partial

def integrand_third_kind(x, n, m):
    return 1/((1-n*np.sin(x)**2)*np.sqrt(1-m*np.sin(x)**2))

def ellipticCPi(n, m):
    mm = 1-m
    return quad_vec(partial(integrand_third_kind, n=n, m=mm), 0, np.pi/2)[0]
