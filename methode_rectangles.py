# ============================================================================
# MODULE 2 : methode_rectangles.py
# DESCRIPTION : Implémentations de la méthode d'intégration numérique des rectangles
#               (Approche du Point Milieu) en Python pur et NumPy vectorisé.
# ============================================================================

import numpy as np


def integration_rectangles_base(a, b, p1, p2, p3, p4, n):
    """
    Approximation numérique par la méthode des rectangles (Point Milieu).
    Algorithme : Boucle itérative standard (Python de base).
    """
    # Sécurité algorithmique
    if n <= 0:
        raise ValueError("Le nombre de segments 'n' doit être un entier strictement positif.")

    largeur_segment = (b - a) / n
    somme_aires = 0.0

    # Parcours séquentiel de chaque segment
    for i in range(n):
        # Calcul géométrique du centre du segment courant
        x_milieu = a + (i + 0.5) * largeur_segment

        # Évaluation locale de la fonction f(x)
        f_x = p1 + p2 * x_milieu + p3 * (x_milieu ** 2) + p4 * (x_milieu ** 3)

        # Accumulation de la hauteur du rectangle
        somme_aires += f_x

    # Aire totale = (somme des hauteurs) * largeur
    return somme_aires * largeur_segment


def integration_rectangles_numpy(a, b, coeffs, n):
    """
    Approximation par la méthode des rectangles (Point Milieu).
    Vectorisation pure sans boucle, génération par grille linéaire.
    """
    if n <= 0:
        raise ValueError("Le nombre de segments 'n' doit être un entier strictement positif.")

    largeur_segment = (b - a) / n

    #On génère directement les points milieux en décalant une grille régulière
    # np.linspace(a, b, n, endpoint=False) crée le début de chaque segment.
    # En ajoutant (largeur_segment / 2), on obtient instantanément tous les points milieux d'un coup !
    
    x_milieux = np.linspace(a, b, n, endpoint=False) + (largeur_segment / 2.0)

    # Évaluation vectorielle ultra-rapide du polynôme (via les fonctions optimisées de NumPy en C)
    f_x = np.polyval(coeffs[::-1], x_milieux)

    # Somme de toutes les aires en une seule opération CPU
    return np.sum(f_x) * largeur_segment