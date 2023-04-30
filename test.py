from coshint import coshint
from expint import expint
from ei import ei
from sinhint import sinhint
from eulergamma import eulergamma
from cosint import cosint
from sinint import sinint
from logint import logint

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
    expected_y = -scipy.special.expi(-x)
    print("expected_y = ", expected_y)
    assert np.allclose(y, expected_y, rtol=1e-3)

def test_expint():
    x = np.array([0, 1, 2, 3, 4], dtype=np.float64)
    y1 = expint(1, x)
    print("actual_y1 = ", y1)
    expected_y1 = scipy.special.expn(1, x)
    print("expected_y1 = ", expected_y1)
    assert np.allclose(y1, expected_y1, rtol=1e-3)
    y2 = expint(2, x)
    print("actual_y2 = ", y2)
    expected_y2 = scipy.special.expn(2, x)
    print("expected_y2 = ", expected_y2)
    assert np.allclose(y2, expected_y2, rtol=1e-3)

def test_sinhint():
    x = np.array([0, 1, 2, 3, 4], dtype=np.float64)
    y = sinhint(x)
    print("actual_y = ", y)
    expected_y = scipy.special.shichi(x)[0]
    print("expected_y = ", expected_y)
    assert np.allclose(y, expected_y, rtol=1e-3)

def test_eulergamma():
    y = eulergamma()
    print("actual_y = ", y)
    expected_y = -scipy.special.digamma(1)
    print("expected_y = ", expected_y)
    assert np.allclose(y, expected_y, rtol=1e-3)

def test_cosint():
    x = np.array([0, 1, 2, 3, 4], dtype=np.float64)
    y = cosint(x)
    print("actual_y = ", y)
    expected_y = scipy.special.sici(x)[1]
    print("expected_y = ", expected_y)
    assert np.allclose(y, expected_y, rtol=1e-3)

def test_sinint():
    x = np.array([0, 1, 2, 3, 4], dtype=np.float64)
    y = sinint(x)
    print("actual_y = ", y)
    expected_y = scipy.special.sici(x)[0]
    print("expected_y = ", expected_y)
    assert np.allclose(y, expected_y, rtol=1e-3)

def test_logint():
    # Test scalar input
    x = np.array([1])
    expected_output = 0.8378669409802087
    
    assert np.isclose(logint(x), expected_output)

    # Test vector input
    x = np.array([1, 2, 3])
    expected_output = np.array([0.8378669409802087, 1.0451637801174924, 1.199675632006671])
    assert np.allclose(logint(x), expected_output)

    # Test matrix input
    x = np.array([[1, 2], [3, 4]])
    expected_output = np.array([[0.8378669409802087, 1.0451637801174924], [1.199675632006671, 1.357814674216707]])
    assert np.allclose(logint(x), expected_output)

    
if __name__ == '__main__':
    # test_coshint()
    # test_ei()
    # test_expint()
    # test_sinhint()
    # test_eulergamma()
    # test_cosint()
    # test_sinint()
    test_logint()
    
