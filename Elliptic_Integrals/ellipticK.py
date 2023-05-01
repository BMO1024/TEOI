import numpy as np
from scipy.integrate import quad_vec

def integrand_first_kind(x, m):
    return 1/np.sqrt(1-m*np.sin(x)**2)

def ellipticK(m):
    return quad_vec(integrand_first_kind, 0, np.pi/2, args=(m,))[0]
