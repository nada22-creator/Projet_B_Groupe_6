"""
preprogramme.py
===============
§2.4 — Méthodes pré-programmées SciPy (trapezoid + simpson).
MGA 802 — Mini-Projet B

Ce script expose une fonction run() qui :
  1. Utilise scipy.integrate.trapezoid et scipy.integrate.simpson
  2. Produit les figures FINALES complètes §2.5 (toutes méthodes)
  3. C'est le dernier script de la chaîne, ne retourne rien
"""

import timeit
import numpy as np
from scipy import integrate
import figures
from rectangles import polynome, solution_analytique, calcul_erreur


# ─────────────────────────────────────────────────────────────
# Trapèzes — SciPy
# ─────────────────────────────────────────────────────────────

def trapezes_scipy(a, b, n, p1, p2, p3, p4):
    """
    Intégration par trapèzes via scipy.integrate.trapezoid.

    Construit le tableau de points (x, y) avec NumPy et
    délègue le calcul à SciPy.
    """
    x = np.linspace(a, b, n + 1)
    y = polynome(x, p1, p2, p3, p4)
    return float(integrate.trapezoid(y, x))


def erreur_trapezes_scipy(a, b, n, p1, p2, p3, p4):
    """Retourne l'erreur absolue pour n segments (SciPy trapèzes)."""
    return calcul_erreur(
        trapezes_scipy(a, b, n, p1, p2, p3, p4),
        solution_analytique(a, b, p1, p2, p3, p4)
    )


def convergence_trapezes_scipy(a, b, liste_n, p1, p2, p3, p4):
    """Calcule l'erreur pour chaque n de liste_n."""
    return [erreur_trapezes_scipy(a, b, n, p1, p2, p3, p4) for n in liste_n]


def temps_trapezes_scipy(a, b, n, p1, p2, p3, p4, repetitions=300):
    """Mesure le temps moyen via timeit."""
    return timeit.timeit(
        lambda: trapezes_scipy(a, b, n, p1, p2, p3, p4),
        number=repetitions
    ) / repetitions


# ─────────────────────────────────────────────────────────────
# Simpson — SciPy
# ─────────────────────────────────────────────────────────────

def simpson_scipy(a, b, n, p1, p2, p3, p4):
    """
    Intégration par Simpson via scipy.integrate.simpson.

    scipy.integrate.simpson requiert un nombre impair de points
    (n pair). Si n est impair, on l'incrémente de 1.
    """
    if n % 2 != 0:
        n += 1
    x = np.linspace(a, b, n + 1)
    y = polynome(x, p1, p2, p3, p4)
    return float(integrate.simpson(y, x=x))


def erreur_simpson_scipy(a, b, n, p1, p2, p3, p4):
    """Retourne l'erreur absolue pour n segments (SciPy Simpson)."""
    return calcul_erreur(
        simpson_scipy(a, b, n, p1, p2, p3, p4),
        solution_analytique(a, b, p1, p2, p3, p4)
    )


def convergence_simpson_scipy(a, b, liste_n, p1, p2, p3, p4):
    """Calcule l'erreur pour chaque n de liste_n."""
    return [erreur_simpson_scipy(a, b, n, p1, p2, p3, p4) for n in liste_n]


def temps_simpson_scipy(a, b, n, p1, p2, p3, p4, repetitions=300):
    """Mesure le temps moyen via timeit."""
    return timeit.timeit(
        lambda: simpson_scipy(a, b, n, p1, p2, p3, p4),
        number=repetitions
    ) / repetitions


# ─────────────────────────────────────────────────────────────
# run() — point d'entrée appelé par main.py
# ─────────────────────────────────────────────────────────────

def run(params, liste_n, donnees_precedentes, reps=300):
    """
    Exécute §2.4 + §2.5 : calculs SciPy + figures FINALES complètes.

    C'est le dernier maillon de la chaîne. Il génère les figures
    définitives avec toutes les méthodes (§2.5 résumé).

    Paramètres
    ----------
    params              : dict  a, b, p1, p2, p3, p4, n_test
    liste_n             : list  Grille de n pour les graphiques
    donnees_precedentes : dict  Retour de simpson.run()
    reps                : int   Répétitions timeit
    """
    a, b   = params["a"], params["b"]
    p1, p2, p3, p4 = params["p1"], params["p2"], params["p3"], params["p4"]
    n_test  = params["n_test"]
    I_exact = donnees_precedentes["I_exact"]

    SEP = "=" * 65
    print(SEP)
    print("§ 2.4  Méthodes pré-programmées (SciPy)")
    print(SEP)

    # ── Calculs ponctuels ──────────────────────────────────────
    I_tsc = trapezes_scipy(a, b, n_test, p1, p2, p3, p4)
    t_tsc = temps_trapezes_scipy(a, b, n_test, p1, p2, p3, p4, reps)
    print(f"  Trap. SciPy  : I = {I_tsc:.10f}  |  erreur = {calcul_erreur(I_tsc, I_exact):.3e}  |  temps = {t_tsc*1e6:.1f} µs")

    I_ssc = simpson_scipy(a, b, n_test, p1, p2, p3, p4)
    t_ssc = temps_simpson_scipy(a, b, n_test, p1, p2, p3, p4, reps)
    print(f"  Simp. SciPy  : I = {I_ssc:.10f}  |  erreur = {calcul_erreur(I_ssc, I_exact):.3e}  |  temps = {t_ssc*1e6:.1f} µs")

    # ── Données convergence & temps ────────────────────────────
    err_tsc   = convergence_trapezes_scipy(a, b, liste_n, p1, p2, p3, p4)
    err_ssc   = convergence_simpson_scipy( a, b, liste_n, p1, p2, p3, p4)
    t_list_tsc = [temps_trapezes_scipy(a, b, n, p1, p2, p3, p4, reps) for n in liste_n]
    t_list_ssc = [temps_simpson_scipy( a, b, n, p1, p2, p3, p4, reps) for n in liste_n]

    # ── Figures §2.5 FINALES : toutes méthodes ────────────────
    print()
    print(SEP)
    print("§ 2.5  Figures finales — toutes méthodes")
    print(SEP)

    series_conv_finales = donnees_precedentes["series_conv"] + [
        {"label": "Trap. SciPy",  "methode": "SciPy", "impl": "SciPy", "erreurs": err_tsc},
        {"label": "Simp. SciPy",  "methode": "SciPy", "impl": "SciPy", "erreurs": err_ssc},
    ]
    series_temps_finales = donnees_precedentes["series_temps"] + [
        {"label": "Trap. SciPy",  "methode": "SciPy", "impl": "SciPy", "temps": t_list_tsc},
        {"label": "Simp. SciPy",  "methode": "SciPy", "impl": "SciPy", "temps": t_list_ssc},
    ]
    erreurs_ponctuelles = donnees_precedentes["erreurs_ponctuelles"] + [
        {"label": "Trap.\nSciPy", "erreur": calcul_erreur(I_tsc, I_exact)},
        {"label": "Simp.\nSciPy", "erreur": calcul_erreur(I_ssc, I_exact)},
    ]

    figures.fig_convergence(liste_n, series_conv_finales,
                            titre="§2.5 — Convergence : toutes méthodes",
                            nom_fichier="fig_convergence.png")

    figures.fig_temps(liste_n, series_temps_finales,
                      titre="§2.5 — Temps de calcul : toutes méthodes",
                      nom_fichier="fig_temps.png")

    figures.fig_erreur_barres(
        labels  = [d["label"]  for d in erreurs_ponctuelles],
        erreurs = [d["erreur"] for d in erreurs_ponctuelles],
        n_ref   = n_test
    )

    print("\n✓ §2.4 + §2.5 terminés.\n")

