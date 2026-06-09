# ============================================================================
# PROGRAMME PRINCIPAL : main.py
# DESCRIPTION : Script du Mini-Projet B.
#               Ce fichier configure les paramètres du polynôme, appelle les
#               solutions analytiques (de base et NumPy) du module d'intégration,
#               évalue les écarts et génère l'analyse de convergence.
# AUTEURS : Groupe 6
# ÉCOLE : École de technologie supérieure (ÉTS)
# ============================================================================

import timeit
import numpy as np

# 1. Importation des fonctions analytiques et de métrique

from integration_numerique import (
    calcul_erreur_relative,
    calcul_solution_analytique,
    calcul_solution_analytique_numpy,
)

# 2. Importation depuis le Module Spécifique de la Méthode des Rectangles

from methode_rectangles import (
    integration_rectangles_base,
    integration_rectangles_numpy,
)

from methode_simpson import (
    integration_simpson_base,
    integration_simpson_numpy
)

# 3. Importation depuis le Module Spécifique aux graphiques

from Graphiques import tracer_tableau_bord


# ============================================================================
# OUTILS DE MESURE DES PERFORMANCES
# ============================================================================
def mesurer_performance(fonction_integration, *args, clics_execution=100):
    """Calcule le temps d'exécution moyen d'une fonction d'intégration.

    Parameters:
    -----------
    fonction_integration : function
        La fonction Python ou NumPy à benchmarker.
    *args : arguments
        Les paramètres à passer à la fonction d'intégration.
    clics_execution : int, optional
        Le nombre de répétitions pour stabiliser la mesure (default: 100).

    Returns:
    --------
    float : Temps d'exécution moyen d'une seule intégration (en secondes).
    """
    # Utilisation d'une structure lambda pour éviter les effets de bord au chronométrage
    temps_cumule = timeit.timeit(
        lambda: fonction_integration(*args), number=clics_execution
    )
    return temps_cumule / clics_execution


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
# EXECUTION DU PROGRAMME PRINCIPAL (__main__)
# ============================================================================

if __name__ == "__main__":

    # --- ÉTAPE 2 : Définition des paramètres du problème ---
    # Coefficients du polynôme : f(x) = p1 + p2*x + p3*x^2 + p4*x^3
    p1, p2, p3, p4 = 1.0, 2.0, 3.0, 4.0
    coefficients_poly = [p1, p2, p3, p4]

erreurs_simp = []
temps_simpson_python = []
temps_simpson_numpy = []

for n in n_values:
    # Bornes de l'intervalle d'intégration [a, b]
    borne_a = -2.0
    borne_b = 3.0

    # Nombre de segments initial pour la validation des méthodes
    n_segments_base = 10

    # --- ÉTAPE 3 : Validation et performance des solutions analytiques ---
    print("=" * 70)
    print(f"{'ANALYSE DES SOLUTIONS ANALYTIQUES DE RÉFÉRENCE':^70}")
    print("=" * 70)

    # Appels des méthodes analytiques
    i_exact_base = calcul_solution_analytique(
        borne_a, borne_b, p1, p2, p3, p4
    )
    i_exact_numpy = calcul_solution_analytique_numpy(
        borne_a, borne_b, coefficients_poly
    )
    difference_analytique = calcul_erreur_relative(
        i_exact_base, i_exact_numpy
    )

    print(f"Solution exacte (Python de base) : {i_exact_base:.6f}")
    print(f"Solution exacte (Via NumPy)       : {i_exact_numpy:.6f}")
    print(f"Écart relatif analytique          : {difference_analytique:.6e}")
    print("-" * 70)

    # Chronométrage des versions analytiques
    temps_analytique_base = mesurer_performance(
        calcul_solution_analytique, borne_a, borne_b, p1, p2, p3, p4
    )
    temps_analytique_numpy = mesurer_performance(
        calcul_solution_analytique_numpy,
        borne_a,
        borne_b,
        coefficients_poly,
    )
    rapport_analytique = temps_analytique_base / temps_analytique_numpy

    # Rendu arrondi  (.7f)
    print(f"Temps de calcul (Python de base) : {temps_analytique_base:.7f} s")
    print(f"Temps de calcul (Version NumPy)   : {temps_analytique_numpy:.7f} s")
    print(f"Gain d'efficacité Analytique     : NumPy est {rapport_analytique:.1f}x plus rapide")
    print("=" * 70)
    print("\n")

    # --- ÉTAPE 4 : Intégration Numérique - Méthode des Rectangles (n = 10) ---
    print("=" * 70)
    print(f"{'MÉTHODE DES RECTANGLES : VALIDATION ET PERFORMANCE (n = 10)':^70}")
    print("=" * 70)

    temps_rect_base = mesurer_performance(
        integration_rectangles_base,
        borne_a,
        borne_b,
        p1,
        p2,
        p3,
        p4,
        n_segments_base,
    )
    temps_rect_numpy = mesurer_performance(
        integration_rectangles_numpy,
        borne_a,
        borne_b,
        coefficients_poly,
        n_segments_base,
    )
    rapport_vitesse_rect = temps_rect_base / temps_rect_numpy

    # Rendu arrondi  (.7f)
    print(f"Temps de calcul (Python de base) : {temps_rect_base:.7f} s")
    print(f"Temps de calcul (Version NumPy)   : {temps_rect_numpy:.7f} s")
    print(f"Gain d'efficacité Numérique      : NumPy est {rapport_vitesse_rect:.1f}x plus rapide")
    valeur_rect_10 = integration_rectangles_numpy(borne_a, borne_b, coefficients_poly, 10)
    erreur_rect_10 = abs(i_exact_numpy - valeur_rect_10)
    print(f"Valeur obtenue Rectangles (n=10) : {valeur_rect_10:.6f}")
    print(f"Erreur Rectangles (n=10)         : {erreur_rect_10:.6f}")

    print("=" * 70)
    print("\n")
    print("=" * 70)
    print("\n")

    # --- ÉTAPE 5 : Analyse de Convergence et Graphiques ---
    print("Génération de l'analyse de convergence en cours...")

    n_values = [10, 20, 50, 100, 200, 500, 1000]

    erreurs_rect = []
    temps_python = []
    temps_numpy = []

    for n in n_values:
        # Mesure de performance et stockage direct du temps (Python de base)
        t_py = mesurer_performance(
            integration_rectangles_base,
            borne_a,
            borne_b,
            p1,
            p2,
            p3,
            p4,
            n,
        )
        temps_python.append(t_py)

        # Mesure de performance et stockage direct du temps (NumPy)
        t_np = mesurer_performance(
            integration_rectangles_numpy,
            borne_a,
            borne_b,
            coefficients_poly,
            n,
        )
        temps_numpy.append(t_np)

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
        # Calcul de l'erreur absolue
        approx = integration_rectangles_numpy(
            borne_a, borne_b, coefficients_poly, n
        )
        erreurs_rect.append(abs(i_exact_numpy - approx))

    print("Calculs terminés. Affichage du tableau de bord graphique.")
    print("=" * 70)

    # Affichage final structuré
    tracer_tableau_bord(
        n_values,
        erreurs_rect,
        temps_python,
        temps_numpy,
        borne_a,
        borne_b,
        p1,
        p2,
        p3,
        p4,
    )
