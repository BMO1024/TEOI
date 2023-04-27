from coshint import coshint
from ei import ei
import math
import numpy as np
import scipy

def test_coshint():
    x = np.array([0, 1, 2, 3, 4], dtype=np.float64)
    y = coshint(x)
    print("actual_y = ", y)
    expected_y = scipy.special.shichi(x)[1]
    print("expected_y = ", expected_y)
    assert np.allclose(y, expected_y, rtol=1e-3)

def test_ei():
    x = np.array([0, 1, 2, 3, 4], dtype=np.float64)
    y = ei(x)
    print("actual_y = ", y)
    expected_y = scipy.special.expi(x)
    print("expected_y = ", expected_y)
    assert np.allclose(y, expected_y, rtol=1e-3)

if __name__ == '__main__':
    test_coshint()
    # test_ei()
