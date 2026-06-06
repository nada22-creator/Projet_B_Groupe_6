# ============================================================================
# MODULE : graphiques.py
# ============================================================================
# Contient uniquement les visualisations du projet :
#   - convergence
#   - temps d'exécution
#   - erreur
#   - surface 3D
# ============================================================================

import numpy as np
import matplotlib.pyplot as plt


# ============================================================================
# 1. CONVERGENCE
# ============================================================================
def tracer_convergence(n_values, erreurs_rect):
    """
    Montre l'évolution de l'erreur selon le nombre de segments.
    """

    plt.figure(figsize=(10,6))

    plt.plot(n_values, erreurs_rect, marker='o', label="Rectangles")

    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Erreur absolue")
    plt.title("Convergence - méthode des rectangles")

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.show()


# ============================================================================
# 2. TEMPS D'EXÉCUTION
# ============================================================================
def tracer_temps_execution(n_values, temps_python, temps_numpy):
    """
    Compare Python vs NumPy pour la méthode des rectangles.
    """

    plt.figure(figsize=(10,6))

    plt.plot(n_values, temps_python, marker='o', label="Python")
    plt.plot(n_values, temps_numpy, marker='s', label="NumPy")

    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Temps (s)")
    plt.title("Temps d'exécution - méthode des rectangles")

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.show()


# ============================================================================
# 3. ERREUR
# ============================================================================
def tracer_erreurs(n_values, erreurs_rect):
    """
    Erreur de la méthode des rectangles.
    """

    plt.figure(figsize=(10,6))

    plt.plot(n_values, erreurs_rect, marker='o', label="Rectangles")

    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Erreur")
    plt.title("Erreur - méthode des rectangles")

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.show()


# ============================================================================
# 4. SURFACE 3D
# ============================================================================

"""
Représenter graphiquement la fonction polynomiale f(x) en 3D
 afin  de mieux visualiser sa forme globale sur l’intervalle [a, b].
 """

def tracer_surface_polynome(a, b, p1, p2, p3, p4):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(a, b, 100)
    y = np.linspace(0, 1, 30)

    X, Y = np.meshgrid(x, y)

    Z = p1 + p2*X + p3*X**2 + p4*X**3

    ax.plot_surface(X, Y, Z, alpha=0.8)

    ax.set_title("Surface du polynôme")
    ax.set_xlabel("x")
    ax.set_ylabel("dimension fictive")
    ax.set_zlabel("f(x)")

    plt.show()