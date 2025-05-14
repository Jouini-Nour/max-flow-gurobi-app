# 🌐 Application Web - Problème de Flot Maximum avec Gurobi

Ce projet est une application web interactive qui permet de résoudre dynamiquement un problème de flot maximum sur un graphe orienté, en utilisant le solveur d’optimisation **Gurobi**, et de visualiser les résultats avec **matplotlib**.

---

## 📌 Fonctionnalités

- Entrée des données du graphe (nœuds, arcs, capacités) via interface web
- Résolution du problème de flot maximum avec Gurobi
- Visualisation du graphe avec arcs saturés colorés en rouge
- Génération d’un rapport LaTeX contenant la modélisation, les résultats, et un guide d’utilisation

---

## 🛠️ Technologies utilisées

- [Python](https://www.python.org/)
- [Gurobi Optimizer](https://www.gurobi.com/)
- [NetworkX](https://networkx.org/)
- [Matplotlib](https://matplotlib.org/)
- [Streamlit](https://streamlit.io/)
- [LaTeX](https://www.latex-project.org/) pour le rapport

---

## 🚀 Installation

### 1. Cloner le répôt

```bash
git clone https://github.com/Jouini-Nour/max-flow-gurobi-app.git
cd max-flow-gurobi-app
```
### 2. Installer les dépendances

Crée un environnement virtuel si nécessaire, puis :
```bash
pip install -r requirements.txt
```

### 3. Lancer l'application
```bash
streamlit run app.py
```
---
## 📄 Exemple d’utilisation

Entrer les nœuds : A,B,C,D

Définir le nœud source et puits : A → D

Ajouter les arcs : 
* A,B,10, 
* B,C,5, 
* C,D,7, ...

Visualisation instantanée du graphe + résultat du flot

---
## 📘 Rapport
Le rapport complet est inclus et contient :

* La modélisation mathématique

* Les choix technologiques

* Un guide utilisateur

* Une illustration graphique


---
## 📜 Licence
Ce projet est distribué sous licence MIT.

