import numpy as np
import scipy

from Trigonometric_Integrals.coshint import coshint
from Trigonometric_Integrals.expint import expint
from Trigonometric_Integrals.ei import ei
from Trigonometric_Integrals.sinhint import sinhint
from Trigonometric_Integrals.eulergamma import eulergamma
from Trigonometric_Integrals.cosint import cosint
from Trigonometric_Integrals.sinint import sinint
from Trigonometric_Integrals.logint import logint
from Trigonometric_Integrals.ssint import ssi

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
    x = np.array([0, 1/4, 1/2, 1, 2, 10], dtype=np.float64)
    y = logint(x)
    print("actual_y = ", y)
    expected_y = np.array([ 0.0000, -0.1187,-0.3787, -np.inf, 1.0452, 6.1656])
    print("expected_y = ", expected_y)
    assert np.allclose(y, expected_y, rtol=1e-3)

def test_ssi():
    x = np.array([0, 1, 2, 3, 4], dtype=np.float64)
    y = ssi(x)
    print("actual_y = ", y)
    expected_y = scipy.special.sici(x)[0] - np.pi/2
    print("expected_y = ", expected_y)
    assert np.allclose(y, expected_y, rtol=1e-3)
