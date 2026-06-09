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
def tracer_convergence(n_values, erreurs_rect, erreurs_simp, erreurs_trap, erreurs_trap_preprog):
    plt.figure(figsize=(10,6))

    plt.plot(n_values, erreurs_rect, marker='o', label="Rectangles")
    plt.plot(n_values, erreurs_simp, marker='s', label="Simpson")
    plt.plot(n_values, erreurs_trap, marker='^',label="Trapèzes Python")
    plt.plot(n_values, erreurs_trap_preprog,marker='d',label="Trapèzes Préprogrammée")

    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Erreur absolue")
    plt.title("Convergence - Rectangles vs Simpson VS Trapeze")

    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# ============================================================================
# 2. TEMPS D'EXÉCUTION
# ============================================================================
def tracer_temps_execution(n_values, temps_python, temps_numpy, temps_simpson_python, temps_simpson_numpy,    temps_trap_python,
    temps_trap_numpy,
    temps_trap_preprog):

    plt.figure(figsize=(10,6))

    plt.plot(n_values, temps_python, marker='o', label="Rectangles Python")
    plt.plot(n_values, temps_numpy, marker='s', label="Rectangles NumPy")
    plt.plot(n_values, temps_simpson_python, marker='^', label="Simpson Python")
    plt.plot(n_values, temps_simpson_numpy, marker='x', label="Simpson NumPy")
    plt.plot(n_values, temps_trap_python, marker='d',label="Trapèzes Python")

    plt.plot(n_values, temps_trap_numpy,marker='v',label="Trapèzes NumPy")

    plt.plot(n_values, temps_trap_preprog, marker='P', label="Trapèzes Préprogrammée")

    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Temps (s)")
    plt.title("Temps d'exécution - Rectangles vs Simpson VS Trapeze")

    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# ============================================================================
# 3. ERREUR
# ============================================================================
def tracer_erreurs(n_values, erreurs_rect, erreurs_simp, erreurs_trapeze,
        erreurs_trap_preprog):
    plt.figure(figsize=(10,6))


    plt.plot(n_values, erreurs_rect, marker='o', label="Rectangles")
    plt.plot(n_values, erreurs_simp, marker='s', label="Simpson")
    plt.plot(n_values, erreurs_trapeze, marker='^', label="Trapèzes")
    plt.plot(n_values, erreurs_trap_preprog, marker='x', label="Trapèzes préprogrammée")


    plt.xlabel("Nombre de segments (n)")
    plt.ylabel("Erreur")
    plt.title("Erreur - Rectangles vs Simpson VS Trapeze")

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

def tracer_tableau_bord(n_values, erreurs_rect, temps_python, temps_numpy, a, b, p1, p2, p3, p4):
    """
    Regroupe toutes les figures sur un seul et même tableau de bord (2x2).
    """
    fig = plt.figure(figsize=(15, 10))

    # 1. Convergence / Erreur
    ax1 = fig.add_subplot(221)
    ax1.plot(n_values, erreurs_rect, marker='o', color='blue', label="Rectangles")
    ax1.set_xlabel("Nombre de segments (n)")
    ax1.set_ylabel("Erreur absolue")
    ax1.set_title("Convergence & Erreurs")
    ax1.grid(True)
    ax1.legend()

    # 2. Temps d'exécution
    ax2 = fig.add_subplot(222)
    ax2.plot(n_values, temps_python, marker='o', label="Python de base")
    ax2.plot(n_values, temps_numpy, marker='s', label="NumPy")
    ax2.set_xlabel("Nombre de segments (n)")
    ax2.set_ylabel("Temps (s)")
    ax2.set_title("Comparaison des temps d'exécution")
    ax2.grid(True)
    ax2.legend()

    # 3. Surface 3D du polynôme
    ax3 = fig.add_subplot(212, projection='3d')  # Prend toute la ligne du bas
    x = np.linspace(a, b, 100)
    y = np.linspace(0, 1, 30)
    X, Y = np.meshgrid(x, y)
    Z = p1 + p2 * X + p3 * X ** 2 + p4 * X ** 3
    surf = ax3.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax3.set_title("Surface du polynôme f(x)")
    ax3.set_xlabel("x")
    ax3.set_ylabel("y (fictif)")
    ax3.set_zlabel("f(x)")
    fig.colorbar(surf, ax=ax3, shrink=0.5, aspect=5)

    plt.tight_layout()
    plt.show()  # Un seul point de blocage à la toute fin