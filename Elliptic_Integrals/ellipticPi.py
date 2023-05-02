# Complete and incomplete elliptic integrals of the third kind
import numpy as np
from scipy.integrate import quad_vec

def integrand_third_kind(x, n, m):
    return 1/((1-n*np.sin(x)**2)*np.sqrt(1-m*np.sin(x)**2))

def ellipticPi(*args):
    if len(args) == 2:
        n = args[0]
        m = args[1]
        phi = np.pi/2
    elif len(args) == 3:
        n = args[0]
        phi = args[1]
        m = args[2]
    else:
        raise Exception("Invalid number of arguments")
    return quad_vec(integrand_third_kind, 0, phi, args=(n, m))[0]
    