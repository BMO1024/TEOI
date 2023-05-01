from Elliptic_Integrals.ellipke import elliptic_integral_first_kind
from Elliptic_Integrals.ellipke import elliptic_integral_second_kind

import numpy as np
import scipy

def test_ellipke():

    m = np.array([0, 1/2, 1/4, 1])

    actual_y1 = elliptic_integral_first_kind(m)
    print("actual_y1 = ", actual_y1)
    expected_y1 = scipy.special.ellipk(m)
    print("expected_y1 = ", expected_y1)
    assert np.allclose(actual_y1, expected_y1, rtol=1e-05, atol=1e-08, equal_nan=False)

    n = np.array([0, 1/2, 1/4, 1])
    actual_y2 = elliptic_integral_second_kind(n)
    print("actual_y2 = ", actual_y2)
    expected_y2 = scipy.special.ellipe(n)
    print("expected_y2 = ", expected_y2)
    assert np.allclose(actual_y2, expected_y2, rtol=1e-05, atol=1e-08, equal_nan=False)


    