# ============================================================================
# PROGRAMME PRINCIPAL : main.py
# DESCRIPTION : Script directeur du Mini-Projet B.
#               Ce fichier configure les paramètres, appelle les fonctions
#               du module d'intégration, mesure les temps d'exécution (timeit)
#               et génère les graphiques de convergence et de performance.
# ============================================================================

# ----------------------------------------------------------------------------
# ÉTAPE 1 : Importation des bibliothèques standards, scientifiques et modules
# ----------------------------------------------------------------------------

# Importation de notre module personnalisé d'analyse numérique
from integration_numerique import calcul_solution_analytique, calcul_erreur_relative


# ----------------------------------------------------------------------------
# ÉTAPE 2 : Définition des conditions initiales et paramètres du problème
# ----------------------------------------------------------------------------

# Coefficients fixés pour le polynôme du 3e degré : f(x) = p1 + p2*x + p3*x^2 + p4*x^3
p1, p2, p3, p4 = 1.0, 2.0, 3.0, 4.0

# Bornes d'intégration [a, b]
borne_a = -2.0
borne_b = 3.0

# Paramètre initial pour le nombre de segments (Étape de base)
n_segments_base = 10


# ----------------------------------------------------------------------------
# ÉTAPE 3 : Calcul de la solution de référence (Solution Analytique Exacte)
# ----------------------------------------------------------------------------
# Nous calculons d'abord I_exact qui servira de métrique pour quantifier
# l'exactitude de nos futures approximations numériques.
i_exact = calcul_solution_analytique(borne_a, borne_b, p1, p2, p3, p4)

print("-" * 50)
print(f"SOLUTION ANALYTIQUE DE RÉFÉRENCE : {i_exact}")
print("-" * 50)


# ----------------------------------------------------------------------------
# ÉTAPE 4 : Analyse comparative (À compléter au fil des questions)
# TODO:
#  - Appels des méthodes (Rectangles, Trapèzes, Simpson, Méthodes pré-programmées)
#  - Évaluation des performances temporelles avec la fonction timeit
#  - Génération des courbes comparatives (Erreur vs Segments / Temps vs Segments)
# ----------------------------------------------------------------------------