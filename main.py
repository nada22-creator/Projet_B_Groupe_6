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
import timeit
# Importation des fonctions regroupées dans notre module d'intégration

from integration_numerique import (
    calcul_solution_analytique,
    calcul_solution_analytique_numpy,
    calcul_erreur_relative,

)
# 2. Importation depuis le Module Spécifique de la Méthode des Rectangles
from methode_rectangles import (
    integration_rectangles_base,
    integration_rectangles_numpy
)

from methode_simpson import (
    integration_simpson_base,
    integration_simpson_numpy
)

# 3. Importation depuis le Module Spécifique aux graphiques

from Graphiques import (
    tracer_convergence,
    tracer_temps_execution,
    tracer_erreurs,
    tracer_surface_polynome
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

# ============================================================================
# OUTILS DE MESURE DES PERFORMANCES (Module timeit)
# ============================================================================

def mesurer_performance(fonction_integration, *args, clics_execution=100):
    """
    Calcule le temps d'exécution moyen d'une fonction d'intégration numérique.

   """
    # 1. Répétition de la fonction via une structure lambda pour mesurer le temps cumulé
    temps_cumule = timeit.timeit(lambda: fonction_integration(*args), number=clics_execution)

    # 2. Normalisation du temps pour obtenir la durée moyenne d'une seule intégration
    temps_moyen = temps_cumule / clics_execution

    return temps_moyen

# ----------------------------------------------------------------------------
#APPELS, CHRONOMÉTRAGE ET AFFICHAGE
# ----------------------------------------------------------------------------
print("=" * 60)
print("=" * 60)
print("         ANALYSE DES PERFORMANCES TEMPORELLES (timeit)        ")
print("=" * 60)

# 1. On stocke le temps calculé dans une variable
temps_analytique_base = mesurer_performance(calcul_solution_analytique, borne_a, borne_b, p1, p2, p3, p4)

# 2. On stocke le temps calculé pour la version NumPy
temps_analytique_numpy = mesurer_performance(calcul_solution_analytique_numpy, borne_a, borne_b, coefficients_poly)

print(f"Temps de calcul (Python de base) : {temps_analytique_base:.3e} secondes")
print(f"Temps de calcul (Version NumPy)   : {temps_analytique_numpy:.3e} secondes")
print("-" * 60)

rapport = temps_analytique_base / temps_analytique_numpy
print(f"Résultat de l'analyse : NumPy est {rapport:.1f}x plus rapide ici !")
print("=" * 60)

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
# ----------------------------------------------------------------------------
# ÉTAPE 4 : Intégration Numérique - Méthode des Rectangles (Point Milieu)
# ----------------------------------------------------------------------------

# Chronométrage de la version itérative (Boucle standard)
temps_rect_base = mesurer_performance(
    integration_rectangles_base, borne_a, borne_b, p1, p2, p3, p4, n_segments_base
)

# Chronométrage de la version vectorisée (Grille linéaire NumPy)
temps_rect_numpy = mesurer_performance(
    integration_rectangles_numpy, borne_a, borne_b, coefficients_poly, n_segments_base
)

print(f"Temps de calcul (Python de base) : {temps_rect_base:.3e} secondes")
print(f"Temps de calcul (Version NumPy)   : {temps_rect_numpy:.3e} secondes")
print("-" * 60)

# Calcul créatif du gain d'efficacité grâce à la vectorisation
rapport_vitesse_rect = temps_rect_base / temps_rect_numpy
print(f"Résultat de l'analyse : NumPy est {rapport_vitesse_rect:.1f}x plus rapide sur les rectangles !")
print("=" * 60)

# ----------------------------------------------------------------------------
# ÉTAPE 4 : Intégration Numérique - Méthode simpson
# ----------------------------------------------------------------------------
print("=" * 60)
print("          MÉTHODE DE SIMPSON")
print("=" * 60)

temps_simpson_base = mesurer_performance(
    integration_simpson_base,
    borne_a,
    borne_b,
    p1, p2, p3, p4,
    n_segments_base
)

temps_simpson_numpy = mesurer_performance(
    integration_simpson_numpy,
    borne_a,
    borne_b,
    coefficients_poly,
    n_segments_base
)

print(f"Temps de calcul (Python de base) : {temps_simpson_base:.3e} secondes")
print(f"Temps de calcul (Version NumPy)   : {temps_simpson_numpy:.3e} secondes")

rapport_simpson = temps_simpson_base / temps_simpson_numpy

print("-" * 60)
print(f"Résultat de l'analyse : NumPy est {rapport_simpson:.1f}x plus rapide sur Simpson !")
print("=" * 60)

# ============================================================================
# ÉTAPE 5 : AFFICHAGE DES GRAPHIQUES
# ============================================================================

n_values = [10, 20, 50, 100, 200, 500, 1000]

erreurs_rect = []
temps_python = []
temps_numpy = []

erreurs_simp = []
temps_simpson_python = []
temps_simpson_numpy = []

for n in n_values:

    approx = integration_rectangles_numpy(
        borne_a,
        borne_b,
        coefficients_poly,
        n
    )

    erreurs_rect.append(abs(i_exact_numpy - approx))

    temps_python.append(
        mesurer_performance(
            integration_rectangles_base,
            borne_a,
            borne_b,
            p1, p2, p3, p4,
            n
        )
    )

    temps_numpy.append(
        mesurer_performance(
            integration_rectangles_numpy,
            borne_a,
            borne_b,
            coefficients_poly,
            n
        )
    )

    approx_simpson = integration_simpson_numpy(
        borne_a,
        borne_b,
        coefficients_poly,
        n
    )

    erreurs_simp.append(abs(i_exact_numpy - approx_simpson))

    temps_simpson_python.append(
        mesurer_performance(
            integration_simpson_base,
            borne_a,
            borne_b,
            p1, p2, p3, p4,
            n
        )
    )

    temps_simpson_numpy.append(
        mesurer_performance(
            integration_simpson_numpy,
            borne_a,
            borne_b,
            coefficients_poly,
            n
        )
    )

# ------------------------------------------------------------------
# AFFICHAGE DES GRAPHIQUES
# ------------------------------------------------------------------

tracer_convergence(n_values, erreurs_rect, erreurs_simp)

tracer_temps_execution(
    n_values,
    temps_python,
    temps_numpy,
    temps_simpson_python,
    temps_simpson_numpy
)

tracer_erreurs(
    n_values,
    erreurs_rect,
    erreurs_simp
)

tracer_surface_polynome(
    borne_a,
    borne_b,
    p1,
    p2,
    p3,
    p4
)