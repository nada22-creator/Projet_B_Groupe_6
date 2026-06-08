# ============================================================================
# MODULE : methode_simpson.py
# DESCRIPTION : Implémentation de la méthode d'intégration numérique de Simpson
#               (règle composite 1/3) en Python pur et NumPy vectorisé.
# ============================================================================

import numpy as np


def integration_simpson_base(a, b, p1, p2, p3, p4, n):
    """
    Approximation numérique par la règle de Simpson composite (1/3).
    Algorithme : Boucle itérative standard (Python de base).

    Formule sur chaque segment [x_g, x_d] :
        S_i = (h/6) * (f(x_g) + 4*f(x_m) + f(x_d))
    où x_m = (x_g + x_d) / 2 est le point milieu du segment.

    Note : exacte pour tout polynôme de degré <= 3.
    """
    if n <= 0:
        raise ValueError("Le nombre de segments 'n' doit être un entier strictement positif.")

    # Simpson requiert un nombre pair de segments pour la formule composite
    if n % 2 != 0:
        n += 1

    largeur_segment = (b - a) / n
    somme_aires = 0.0

    for i in range(n):
        # Calcul des trois points caractéristiques du segment courant
        x_gauche = a + i * largeur_segment
        x_milieu = x_gauche + largeur_segment / 2.0
        x_droite = a + (i + 1) * largeur_segment

        # Évaluation de f aux trois points
        f_gauche = p1 + p2 * x_gauche + p3 * (x_gauche ** 2) + p4 * (x_gauche ** 3)
        f_milieu = p1 + p2 * x_milieu + p3 * (x_milieu ** 2) + p4 * (x_milieu ** 3)
        f_droite = p1 + p2 * x_droite + p3 * (x_droite ** 2) + p4 * (x_droite ** 3)

        # Règle de Simpson locale : (h/6) * (f_g + 4*f_m + f_d)
        somme_aires += f_gauche + 4.0 * f_milieu + f_droite

    return (largeur_segment / 6.0) * somme_aires


def integration_simpson_numpy(a, b, coeffs, n):
    """
    Approximation par la règle de Simpson composite (1/3).
    Vectorisation pure sans boucle explicite (NumPy).

    Crée simultanément les trois grilles vectorielles (x_g, x_m, x_d)
    et applique la règle de Simpson en une seule expression NumPy.
    """
    if n <= 0:
        raise ValueError("Le nombre de segments 'n' doit être un entier strictement positif.")

    if n % 2 != 0:
        n += 1

    largeur_segment = (b - a) / n

    # Génération vectorielle des trois grilles de points
    x_gauche = np.linspace(a,                    b - largeur_segment, n)
    x_milieu = np.linspace(a + largeur_segment / 2.0, b - largeur_segment / 2.0, n)
    x_droite = np.linspace(a + largeur_segment,  b,                   n)

    # Évaluation vectorielle du polynôme aux trois grilles
    # np.polyval attend les coefficients du degré le plus élevé au plus faible
    f_g = np.polyval(coeffs[::-1], x_gauche)
    f_m = np.polyval(coeffs[::-1], x_milieu)
    f_d = np.polyval(coeffs[::-1], x_droite)

    # Règle de Simpson composite en une seule opération vectorielle
    return (largeur_segment / 6.0) * np.sum(f_g + 4.0 * f_m + f_d)

