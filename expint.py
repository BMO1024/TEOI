# Exponential integral function
import numpy as np
from scipy.integrate import quad

def integrand_ei(t):
    return np.exp(-t) / t

def integrand_expint(t, n, x):
    return np.exp(-x*t) * t**(-n)

def ei(x):
    # One-argument exponential integral function

    # x is a scalar
    if x.ndim == 0:
        if x == 0:
            return np.inf
        return quad(integrand_ei, x, np.inf)[0]

    # x is a vector
    if x.ndim == 1:
        y = np.zeros_like(x, dtype=np.float64)
        for i, xi in enumerate(x):
            # print("i = ", i)
            # print("xi = ", xi)
            if xi == 0:
                xi = 1e-10
                y[i] = np.inf
            else:
                y[i] = quad(integrand_ei, xi, np.inf)[0]

            # print("y[i] = ",y[i])
        return y

    # x is a matrix
    if x.ndim == 2:
        y = np.zeros_like(x, dtype=np.float64)
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                xi = x[i, j]
                if xi == 0:
                    y[i, j] = np.inf
                y[i, j] = quad(integrand_ei, xi, np.inf)[0]
        return y

def expint(n,x):
    # Two-argument exponential integral function
    # x is a scalar
    if x.ndim == 0:
        return quad(integrand_expint, 1, np.inf, args=(n, x))[0]

    # x is a vector
    if x.ndim == 1:
        y = np.zeros_like(x, dtype=np.float64)
        for i, xi in enumerate(x):
            y[i] = quad(integrand_expint, 1, np.inf, args=(n, xi))[0]
        return y

    # x is a matrix
    if x.ndim == 2:
        y = np.zeros_like(x, dtype=np.float64)
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                xi = x[i, j]
                y[i, j] = quad(integrand_expint, 1, np.inf, args=(n, xi))[0]
        return y

    else:
        raise ValueError("x must be a scalar, vector, or matrix")