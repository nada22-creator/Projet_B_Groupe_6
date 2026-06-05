"""
simpson.py
==========
§2.3 — Méthode de Simpson (Python de base + NumPy).
MGA 802 — Mini-Projet B

Ce script expose une fonction run() qui :
  1. Calcule l'intégrale par Simpson (Python + NumPy)
  2. Met à jour les figures convergence + temps (cumul §2.1 + §2.2)
  3. Retourne un dict enrichi à passer au script suivant
"""

import timeit
import numpy as np
import figures
from rectangles import polynome, solution_analytique, calcul_erreur


# ─────────────────────────────────────────────────────────────
# Méthode de Simpson — Python de base
# ─────────────────────────────────────────────────────────────

def simpson_python(a, b, n, p1, p2, p3, p4):
    """
    Intégration par la règle de Simpson composée — Python de base.

    Sur chaque segment [x_i, x_{i+1}], utilise le point milieu x_m :
        S_i = h/6 * (f(x_g) + 4*f(x_m) + f(x_d))

    Note : exacte pour les polynômes de degré ≤ 3.
    """
    if n % 2 != 0:
        n += 1                        # Simpson requiert n pair
    h = (b - a) / n
    somme = 0.0
    for i in range(n):
        x_g = a + i * h
        x_m = x_g + h / 2
        x_d = a + (i + 1) * h
        somme += (polynome(x_g, p1, p2, p3, p4)
                  + 4 * polynome(x_m, p1, p2, p3, p4)
                  + polynome(x_d, p1, p2, p3, p4))
    return (h / 6) * somme


def erreur_simpson_python(a, b, n, p1, p2, p3, p4):
    """Retourne l'erreur absolue pour n segments (Python)."""
    return calcul_erreur(
        simpson_python(a, b, n, p1, p2, p3, p4),
        solution_analytique(a, b, p1, p2, p3, p4)
    )


def convergence_python(a, b, liste_n, p1, p2, p3, p4):
    """Calcule l'erreur pour chaque n de liste_n (Python)."""
    return [erreur_simpson_python(a, b, n, p1, p2, p3, p4) for n in liste_n]


def temps_python(a, b, n, p1, p2, p3, p4, repetitions=300):
    """Mesure le temps moyen via timeit (Python)."""
    return timeit.timeit(
        lambda: simpson_python(a, b, n, p1, p2, p3, p4),
        number=repetitions
    ) / repetitions


# ─────────────────────────────────────────────────────────────
# Méthode de Simpson — NumPy vectorisé
# ─────────────────────────────────────────────────────────────

def simpson_numpy(a, b, n, p1, p2, p3, p4):
    """
    Intégration par la règle de Simpson composée — NumPy vectorisé.

    Crée trois tableaux vectoriels (x_g, x_m, x_d) en une seule
    opération np.linspace, puis calcule la somme de Simpson en
    une expression numpy sans boucle.
    """
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    x_g = np.linspace(a,       b - h, n)
    x_m = np.linspace(a + h/2, b - h/2, n)
    x_d = np.linspace(a + h,   b,     n)
    return (h / 6) * np.sum(
        polynome(x_g, p1, p2, p3, p4)
        + 4 * polynome(x_m, p1, p2, p3, p4)
        + polynome(x_d, p1, p2, p3, p4)
    )


def erreur_simpson_numpy(a, b, n, p1, p2, p3, p4):
    """Retourne l'erreur absolue pour n segments (NumPy)."""
    return calcul_erreur(
        simpson_numpy(a, b, n, p1, p2, p3, p4),
        solution_analytique(a, b, p1, p2, p3, p4)
    )


def convergence_numpy(a, b, liste_n, p1, p2, p3, p4):
    """Calcule l'erreur pour chaque n de liste_n (NumPy)."""
    return [erreur_simpson_numpy(a, b, n, p1, p2, p3, p4) for n in liste_n]


def temps_numpy(a, b, n, p1, p2, p3, p4, repetitions=300):
    """Mesure le temps moyen via timeit (NumPy)."""
    return timeit.timeit(
        lambda: simpson_numpy(a, b, n, p1, p2, p3, p4),
        number=repetitions
    ) / repetitions


# ─────────────────────────────────────────────────────────────
# run() — point d'entrée appelé par main.py
# ─────────────────────────────────────────────────────────────

def run(params, liste_n, donnees_precedentes, reps=300):
    """
    Exécute §2.3 : calculs + mise à jour des figures.

    Paramètres
    ----------
    params              : dict  a, b, p1, p2, p3, p4, n_test
    liste_n             : list  Grille de n pour les graphiques
    donnees_precedentes : dict  Retour de trapezes.run()
    reps                : int   Répétitions timeit

    Retourne
    --------
    dict : Données enrichies à passer au script suivant.
    """
    a, b   = params["a"], params["b"]
    p1, p2, p3, p4 = params["p1"], params["p2"], params["p3"], params["p4"]
    n_test  = params["n_test"]
    I_exact = donnees_precedentes["I_exact"]

    SEP = "=" * 65
    print(SEP)
    print("§ 2.3  Méthode de Simpson")
    print(SEP)

    # ── Calculs ponctuels ──────────────────────────────────────
    I_py = simpson_python(a, b, n_test, p1, p2, p3, p4)
    t_py = temps_python(a, b, n_test, p1, p2, p3, p4, reps)
    print(f"  Python  : I = {I_py:.10f}  |  erreur = {calcul_erreur(I_py, I_exact):.3e}  |  temps = {t_py*1e6:.1f} µs")

    I_np = simpson_numpy(a, b, n_test, p1, p2, p3, p4)
    t_np = temps_numpy(a, b, n_test, p1, p2, p3, p4, reps)
    print(f"  NumPy   : I = {I_np:.10f}  |  erreur = {calcul_erreur(I_np, I_exact):.3e}  |  temps = {t_np*1e6:.1f} µs")

    # ── Données convergence & temps ────────────────────────────
    err_py    = convergence_python(a, b, liste_n, p1, p2, p3, p4)
    err_np    = convergence_numpy( a, b, liste_n, p1, p2, p3, p4)
    t_list_py = [temps_python(a, b, n, p1, p2, p3, p4, reps) for n in liste_n]
    t_list_np = [temps_numpy( a, b, n, p1, p2, p3, p4, reps) for n in liste_n]

    # ── Figures §2.3 : cumul avec §2.1 + §2.2 ─────────────────
    print()
    nouvelles_conv = [
        {"label": "Simp. Python", "methode": "Simpson", "impl": "Python", "erreurs": err_py},
        {"label": "Simp. NumPy",  "methode": "Simpson", "impl": "NumPy",  "erreurs": err_np},
    ]
    nouvelles_temps = [
        {"label": "Simp. Python", "methode": "Simpson", "impl": "Python", "temps": t_list_py},
        {"label": "Simp. NumPy",  "methode": "Simpson", "impl": "NumPy",  "temps": t_list_np},
    ]

    series_conv  = donnees_precedentes["series_conv"]  + nouvelles_conv
    series_temps = donnees_precedentes["series_temps"] + nouvelles_temps

    figures.fig_convergence(liste_n, series_conv,
                            titre="§2.1 + §2.2 + §2.3 — Convergence",
                            nom_fichier="fig_convergence.png")
    figures.fig_temps(liste_n, series_temps,
                      titre="§2.1 + §2.2 + §2.3 — Temps de calcul",
                      nom_fichier="fig_temps.png")

    print("\n✓ §2.3 terminé.\n")

    return {
        "I_exact"      : I_exact,
        "series_conv"  : series_conv,
        "series_temps" : series_temps,
        "erreurs_ponctuelles": donnees_precedentes["erreurs_ponctuelles"] + [
            {"label": "Simp.\nPython", "erreur": calcul_erreur(I_py, I_exact)},
            {"label": "Simp.\nNumPy",  "erreur": calcul_erreur(I_np, I_exact)},
        ],
    }

