import numpy as np
from scipy.integrate import quad_vec

def integrand_third_kind(x, n, m):
    return 1/((1-n*np.sin(x)**2)*np.sqrt(1-m*np.sin(x)**2))

def elliptic_integral_third_kind_CPi(n, m):
    return quad_vec(integrand_third_kind, 0, np.pi/2, args=(n, 1-m))[0]