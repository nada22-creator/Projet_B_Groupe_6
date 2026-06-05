# ============================================================================
# SECTION 3 : METHODE DES TRAPEZES
# ============================================================================

def calcul_trapeze(a, b, n, p1, p2, p3, p4):
    """
    Approximation de l'intégrale d'un polynôme du 3e degré
    par la méthode des trapèzes.

    Paramètres :
        a, b (float) : Bornes d'intégration.
        n (int) : Nombre de sous-intervalles.
        p1, p2, p3, p4 (float) : Coefficients du polynôme.

    Retour :
        float : Valeur approchée de l'intégrale.
    """

    m = (b - a) / n

    somme = 0

    for i in range(1, n):
        x = a + i * m
        fx = p1 + p2 * x + p3 * x**2 + p4 * x**3
        somme += fx

    f_a = p1 + p2 * a + p3 * a**2 + p4 * a**3
    f_b = p1 + p2 * b + p3 * b**2 + p4 * b**3

    return (m / 2) * (f_a + 2 * somme + f_b)


# ============================================================================
# SECTION 4 : METHODE DES TRAPEZES NUMPY
# ============================================================================
import numpy as np
def calcul_trapeze_numpy(a, b, n, coefficients):
    """
    Approximation de l'intégrale d'un polynôme du 3e degré
    par la méthode des trapèzes en utilisant NumPy.

    Paramètres :
        a, b (float) : Bornes d'intégration.
        n (int) : Nombre de sous-intervalles.
        coefficients (list/array) : Tableau [p1, p2, p3, p4].

    Retour :
        float : Valeur approchée de l'intégrale.
    """

    p = np.array(coefficients)

    x = np.linspace(a, b, n + 1)

    y = p[0] + p[1] * x + p[2] * x**2 + p[3] * x**3

    m = (b - a) / n

    return (m / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])