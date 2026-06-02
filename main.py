# ============================================================================
# PROGRAMME PRINCIPAL : main.py
# DESCRIPTION : Script du Mini-Projet B.
#               Ce fichier configure les paramètres du polynôme, appelle les
#               solutions analytiques (de base et NumPy) du module d'intégration,
#               évalue les écarts et servira de base pour les calculs numériques.
# ============================================================================
               # ----------------------------------------------------------------------------
                   # I-Configuration premiere Methode de reference : Integration numerique
               # ----------------------------------------------------------------------------



# ----------------------------------------------------------------------------
# ÉTAPE 1 : Importations des bibliothèques et du module d'analyse numérique
# ----------------------------------------------------------------------------
import numpy as np

# Importation des fonctions analytiques regroupées dans notre module unique
from integration_numerique import (
    calcul_solution_analytique,
    calcul_solution_analytique_numpy,
    calcul_erreur_relative
)

# ----------------------------------------------------------------------------
# ÉTAPE 2 : Définition des paramètres de l'exercice
# ----------------------------------------------------------------------------
# Coefficients du polynôme du 3e degré : f(x) = p1 + p2*x + p3*x^2 + p4*x^3
p1, p2, p3, p4 = 1.0, 2.0, 3.0, 4.0
coefficients_poly = [p1, p2, p3, p4]  # Format liste/tableau pour la version NumPy

# Bornes de l'intervalle d'intégration [a, b]
borne_a = -2.0
borne_b = 3.0

# Nombre de segments initial pour la validation des méthodes numériques
n_segments_base = 10


# ----------------------------------------------------------------------------
# ÉTAPE 3 : Calcul et validation des solutions de référence (Analytiques)
# ----------------------------------------------------------------------------
print("=" * 60)
print("             VALIDATION DES SOLUTIONS ANALYTIQUES             ")
print("=" * 60)

# 3.1 Appel de la méthode analytique classique (Python de base)
i_exact_base = calcul_solution_analytique(borne_a, borne_b, p1, p2, p3, p4)
print(f"Solution exacte (Python de base) : {i_exact_base:.6f}")

# 3.2 Appel de la méthode analytique optimisée (NumPy vectorisé)
i_exact_numpy = calcul_solution_analytique_numpy(borne_a, borne_b, coefficients_poly)
print(f"Solution exacte (Via NumPy)       : {i_exact_numpy:.6f}")

# 3.3 Vérification de la cohérence entre les deux approches analytiques
difference_analytique = calcul_erreur_relative(i_exact_base, i_exact_numpy)
print(f"Écart entre les deux fonctions   : {difference_analytique:.6e}")
print("-" * 60)


