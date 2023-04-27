# Exponential integral function
import numpy as np
from scipy.integrate import quad

def integrand(t, x):
    return np.exp(-x*t) / t

def ei(x):
    # One-argument exponential integral function
    if x.ndim == 0:
        if x == 0:
            return -np.inf
        elif x > 0:
            return quad(integrand, 1, np.inf, args=(x))[0]
        else:
            raise ValueError("x must be non-negative")

    if x.ndim == 1:
        y = np.zeros_like(x, dtype=np.float64)
        for i, xi in enumerate(x):
            if xi == 0:
                y[i] = -np.inf
            elif xi > 0:
                y[i] = quad(integrand, 1, np.inf, args=(xi))[0]
            else:
                raise ValueError("x must be non-negative")
        return y

    if x.ndim == 2:
        y = np.zeros_like(x, dtype=np.float64)
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                xi = x[i, j]
                if xi == 0:
                    y[i, j] = -np.inf
                elif xi > 0:
                    y[i, j] = quad(integrand, 1, np.inf, args=(xi))[0]
                else:
                    raise ValueError("x must be non-negative")
        return y
        
def expint(n,x):
    if n == 1:
        return ei(x)
    else:
        return quad(lambda t: np.exp(-x*t) / t**n, 1, np.inf)[0]
