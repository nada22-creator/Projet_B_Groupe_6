"""
main.py
=======
Point d'entrée — Mini-Projet B : Intégration Numérique.
MGA 802 — Introduction à la programmation avec Python

Ce fichier ne contient aucun calcul ni aucun tracé.
Il définit les paramètres globaux et orchestre l'exécution
en appelant le run() de chaque script de méthode dans l'ordre.

Chaîne d'exécution
-------------------
    rectangles.run()
        → retourne donnees_v1
    trapezes.run(donnees_v1)
        → retourne donnees_v2
    simpson.run(donnees_v2)
        → retourne donnees_v3
    preprogramme.run(donnees_v3)
        → génère toutes les figures finales §2.5
"""

import rectangles
import trapezes
import simpson
import preprogramme

# ── Paramètres globaux ────────────────────────────────────────
PARAMS = {
    "a"     : -2.0,
    "b"     :  3.0,
    "p1"    :  1.0,
    "p2"    : -2.0,
    "p3"    :  0.5,
    "p4"    :  0.3,
    "n_test":  100,
}
LISTE_N = [5, 10, 20, 50, 100, 200, 500, 1000, 5000]
REPS    = 300

# ── Exécution dans l'ordre ────────────────────────────────────
donnees = rectangles.run(PARAMS, LISTE_N, REPS)
donnees = trapezes.run(PARAMS, LISTE_N, donnees, REPS)
donnees = simpson.run(PARAMS, LISTE_N, donnees, REPS)
preprogramme.run(PARAMS, LISTE_N, donnees, REPS)

