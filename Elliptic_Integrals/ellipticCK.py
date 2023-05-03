import numpy as np
from scipy.integrate import quad_vec
from functools import partial

# Complementary complete elliptic integral of the first kind
def integrand_first_kind(x, m):
    return 1/np.sqrt(1-m*np.sin(x)**2)

def ellipticCK(m):
    mm = np.array(1-m)
    return quad_vec(partial(integrand_first_kind, m=mm), 0, np.pi/2)[0]
