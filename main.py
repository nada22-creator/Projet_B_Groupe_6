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



    Démarche :
        1. Utilisation d'une fonction anonyme 'lambda' pour encapsuler la fonction
           cible avec ses arguments sans l'exécuter immédiatement.
        2. Appel de timeit.timeit() pour répéter l'exécution un grand nombre de fois
           afin d'éliminer les fluctuations système.
        3. Calcul du temps moyen d'une seule exécution.

    Paramètres:
        fonction_integration (callable) : La fonction mathématique à chronométrer.
        *args : Liste d'arguments variables requis par la fonction cible (bornes, p, n).
        clics_execution (int) : Nombre de répétitions pour la moyenne (par défaut 100).

    Retourne:
        float : Le temps d'exécution moyen d'un calcul (en secondes).
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
