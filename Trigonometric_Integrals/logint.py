# Logarithmic integral function
import numpy as np
from scipy.integrate import quad_vec

def integrand(t):
    return 1 / np.log(t)

def logint(x):
    # x is a scalar
    if x.ndim == 0:
        if x == 0:
            return 0
        elif x > 0:
            return quad_vec(integrand, np.zeros_like(x), x)[0]
        else:
            raise ValueError("x must be non-negative")
    # x is a vector or matrix
    else:
        logint = np.zeros_like(x, dtype=np.float64)
        for index in np.ndindex(x.shape):
            xi = x[index]
            if xi <= 0:
                logint[index] = 0
            else:
                logint[index] = quad_vec(integrand, np.zeros_like(xi), xi)[0]
        return logint