# Cosine integral function
import math
import numpy as np
import scipy.special

import numpy as np
from scipy.integrate import quad

#Euler-Mascheroni constant
_EULER = 0.5772156649015329  

def integrand(t):
    return (np.cos(t) - 1) / t

def cosint(x):
    # x is a scalar
    if x.ndim == 0:
        if x == 0:
            return -np.inf
        elif x > 0:
            return _EULER + np.log(x) + quad(integrand, 0, x)[0]
        else:
            raise ValueError("x must be non-negative")

    # x is a vector
    if x.ndim == 1:
        cosint = np.zeros_like(x, dtype=np.float64)
        for i, xi in enumerate(x):
            if xi == 0:
                cosint[i] = -np.inf
            elif xi > 0:
                cosint[i] = _EULER + np.log(xi) + quad(integrand, 0, xi)[0]
            else:
                raise ValueError("x must be non-negative")
        return cosint

    # x is a matrix
    if x.ndim == 2:
        cosint = np.zeros_like(x, dtype=np.float64)
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                xi = x[i, j]
                if xi == 0:
                    cosint[i, j] = -np.inf
                elif xi > 0:
                    cosint[i, j] = _EULER + np.log(xi) + quad(integrand, 0, xi)[0]
                else:
                    raise ValueError("x must be non-negative")
        return cosint

    
