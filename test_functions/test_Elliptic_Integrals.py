from Elliptic_Integrals.ellipke import ellipke
from Elliptic_Integrals.ellipticCE import ellipticCE
from Elliptic_Integrals.ellipticCK import ellipticCK
from Elliptic_Integrals.ellipticCPi import ellipticCPi
from Elliptic_Integrals.ellipticK import ellipticK
from Elliptic_Integrals.ellipticE import ellipticE
from Elliptic_Integrals.ellipticF import ellipticF
from Elliptic_Integrals.ellipticNome import ellipticNome
from Elliptic_Integrals.ellipticPi import ellipticPi

import numpy as np
import scipy

def test_ellipke():

    m = np.array([0, 1/2, 1/4, 1])

    actual_y1, actual_y2 = ellipke(m)
    print("actual_y1 = ", actual_y1)
    print("actual_y2 = ", actual_y2)
    expected_y1 = scipy.special.ellipk(m)
    print("expected_y1 = ", expected_y1)
    expected_y2 = scipy.special.ellipe(m)
    print("expected_y2 = ", expected_y2)
    assert np.allclose(actual_y1, expected_y1, rtol=1e-05, atol=1e-08, equal_nan=False)
    

def test_ellipticCE():

    m = np.array([0, 1/2, 1/4, 1])

    actual_y = ellipticCE(m)
    print("actual_y = ", actual_y)

    n = 1 - m
    expected_y = scipy.special.ellipe(n)
    print("expected_y = ", expected_y)
    assert np.allclose(actual_y, expected_y, rtol=1e-05, atol=1e-08, equal_nan=False)

def test_ellipticCK():
        
        m = np.array([0, 1/2, 1/4, 1])
    
        actual_y = ellipticCK(m)
        print("actual_y = ", actual_y)
    
        n = 1 - m
        expected_y = scipy.special.ellipk(n)
        print("expected_y = ", expected_y)
        assert np.allclose(actual_y, expected_y, rtol=1e-05, atol=1e-08, equal_nan=False)  

def test_ellipticCPi():

    (n, m) = (np.array([-1, 0, 9/10, -1]), np.array([1/3, 1/2, 1, 0]))
    actual_y = ellipticCPi(n, m)

    print("actual_y = ", actual_y)

    expected_y = np.array([1.3703, 1.8541, 4.9673, np.inf])
    print("expected_y = ", expected_y)
    assert np.allclose(actual_y, expected_y, rtol=1e-03, atol=1e-08, equal_nan=False)

def test_ellipticK():
    
        m = np.array([0, 1/2, 1/4, 1])
    
        actual_y = ellipticK(m)
        print("actual_y = ", actual_y)
    
        expected_y = scipy.special.ellipk(m)
        print("expected_y = ", expected_y)
        assert np.allclose(actual_y, expected_y, rtol=1e-05, atol=1e-08, equal_nan=False)

def test_ellipticE():
    
    m = np.array([0, 1/2, 1/4, 1])
    phi = np.pi/4

    actual_y1 = ellipticE(phi, m)
    print("actual_y1 = ", actual_y1)

    actual_y2 = ellipticE(m)
    print("actual_y2 = ", actual_y2)

    expected_y1 = scipy.special.ellipeinc(phi, m)
    print("expected_y1 = ", expected_y1)

    expected_y2 = scipy.special.ellipe(m)
    print("expected_y2 = ", expected_y2)

    assert np.allclose(actual_y1, expected_y1, rtol=1e-05, atol=1e-08, equal_nan=False)

def test_ellipticF():
    
    m = np.array([0, 1/2, 1/4, 1], dtype=np.float64)
    phi = np.pi/2

    actual_y = ellipticF(phi, m)
    print("actual_y = ", actual_y)

    expected_y = scipy.special.ellipkinc(phi, m)
    print("expected_y = ", expected_y)

    assert np.allclose(actual_y, expected_y, rtol=1e-03, atol=1e-08, equal_nan=False)

def test_ellipticNome():

    m = np.array([0, 1/2, 1])

    actual_y = ellipticNome(m)
    print("actual_y = ", actual_y)

    expected_y = np.array([0, 0.0432, 1.0000])
    print("expected_y = ", expected_y)
    assert np.allclose(actual_y, expected_y, rtol=1e-03, atol=1e-08, equal_nan=False)

def test_ellipticPi():

    (n, m, phi) = (np.array([-2.3]), np.array([0]), np.pi/4)
    actual_y1 = ellipticPi(n, phi, m)

    print("actual_y1 = ", actual_y1)

    expected_y1 = np.array([ 0.5877])
    print("expected_y1 = ", expected_y1)
    assert np.allclose(actual_y1, expected_y1, rtol=1e-03, atol=1e-08, equal_nan=False)

    actual_y2 = ellipticPi(n, m)
    print("actual_y2 = ", actual_y2)

    expected_y2 = np.array([0.8646])
    print("expected_y2 = ", expected_y2)
    assert np.allclose(actual_y2, expected_y2, rtol=1e-03, atol=1e-08, equal_nan=False)

