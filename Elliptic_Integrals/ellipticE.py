# Complete and incomplete elliptic integrals of the second kind

import numpy as np
from scipy.integrate import quad_vec

def integrand_second_kind(x, m):
    return np.sqrt(1-m*np.sin(x)**2)
    
def ellipticE(*args):
    if len(args) == 1:
        m = args[0]
        return quad_vec(integrand_second_kind, 0, np.pi/2, args=(m,))[0]
    elif len(args) == 2:
        phi = args[0]
        m = args[1]
        return quad_vec(integrand_second_kind, 0, phi, args=(m,))[0]
    else:
        print("Error: Invalid input arguments")
        return None