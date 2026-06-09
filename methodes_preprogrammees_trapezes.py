# ============================================================================
# SECTION 5 : METHODE PREPROGRAMMEE NUMPY
# ============================================================================
import numpy as np

def calcul_trapeze_preprogramme(a, b, n, coefficients):
    """
    Approximation de l'intégrale à l'aide de la fonction
    préprogrammée np.trapezoid() de NumPy.

    Paramètres :
        a, b (float) : Bornes d'intégration.
        n (int) : Nombre de sous-intervalles.
        coefficients (list/array) : Tableau [p1, p2, p3, p4].

    Retour :
        float : Valeur approchée de l'intégrale.
    """

    p1, p2, p3, p4 = coefficients

    # Discrétisation de l'intervalle
    x = np.linspace(a, b, n + 1)

    # Évaluation du polynôme
    y = p1 + p2 * x + p3 * x**2 + p4 * x**3

    # Intégration avec la fonction préprogrammée NumPy
    return np.trapezoid(y, x)