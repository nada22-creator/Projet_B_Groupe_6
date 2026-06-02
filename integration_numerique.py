# ============================================================================
# MODULE : integration_numerique.py
# DESCRIPTION : Implémentation des méthodes d'intégration numérique et calculs
#               analytiques pour l'évaluation de fonctions polynomiales.
# ============================================================================

def calcul_solution_analytique(a, b, p1, p2, p3, p4):
    """
    Calcule la valeur exacte (analytique) de l'intégrale d'un polynôme du 3e degré.

    Formule de la fonction : f(x) = p1 + p2*x + p3*x^2 + p4*x^3
    Démarche : Utilisation de la primitive F(x) pour appliquer le théorème
               fondamental de l'analyse : I = F(b) - F(a).
               F(x) = p1*x + (p2/2)*x^2 + (p3/3)*x^3 + (p4/4)*x^4

    Paramètres:
        a, b (float) : Bornes d'intégration (inférieure et supérieure).
        p1, p2, p3, p4 (float) : Coefficients du polynôme.

    Retourne:
        float : Valeur exacte de l'intégrale sous la courbe.
    """
    # Évaluation de la primitive à la borne supérieure (b)
    F_b = p1 * b + (p2 / 2) * (b ** 2) + (p3 / 3) * (b ** 3) + (p4 / 4) * (b ** 4)

    # Évaluation de la primitive à la borne inférieure (a)
    F_a = p1 * a + (p2 / 2) * (a ** 2) + (p3 / 3) * (a ** 3) + (p4 / 4) * (a ** 4)

    # Retour de la solution exacte (Référence absolue pour le calcul d'erreur)
    return F_b - F_a


def calcul_erreur_relative(valeur_exacte, valeur_approchee):
    """
    Calcule l'erreur absolue (ou relative) entre la solution analytique
    et l'approximation numérique obtenue.

    Sert à évaluer la précision et la convergence des méthodes.
    """
    return abs(valeur_exacte - valeur_approchee)