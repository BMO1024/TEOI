# Shifted sine integral function
# The sine integral function is defined as Ssi(x) = Si(x) - π/2.
import numpy as np
from scipy.integrate import quad_vec

def integrand(t):
    return np.sin(t) / t

def ssint(x):
    x = np.atleast_1d(x)
    # x is a scalar
    if x.ndim == 0:
        if x == 0:
            return -np.pi / 2
        else:
            return quad_vec(integrand, 0, x)[0] - np.pi / 2

    # x is a vector or matrix
    else:
        ssi = np.zeros_like(x, dtype=np.float64)
        for index in np.ndindex(x.shape):
            xi = x[index]
            if xi == 0:
                ssi[index] = -np.pi / 2
            else:
                ssi[index] = quad_vec(integrand, 0, xi)[0] - np.pi / 2
        return ssi