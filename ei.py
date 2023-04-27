import numpy as np
from scipy.integrate import quad

def integrand(t, x):
    return np.exp(-x*t) / t

def ei(x):
    # One-argument exponential integral function
    return 0 