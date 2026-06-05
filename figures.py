"""
figures.py
==========
Module de génération des figures — Mini-Projet B.
MGA 802 — Introduction à la programmation avec Python

Ce module ne fait QUE tracer et sauvegarder les figures.
Toutes les données (erreurs, temps) lui sont passées en argument.
Le main.py calcule les données et appelle ces fonctions.

Fonctions
---------
- fig_illustration_rectangles(A, B, n_liste, p1, p2, p3, p4)
- fig_convergence(liste_n, series, titre, nom_fichier)
- fig_temps(liste_n, series, titre, nom_fichier)
- fig_erreur_barres(labels, erreurs, n_ref, nom_fichier)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# ─────────────────────────────────────────────────────────────
# Palette & styles communs
# ─────────────────────────────────────────────────────────────
COULEURS = {
    "Rectangles" : "#2196F3",
    "Trapèzes"   : "#FF9800",
    "Simpson"    : "#4CAF50",
    "SciPy"      : "#9C27B0",
}
STYLES = {
    "Python" : ("-",  "o"),
    "NumPy"  : ("--", "s"),
    "SciPy"  : (":",  "^"),
}


def _style(impl):
    """Retourne (linestyle, marker) selon l'implémentation."""
    return STYLES.get(impl, ("-", "o"))


# ─────────────────────────────────────────────────────────────
# 1.  ILLUSTRATION MÉTHODE DES RECTANGLES
# ─────────────────────────────────────────────────────────────

def fig_illustration_rectangles(A, B, n_liste, p1, p2, p3, p4,
                                  nom_fichier="fig_rectangles_illustration.png"):
    """
    Trace la courbe f(x) et les rectangles pour plusieurs valeurs de n.

    Paramètres
    ----------
    A, B         : float       Bornes d'intégration.
    n_liste      : list[int]   Valeurs de n à illustrer (ex: [15, 50, 500]).
    p1,p2,p3,p4  : float       Coefficients du polynôme.
    nom_fichier  : str         Nom du fichier PNG de sortie.
    """
    from rectangles import polynome

    fig, axes = plt.subplots(1, len(n_liste), figsize=(5*len(n_liste), 4.5), sharey=True)
    fig.patch.set_facecolor("#f8f9fa")

    if len(n_liste) == 1:
        axes = [axes]

    for ax, n in zip(axes, n_liste):
        x_courbe = np.linspace(A, B, 500)
        y_courbe = polynome(x_courbe, p1, p2, p3, p4)
        h = (B - A) / n

        for i in range(n):
            xg = A + i * h
            xm = xg + h / 2
            ym = polynome(xm, p1, p2, p3, p4)
            couleur = "#ef9a9a" if ym >= 0 else "#90caf9"
            ec      = "#c62828" if ym >= 0 else "#1565c0"
            ax.add_patch(patches.Rectangle(
                (xg, min(0, ym)), h, abs(ym),
                lw=0.3 if n > 50 else 0.8,
                edgecolor=ec, facecolor=couleur, alpha=0.7
            ))

        ax.plot(x_courbe, y_courbe, "k-", lw=2, zorder=5, label="f(x)")
        ax.axhline(0, color="gray", lw=0.6)
        ax.set_title(f"n = {n}", fontsize=13, fontweight="bold")
        ax.set_xlabel("x")
        ax.set_xlim(A, B)
        ax.set_ylim(min(y_courbe) - 2, max(y_courbe) + 2)
        ax.grid(True, alpha=0.3)
        ax.set_facecolor("white")

    axes[0].set_ylabel("f(x)")
    fig.suptitle("Illustration — Méthode des rectangles",
                 fontsize=14, fontweight="bold", y=1.01)
    fig.tight_layout()
    fig.savefig(nom_fichier, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  → {nom_fichier}")


# ─────────────────────────────────────────────────────────────
# 2.  COURBE DE CONVERGENCE (erreur vs n)
# ─────────────────────────────────────────────────────────────

def fig_convergence(liste_n, series, titre="Convergence",
                    nom_fichier="fig_convergence.png"):
    """
    Trace l'erreur absolue en fonction du nombre de segments (log-log).

    Paramètres
    ----------
    liste_n     : list[int]
        Valeurs de n (axe X).
    series      : list[dict]
        Chaque élément est un dict avec les clés :
          - "label"   : str          ex: "Rectangles Python"
          - "methode" : str          ex: "Rectangles"  (pour la couleur)
          - "impl"    : str          ex: "Python"      (pour le style)
          - "erreurs" : list[float]  valeurs d'erreur
    titre       : str
    nom_fichier : str

    Exemple d'appel depuis main.py
    --------------------------------
    series = [
        {"label": "Rect. Python", "methode": "Rectangles", "impl": "Python", "erreurs": err_rect_py},
        {"label": "Rect. NumPy",  "methode": "Rectangles", "impl": "NumPy",  "erreurs": err_rect_np},
        ...
    ]
    figures.fig_convergence(LISTE_N, series, "Convergence §2.1", "fig_convergence.png")
    """
    fig, ax = plt.subplots(figsize=(9, 5))
    fig.patch.set_facecolor("#f8f9fa")
    ax.set_facecolor("white")

    for s in series:
        ls, mk = _style(s["impl"])
        couleur = COULEURS.get(s["methode"], "#607D8B")
        safe = [max(e, 1e-17) for e in s["erreurs"]]
        ax.loglog(liste_n, safe, ls + mk,
                  color=couleur, linewidth=2, markersize=6,
                  label=s["label"],
                  alpha=0.7 if s["impl"] != "Python" else 1.0)

    ax.set_xlabel("Nombre de segments n", fontsize=11)
    ax.set_ylabel("Erreur absolue", fontsize=11)
    ax.set_title(titre, fontsize=13, fontweight="bold")
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(True, which="both", linestyle="--", alpha=0.4)
    fig.tight_layout()
    fig.savefig(nom_fichier, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  → {nom_fichier}")


# ─────────────────────────────────────────────────────────────
# 3.  TEMPS DE CALCUL (temps vs n)
# ─────────────────────────────────────────────────────────────

def fig_temps(liste_n, series, titre="Temps de calcul",
              nom_fichier="fig_temps.png"):
    """
    Trace le temps moyen d'exécution en fonction du nombre de segments (log-log).

    Paramètres
    ----------
    liste_n     : list[int]
    series      : list[dict]
        Même structure que fig_convergence(), mais la clé "erreurs"
        est remplacée par "temps" (valeurs en secondes).
    titre       : str
    nom_fichier : str

    Exemple d'appel depuis main.py
    --------------------------------
    series = [
        {"label": "Rect. Python", "methode": "Rectangles", "impl": "Python", "temps": t_rect_py},
        ...
    ]
    figures.fig_temps(LISTE_N, series, "Temps §2.1", "fig_temps.png")
    """
    fig, ax = plt.subplots(figsize=(9, 5))
    fig.patch.set_facecolor("#f8f9fa")
    ax.set_facecolor("white")

    for s in series:
        ls, mk = _style(s["impl"])
        couleur = COULEURS.get(s["methode"], "#607D8B")
        ax.loglog(liste_n, [t * 1e6 for t in s["temps"]],
                  ls + mk, color=couleur, linewidth=2, markersize=6,
                  label=s["label"],
                  alpha=0.7 if s["impl"] != "Python" else 1.0)

    ax.set_xlabel("Nombre de segments n", fontsize=11)
    ax.set_ylabel("Temps moyen (µs)", fontsize=11)
    ax.set_title(titre, fontsize=13, fontweight="bold")
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(True, which="both", linestyle="--", alpha=0.4)
    fig.tight_layout()
    fig.savefig(nom_fichier, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  → {nom_fichier}")


# ─────────────────────────────────────────────────────────────
# 4.  COMPARAISON DES ERREURS PAR MÉTHODE (barres)
# ─────────────────────────────────────────────────────────────

def fig_erreur_barres(labels, erreurs, n_ref,
                       nom_fichier="fig_erreur_methodes.png"):
    """
    Graphique en barres comparant l'erreur absolue de chaque méthode.

    Paramètres
    ----------
    labels      : list[str]    Noms des méthodes (ex: ["Rect. Python", ...]).
    erreurs     : list[float]  Erreur absolue correspondante.
    n_ref       : int          Valeur de n utilisée (pour le titre).
    nom_fichier : str

    Exemple d'appel depuis main.py
    --------------------------------
    figures.fig_erreur_barres(
        labels  = ["Rect. Python", "Rect. NumPy", "Trap. Python", ...],
        erreurs = [err_rp, err_rn, err_tp, ...],
        n_ref   = N_TEST
    )
    """
    # Association label → méthode pour la couleur
    def _couleur(label):
        l = label.lower()
        if "rect"   in l: return COULEURS["Rectangles"]
        if "trap"   in l: return COULEURS["Trapèzes"]
        if "simp"   in l: return COULEURS["Simpson"]
        if "scipy"  in l: return COULEURS["SciPy"]
        return "#607D8B"

    def _hatch(label):
        l = label.lower()
        if "numpy" in l: return "//"
        if "scipy" in l: return ".."
        return ""

    bar_colors = [_couleur(lb) for lb in labels]
    bar_hatch  = [_hatch(lb)  for lb in labels]

    fig, ax = plt.subplots(figsize=(12, 5))
    fig.patch.set_facecolor("#f8f9fa")
    ax.set_facecolor("white")

    bars = ax.bar(range(len(labels)),
                  [max(e, 1e-17) for e in erreurs],
                  color=bar_colors, hatch=bar_hatch,
                  edgecolor="white", linewidth=0.8, alpha=0.88)

    for bar, err in zip(bars, erreurs):
        label_txt = "≈ 0" if err < 1e-14 else f"{err:.1e}"
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() * 2.0,
                label_txt, ha="center", fontsize=8)

    ax.set_yscale("log")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel("Erreur absolue (échelle log)", fontsize=11)
    ax.set_title(f"Comparaison des erreurs par méthode — n = {n_ref}",
                 fontsize=13, fontweight="bold")
    ax.grid(axis="y", which="both", linestyle="--", alpha=0.4)

    # Séparateurs de groupes
    for xsep in [1.5, 4.5]:
        ax.axvline(xsep, color="gray", linestyle=":", lw=1, alpha=0.6)

    # Légende méthodes
    from matplotlib.patches import Patch
    legend_els = [Patch(facecolor=COULEURS[m], label=m) for m in COULEURS]
    ax.legend(handles=legend_els, title="Méthode", loc="upper right", fontsize=9)

    fig.tight_layout()
    fig.savefig(nom_fichier, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  → {nom_fichier}")

