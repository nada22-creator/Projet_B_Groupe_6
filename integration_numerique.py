# ============================================================================
# MODULE : integration_numerique.py
# DESCRIPTION : Implémentation des méthodes d'intégration numérique et calculs
#               analytiques pour l'évaluation de fonctions polynomiales.
# ============================================================================

import numpy as np

# ============================================================================
# SECTION 1 : SOLUTIONS ANALYTIQUES (EXACTES)
# ============================================================================

def calcul_solution_analytique(a, b, p1, p2, p3, p4):
    """
    Calcule la valeur exacte (analytique) de l'intégrale d'un polynôme du 3e degré.
    Version en Python de base utilisant des variables standards.

    Formule de la fonction : f(x) = p1 + p2*x + p3*x^2 + p4*x^3
    Primitive : F(x) = p1*x + (p2/2)*x^2 + (p3/3)*x^3 + (p4/4)*x^4
    """
    # Évaluation de la primitive à la borne supérieure (b)
    F_b = p1 * b + (p2 / 2) * (b ** 2) + (p3 / 3) * (b ** 3) + (p4 / 4) * (b ** 4)

    # Évaluation de la primitive à la borne inférieure (a)
    F_a = p1 * a + (p2 / 2) * (a ** 2) + (p3 / 3) * (a ** 3) + (p4 / 4) * (a ** 4)

    return F_b - F_a

# ============================================================================
# SECTION 2 : Methode numpy
# ============================================================================



def calcul_solution_analytique_numpy(a, b, coefficients):
    """
    Calcule la valeur exacte (analytique) de l'intégrale en utilisant NumPy
    pour la gestion vectorisée des coefficients et des puissances (sans boucle).

    Paramètres:
        a, b (float) : Bornes d'intégration.
        coefficients (list/array) : Tableau des coefficients [p1, p2, p3, p4].
    """
    p = np.array(coefficients)
    diviseurs = np.array([1, 2, 3, 4])
    puissances = np.array([1, 2, 3, 4])

    # Calcul vectorisé des primitives aux bornes
    f_b = np.sum((p / diviseurs) * np.power(b, puissances))
    f_a = np.sum((p / diviseurs) * np.power(a, puissances))

    return f_b - f_a


def calcul_erreur_relative(valeur_exacte, valeur_approchee):
    """
    Calcule l'erreur absolue entre la solution analytique de référence
    et l'approximation numérique obtenue.
    """
    return abs(valeur_exacte - valeur_approchee)