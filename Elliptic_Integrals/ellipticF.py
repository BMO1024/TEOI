# Incomplete elliptic integral of the first kind
import numpy as np
from scipy.integrate import quad_vec

def integrand_first_kind(m, x):
    return 1/np.sqrt(1-m*np.sin(x)**2)

def ellipticF(phi, m):
    return quad_vec(integrand_first_kind, 0, phi, args=(m,))[0]
        