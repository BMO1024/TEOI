# Incomplete elliptic integral of the first kind
import numpy as np
from scipy.integrate import quad_vec
from functools import partial

def integrand_first_kind(x, m):
    return 1/np.sqrt(1-m*np.sin(x)**2)

def ellipticF(phi, m):
    return quad_vec(partial(integrand_first_kind, m=m), 0, phi)[0]