import numpy as np
from scipy.integrate import quad_vec

# Complementary complete elliptic integral of the first kind
def integrand_first_kind(x, m):
    return 1/np.sqrt(1-m*np.sin(x)**2)

def ellipticCK(m):
    mm = np.array(1-m)
    return quad_vec(integrand_first_kind, 0, np.pi/2, args=(mm,))[0]