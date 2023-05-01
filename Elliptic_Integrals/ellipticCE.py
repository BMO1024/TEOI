import numpy as np
from scipy.integrate import quad_vec

# Complementary complete elliptic integral of the second kind
def integrand_second_kind(x, m):
    return np.sqrt(1-m*np.sin(x)**2)

def elliptic_integral_second_kind_CE(m):
    mm = np.array(1-m)
    return quad_vec(integrand_second_kind, 0, np.pi/2, args=(mm,))[0]