import numpy as np
from scipy.integrate import quad_vec
from functools import partial


# Complementary complete elliptic integral of the second kind
def integrand_second_kind(x, m):
    return np.sqrt(1-m*np.sin(x)**2)

def ellipticCE(m):
    mm = np.array(1-m)
    return quad_vec(partial(integrand_second_kind, m=mm), 0, np.pi/2)[0]
