import numpy as np
from scipy.integrate import quad

def integrand(t):
    return np.sinh(t) / t

def sinhint(x):
    x = np.atleast_1d(x)
    # x is a scalar
    if x.ndim == 0:
        if x == 0:
            return 0
        elif x > 0:
            return quad(integrand, 0, x)[0]
        else:
            raise ValueError("x must be non-negative")

    # x is a vector
    if x.ndim == 1:
        shi = np.zeros_like(x, dtype=np.float64)
        for i, xi in enumerate(x):
            if xi == 0:
                shi[i] = 0
            elif xi > 0:
                shi[i] = quad(integrand, 0, xi)[0]
            else:
                raise ValueError("x must be non-negative")
        return shi

    # x is a matrix
    if x.ndim >= 2:
            shi = np.zeros_like(x, dtype=np.float64)
            for index in np.ndindex(x.shape[:-1]):
                xi = x[index]
                if xi == 0:
                    shi[index] = 0
                elif xi > 0:
                    shi[index] = quad(integrand, 0, xi)[0]
                else:
                    raise ValueError("x must be non-negative")
            return shi
        
