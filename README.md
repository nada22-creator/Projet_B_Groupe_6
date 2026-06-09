# MGA802 — Mini-Projet B — Équipe 6

## Intégration numérique et comparaison des méthodes

## 1. Description du programme

Ce projet consiste à développer un programme Python permettant de calculer l'intégrale d'un polynôme de degré trois à l'aide de différentes méthodes numériques.

Le programme permet de :

- Calculer la solution analytique de référence ;
- Appliquer la méthode des rectangles ;
- Appliquer la méthode des trapèzes ;
- Appliquer la méthode de Simpson ;
- Utiliser des fonctions préprogrammées ;
- Comparer les erreurs obtenues ;
- Comparer les temps d'exécution ;
- Générer des graphiques de convergence et de performance.

---

## 2. Fonctionnalités du programme

### Solution analytique

Calcule la valeur exacte de l'intégrale du polynôme.

Exemple :

```python
calcul_solution_analytique(a, b, p1, p2, p3, p4)
```

### Méthode des rectangles

Approxime l'aire sous la courbe à l'aide d'une somme de rectangles.

Versions disponibles :

- Python de base
- NumPy

### Méthode des trapèzes

Approxime la courbe par des segments de droite et calcule l'aire à l'aide de trapèzes.

Versions disponibles :

- Python de base
- NumPy
- Préprogrammée (SciPy)

### Méthode de Simpson

Approxime la courbe à l'aide de paraboles afin d'améliorer la précision.

Versions disponibles :

- Python de base
- NumPy
- Préprogrammée (SciPy)

### Analyse des performances

Le programme mesure automatiquement :

- le temps d'exécution ;
- l'erreur par rapport à la solution exacte ;
- la convergence des méthodes.

---

## 3. Installation

### Prérequis

Installer Python 3.12 ou une version plus récente.

Installer les bibliothèques nécessaires :

```bash
pip install numpy
pip install matplotlib
pip install scipy
```

### Vérification

```bash
python --version
```

---

## 4. Exécution du programme

Ouvrir un terminal dans le dossier du projet puis exécuter :

```bash
python main.py
```

Le programme :

- calcule la solution analytique ;
- exécute les différentes méthodes numériques ;
- mesure les temps d'exécution ;
- calcule les erreurs ;
- affiche les graphiques.

---

## 5. Structure du projet

```text
Projet_B_Groupe_6/
│
├── main.py
├── integration_numerique.py
├── methode_rectangles.py
├── methodes_trapezes.py
├── methodes_preprogrammees_trapezes.py
├── methodes_simpson.py
├── methode_simpson_preprog.py
├── Graphiques.py
├── README.md
```

---

## 6. Choix de conception

### Utilisation de modules

Le projet est divisé en plusieurs modules afin de :

- améliorer la lisibilité du code ;
- faciliter la maintenance ;
- permettre la réutilisation des fonctions ;
- simplifier les tests.

### Utilisation de NumPy

NumPy est utilisé pour effectuer des calculs vectorisés et comparer les performances avec les implémentations Python de base.

### Utilisation de SciPy

SciPy est utilisé pour comparer les implémentations développées avec des méthodes préprogrammées reconnues.

### Mesure des performances

Les temps d'exécution sont mesurés à l'aide du module `timeit`.

### Visualisation des résultats

Les graphiques sont générés avec Matplotlib afin d'observer :

- la convergence des méthodes ;
- l'évolution de l'erreur ;
- les temps d'exécution ;
- la surface 3D du polynôme.

---

## 7. Technologies utilisées

- Python 3
- NumPy
- SciPy
- Matplotlib
- timeit

---

## 8. Auteurs

Projet réalisé par :

- Asma Brik
- Brahim Rezgui
- Nada Chaouachi

---

## 9. Références

Documentation officielle Python :  
https://docs.python.org/3/

Documentation NumPy :  
https://numpy.org/doc/stable/

Documentation SciPy :  
https://docs.scipy.org/doc/scipy/

Documentation Matplotlib :  
https://matplotlib.org/stable/

Documentation timeit :  
https://docs.python.org/3/library/timeit.html
