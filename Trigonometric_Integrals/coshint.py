import numpy as np
from scipy.integrate import quad, quad_vec

#Euler-Mascheroni constant
_EULER = 0.5772156649015329  

def integrand(t):
    return (np.cosh(t) - 1) / t

def coshint(x):
    # convert x to an array
    x = np.atleast_1d(x)
    result = np.zeros_like(x, dtype=np.float64)
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
        chi = np.zeros_like(x, dtype=np.float64)
        for i, xi in enumerate(x):
            if xi == 0:
                chi[i] = -np.inf
            elif xi > 0:
                chi[i] = _EULER + np.log(xi) + quad(integrand, 0, xi)[0]
            else:
                raise ValueError("x must be non-negative")
        return chi

    # x is a matrix
    if x.ndim >= 2:
            chi = np.zeros_like(x, dtype=np.float64)
            for index in np.ndindex(x.shape[:-1]):
                xi = x[index]
                if xi == 0:
                    chi[index] = 0
                elif xi > 0:
                    chi[index] = quad(integrand, 0, xi)[0]
                else:
                    raise ValueError("x must be non-negative")
            return chi
        

    
