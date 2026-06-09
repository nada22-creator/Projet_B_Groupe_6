import numpy as np
from scipy.integrate import simpson as scipy_simpson


def integration_simpson_scipy(a, b, coeffs, n):
    """
    Approximation par Simpson avec scipy.integrate.simpson.
    """
    if n <= 0:
        raise ValueError("Le nombre de segments 'n' doit être strictement positif.")

    if n % 2 != 0:
        n += 1

    x = np.linspace(a, b, n + 1)
    y = np.polyval(coeffs[::-1], x)

    return scipy_simpson(y, x=x)