"""
rectangles.py
=============
§2.1 — Méthode des rectangles (Python de base + NumPy).
MGA 802 — Mini-Projet B

Ce script expose une fonction run() qui :
  1. Calcule l'intégrale par rectangles (Python + NumPy)
  2. Mesure les temps d'exécution via timeit
  3. Génère les figures §2.1
  4. Retourne un dict de données pour les scripts suivants
"""

import timeit
import numpy as np
import figures


# ─────────────────────────────────────────────────────────────
# Fonctions communes (réutilisées par les autres scripts)
# ─────────────────────────────────────────────────────────────

def polynome(x, p1, p2, p3, p4):
    """Évalue f(x) = p1 + p2*x + p3*x² + p4*x³."""
    return p1 + p2*x + p3*x**2 + p4*x**3


def solution_analytique(a, b, p1, p2, p3, p4):
    """Calcule l'intégrale exacte par la primitive analytique."""
    def F(x):
        return p1*x + (p2/2)*x**2 + (p3/3)*x**3 + (p4/4)*x**4
    return F(b) - F(a)


def calcul_erreur(I_num, I_exact):
    """Retourne l'erreur absolue |I_num - I_exact|."""
    return abs(I_num - I_exact)


# ─────────────────────────────────────────────────────────────
# Méthode des rectangles — Python de base
# ─────────────────────────────────────────────────────────────

def rectangles_python(a, b, n, p1, p2, p3, p4):
    """
    Intégration par rectangles (centre) — Python de base.

    Divise [a,b] en n segments, évalue f au centre de chaque
    segment et somme les aires h * f(x_centre).
    """
    h = (b - a) / n
    somme = 0.0
    for i in range(n):
        x_centre = a + (i + 0.5) * h
        somme += polynome(x_centre, p1, p2, p3, p4)
    return h * somme


def erreur_rectangles_python(a, b, n, p1, p2, p3, p4):
    """Retourne l'erreur absolue pour n segments (Python)."""
    return calcul_erreur(
        rectangles_python(a, b, n, p1, p2, p3, p4),
        solution_analytique(a, b, p1, p2, p3, p4)
    )


def convergence_python(a, b, liste_n, p1, p2, p3, p4):
    """Calcule l'erreur pour chaque n de liste_n (Python)."""
    return [erreur_rectangles_python(a, b, n, p1, p2, p3, p4) for n in liste_n]


def temps_python(a, b, n, p1, p2, p3, p4, repetitions=300):
    """Mesure le temps moyen via timeit (Python)."""
    return timeit.timeit(
        lambda: rectangles_python(a, b, n, p1, p2, p3, p4),
        number=repetitions
    ) / repetitions


# ─────────────────────────────────────────────────────────────
# Méthode des rectangles — NumPy vectorisé
# ─────────────────────────────────────────────────────────────

def rectangles_numpy(a, b, n, p1, p2, p3, p4):
    """
    Intégration par rectangles (centre) — NumPy vectorisé.

    Crée tous les centres en une ligne avec np.linspace,
    évalue f en une opération vectorielle, somme avec np.sum.
    """
    h = (b - a) / n
    x_centres = np.linspace(a + h/2, b - h/2, n)
    return h * np.sum(polynome(x_centres, p1, p2, p3, p4))


def erreur_rectangles_numpy(a, b, n, p1, p2, p3, p4):
    """Retourne l'erreur absolue pour n segments (NumPy)."""
    return calcul_erreur(
        rectangles_numpy(a, b, n, p1, p2, p3, p4),
        solution_analytique(a, b, p1, p2, p3, p4)
    )


def convergence_numpy(a, b, liste_n, p1, p2, p3, p4):
    """Calcule l'erreur pour chaque n de liste_n (NumPy)."""
    return [erreur_rectangles_numpy(a, b, n, p1, p2, p3, p4) for n in liste_n]


def temps_numpy(a, b, n, p1, p2, p3, p4, repetitions=300):
    """Mesure le temps moyen via timeit (NumPy)."""
    return timeit.timeit(
        lambda: rectangles_numpy(a, b, n, p1, p2, p3, p4),
        number=repetitions
    ) / repetitions


# ─────────────────────────────────────────────────────────────
# run() — point d'entrée appelé par main.py
# ─────────────────────────────────────────────────────────────

def run(params, liste_n, reps=300):
    """
    Exécute §2.1 : calculs + figures.

    Paramètres
    ----------
    params  : dict  Clés : a, b, p1, p2, p3, p4, n_test
    liste_n : list  Grille de n pour les graphiques
    reps    : int   Répétitions timeit

    Retourne
    --------
    dict : Données calculées (erreurs + temps) à passer
           aux scripts suivants (trapezes, simpson...).
    """
    a, b   = params["a"], params["b"]
    p1, p2, p3, p4 = params["p1"], params["p2"], params["p3"], params["p4"]
    n_test = params["n_test"]
    I_exact = solution_analytique(a, b, p1, p2, p3, p4)

    SEP = "=" * 65
    print(SEP)
    print("§ 2.1  Méthode des Rectangles")
    print(SEP)
    print(f"  Solution analytique exacte : I = {I_exact:.10f}")
    print("-" * 65)

    # ── Calculs ponctuels (n = n_test) ────────────────────────
    I_py = rectangles_python(a, b, n_test, p1, p2, p3, p4)
    t_py = temps_python(a, b, n_test, p1, p2, p3, p4, reps)
    print(f"  Python  : I = {I_py:.10f}  |  erreur = {calcul_erreur(I_py, I_exact):.3e}  |  temps = {t_py*1e6:.1f} µs")

    I_np = rectangles_numpy(a, b, n_test, p1, p2, p3, p4)
    t_np = temps_numpy(a, b, n_test, p1, p2, p3, p4, reps)
    print(f"  NumPy   : I = {I_np:.10f}  |  erreur = {calcul_erreur(I_np, I_exact):.3e}  |  temps = {t_np*1e6:.1f} µs")

    # ── Données convergence & temps sur toute la grille ───────
    err_py = convergence_python(a, b, liste_n, p1, p2, p3, p4)
    err_np = convergence_numpy( a, b, liste_n, p1, p2, p3, p4)
    t_list_py = [temps_python(a, b, n, p1, p2, p3, p4, reps) for n in liste_n]
    t_list_np = [temps_numpy( a, b, n, p1, p2, p3, p4, reps) for n in liste_n]

    # ── Figures §2.1 ──────────────────────────────────────────
    print()
    figures.fig_illustration_rectangles(a, b, [15, 50, 500], p1, p2, p3, p4)

    series_conv = [
        {"label": "Rect. Python", "methode": "Rectangles", "impl": "Python", "erreurs": err_py},
        {"label": "Rect. NumPy",  "methode": "Rectangles", "impl": "NumPy",  "erreurs": err_np},
    ]
    figures.fig_convergence(liste_n, series_conv,
                            titre="§2.1 — Convergence Rectangles",
                            nom_fichier="fig_convergence.png")

    series_temps = [
        {"label": "Rect. Python", "methode": "Rectangles", "impl": "Python", "temps": t_list_py},
        {"label": "Rect. NumPy",  "methode": "Rectangles", "impl": "NumPy",  "temps": t_list_np},
    ]
    figures.fig_temps(liste_n, series_temps,
                      titre="§2.1 — Temps de calcul Rectangles",
                      nom_fichier="fig_temps.png")

    print("\n✓ §2.1 terminé.\n")

    # ── Retourne les données pour les scripts suivants ─────────
    return {
        "I_exact"      : I_exact,
        "series_conv"  : series_conv,
        "series_temps" : series_temps,
        "erreurs_ponctuelles": [
            {"label": "Rect.\nPython", "erreur": calcul_erreur(I_py, I_exact)},
            {"label": "Rect.\nNumPy",  "erreur": calcul_erreur(I_np, I_exact)},
        ],
    }

