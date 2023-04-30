# Logarithmic integral function
import math
import numpy as np
import scipy.special

import numpy as np
from scipy.integrate import quad, quad_vec

def integrand(t):
    return 1 / np.log(t)

def logint(x):
    # x is a scalar
    if x.ndim == 0:
        if x == 0:
            return 0
        elif x > 0:
            return quad(integrand, 1e-10, x)[0]
        else:
            raise ValueError("x must be non-negative")
    # x is a vector or matrix
    else:
        results = np.zeros(x.shape[0], dtype=np.float64)
        for i in range(x.shape[0]):
            if x[i] == 0:
                results[i] = 0
            elif x[i] > 0:
                result = quad_vec(integrand, 1e-10, x[i])
                results[i] = result[0]
            else:
                raise ValueError("x must be non-negative")
        return results

