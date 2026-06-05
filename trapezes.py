"""
trapezes.py
===========
§2.2 — Méthode des trapèzes (Python de base + NumPy).
MGA 802 — Mini-Projet B

Ce script expose une fonction run() qui :
  1. Calcule l'intégrale par trapèzes (Python + NumPy)
  2. Compare avec la méthode des rectangles (§2.2 exige cette comparaison)
  3. Met à jour les figures convergence + temps (cumul avec §2.1)
  4. Retourne un dict enrichi à passer aux scripts suivants
"""

import timeit
import numpy as np
import figures
from rectangles import polynome, solution_analytique, calcul_erreur


# ─────────────────────────────────────────────────────────────
# Méthode des trapèzes — Python de base
# ─────────────────────────────────────────────────────────────

def trapezes_python(a, b, n, p1, p2, p3, p4):
    """
    Intégration par la méthode des trapèzes — Python de base.

    Sur chaque segment [x_i, x_{i+1}] :
        T_i = h/2 * (f(x_i) + f(x_{i+1}))
    """
    h = (b - a) / n
    somme = 0.0
    for i in range(n):
        x_g = a + i * h
        x_d = a + (i + 1) * h
        somme += polynome(x_g, p1, p2, p3, p4) + polynome(x_d, p1, p2, p3, p4)
    return (h / 2) * somme


def erreur_trapezes_python(a, b, n, p1, p2, p3, p4):
    """Retourne l'erreur absolue pour n segments (Python)."""
    return calcul_erreur(
        trapezes_python(a, b, n, p1, p2, p3, p4),
        solution_analytique(a, b, p1, p2, p3, p4)
    )


def convergence_python(a, b, liste_n, p1, p2, p3, p4):
    """Calcule l'erreur pour chaque n de liste_n (Python)."""
    return [erreur_trapezes_python(a, b, n, p1, p2, p3, p4) for n in liste_n]


def temps_python(a, b, n, p1, p2, p3, p4, repetitions=300):
    """Mesure le temps moyen via timeit (Python)."""
    return timeit.timeit(
        lambda: trapezes_python(a, b, n, p1, p2, p3, p4),
        number=repetitions
    ) / repetitions


# ─────────────────────────────────────────────────────────────
# Méthode des trapèzes — NumPy vectorisé
# ─────────────────────────────────────────────────────────────

def trapezes_numpy(a, b, n, p1, p2, p3, p4):
    """
    Intégration par la méthode des trapèzes — NumPy vectorisé.

    Utilise np.trapz() sur les n+1 points uniformément espacés.
    """
    x = np.linspace(a, b, n + 1)
    y = polynome(x, p1, p2, p3, p4)
    return float(np.trapz(y, x))


def erreur_trapezes_numpy(a, b, n, p1, p2, p3, p4):
    """Retourne l'erreur absolue pour n segments (NumPy)."""
    return calcul_erreur(
        trapezes_numpy(a, b, n, p1, p2, p3, p4),
        solution_analytique(a, b, p1, p2, p3, p4)
    )


def convergence_numpy(a, b, liste_n, p1, p2, p3, p4):
    """Calcule l'erreur pour chaque n de liste_n (NumPy)."""
    return [erreur_trapezes_numpy(a, b, n, p1, p2, p3, p4) for n in liste_n]


def temps_numpy(a, b, n, p1, p2, p3, p4, repetitions=300):
    """Mesure le temps moyen via timeit (NumPy)."""
    return timeit.timeit(
        lambda: trapezes_numpy(a, b, n, p1, p2, p3, p4),
        number=repetitions
    ) / repetitions


# ─────────────────────────────────────────────────────────────
# run() — point d'entrée appelé par main.py
# ─────────────────────────────────────────────────────────────

def run(params, liste_n, donnees_precedentes, reps=300):
    """
    Exécute §2.2 : calculs + mise à jour des figures.

    Paramètres
    ----------
    params              : dict  a, b, p1, p2, p3, p4, n_test
    liste_n             : list  Grille de n pour les graphiques
    donnees_precedentes : dict  Retour de rectangles.run()
    reps                : int   Répétitions timeit

    Retourne
    --------
    dict : Données enrichies à passer aux scripts suivants.
    """
    a, b   = params["a"], params["b"]
    p1, p2, p3, p4 = params["p1"], params["p2"], params["p3"], params["p4"]
    n_test  = params["n_test"]
    I_exact = donnees_precedentes["I_exact"]

    SEP = "=" * 65
    print(SEP)
    print("§ 2.2  Méthode des Trapèzes")
    print(SEP)

    # ── Calculs ponctuels ──────────────────────────────────────
    I_py = trapezes_python(a, b, n_test, p1, p2, p3, p4)
    t_py = temps_python(a, b, n_test, p1, p2, p3, p4, reps)
    print(f"  Python  : I = {I_py:.10f}  |  erreur = {calcul_erreur(I_py, I_exact):.3e}  |  temps = {t_py*1e6:.1f} µs")

    I_np = trapezes_numpy(a, b, n_test, p1, p2, p3, p4)
    t_np = temps_numpy(a, b, n_test, p1, p2, p3, p4, reps)
    print(f"  NumPy   : I = {I_np:.10f}  |  erreur = {calcul_erreur(I_np, I_exact):.3e}  |  temps = {t_np*1e6:.1f} µs")

    # ── Données convergence & temps ────────────────────────────
    err_py    = convergence_python(a, b, liste_n, p1, p2, p3, p4)
    err_np    = convergence_numpy( a, b, liste_n, p1, p2, p3, p4)
    t_list_py = [temps_python(a, b, n, p1, p2, p3, p4, reps) for n in liste_n]
    t_list_np = [temps_numpy( a, b, n, p1, p2, p3, p4, reps) for n in liste_n]

    # ── Figures §2.2 : cumul avec §2.1 ────────────────────────
    print()
    nouvelles_conv = [
        {"label": "Trap. Python", "methode": "Trapèzes", "impl": "Python", "erreurs": err_py},
        {"label": "Trap. NumPy",  "methode": "Trapèzes", "impl": "NumPy",  "erreurs": err_np},
    ]
    nouvelles_temps = [
        {"label": "Trap. Python", "methode": "Trapèzes", "impl": "Python", "temps": t_list_py},
        {"label": "Trap. NumPy",  "methode": "Trapèzes", "impl": "NumPy",  "temps": t_list_np},
    ]

    series_conv  = donnees_precedentes["series_conv"]  + nouvelles_conv
    series_temps = donnees_precedentes["series_temps"] + nouvelles_temps

    figures.fig_convergence(liste_n, series_conv,
                            titre="§2.1 + §2.2 — Convergence",
                            nom_fichier="fig_convergence.png")
    figures.fig_temps(liste_n, series_temps,
                      titre="§2.1 + §2.2 — Temps de calcul",
                      nom_fichier="fig_temps.png")

    print("\n✓ §2.2 terminé.\n")

    return {
        "I_exact"      : I_exact,
        "series_conv"  : series_conv,
        "series_temps" : series_temps,
        "erreurs_ponctuelles": donnees_precedentes["erreurs_ponctuelles"] + [
            {"label": "Trap.\nPython", "erreur": calcul_erreur(I_py, I_exact)},
            {"label": "Trap.\nNumPy",  "erreur": calcul_erreur(I_np, I_exact)},
        ],
    }

