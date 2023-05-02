# Logarithmic integral function
import numpy as np
from scipy.integrate import quad_vec

def integrand(t):
    return 1 / np.log(t)

def logint(x):
    if not isinstance(x, (int, float, np.ndarray)):
        raise TypeError("Input must be a number or an array of numbers")
    x = np.atleast_1d(x)
    result = np.zeros_like(x)
    for i, xi in enumerate(x):
        if xi == 0:
            result[i] = 0
        elif xi == 1:
            result[i] = -np.inf
        elif xi > 1:
            epsilon = 1e-10
            result[i] = quad_vec(integrand, 1+epsilon, xi)[0] + quad_vec(integrand, 0, 1-epsilon)[0]
        elif xi < 1:
            result[i] = quad_vec(integrand, 0, xi)[0]     

    return np.asarray(result, dtype=np.float64)