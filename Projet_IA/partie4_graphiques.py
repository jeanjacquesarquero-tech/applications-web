import matplotlib.pyplot as plt
import numpy as np

# 1. COMPARAISON DES ALGORITHMES (Barres) 
# Comparaison du score total obtenu par chaque approche
# Données basées sur les résultats : PuLP (524), Ratio (516), Meilleur Score (446)
scores_dict = {"Meilleur Score": 446, "Ratio Score/Salaire": 516, "PuLP": 524}

plt.figure(figsize=(8, 5))
# Création des barres avec les couleurs demandées
plt.bar(scores_dict.keys(), scores_dict.values(), color=['steelblue', 'salmon', 'green'])

# Ligne horizontale de référence pour le score optimal
plt.axhline(y=524, color='red', linestyle='--', label='Optimum (524 pts)')

plt.title("Comparaison des scores par approche")
plt.ylabel("Score Total")
plt.ylim(400, 550) # Ajustement de l'échelle pour mieux voir les différences
plt.legend()
plt.savefig('graph1_comparaison.png')
print("Graphique 1 (Comparaison) généré avec succès.")
plt.show()

# 2. CROISSANCE DU NOMBRE D'APPELS RÉCURSIFS 
# Analyse de l'efficacité entre fib_naif et fib_memo pour n de 1 à 25
n_range = range(1, 26) 

# Simulation du nombre d'appels (Exponentiel pour Naïf vs Linéaire pour Mémo)
appels_naif = [2 * (1.618**n) / 2.236 for n in n_range] 
appels_memo = [2 * n - 1 for n in n_range] 

plt.figure(figsize=(8, 5))
plt.plot(n_range, appels_naif, label='fib_naif', marker='o', color='red', markersize=4)
plt.plot(n_range, appels_memo, label='fib_memo', marker='s', color='blue', markersize=4)

# Utilisation d'une échelle logarithmique pour l'axe Y
plt.yscale('log')
plt.title("Nombre d'appels récursifs (Échelle Logarithmique)")
plt.xlabel("Valeur de n")
plt.ylabel("Nombre d'appels")
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.savefig('graph2_appels.png')
print("Graphique 2 (Appels récursifs) généré avec succès.")
plt.show()

#  3. RÉPARTITION DU BUDGET ET DU POIDS PAR ÉQUIPE
# Comparaison de l'utilisation des ressources (Equipe A vs Equipe B)
labels = ['Budget ($)', 'Poids (Kg)']
# Valeurs basées sur la sélection finale de PuLP
equipe_A = [4250, 242] 
equipe_B = [4250, 248]

x = np.arange(len(labels)) # Emplacement des étiquettes
width = 0.35 # Largeur des barres

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x - width/2, equipe_A, width, label='Équipe A', color='lightblue')
ax.bar(x + width/2, equipe_B, width, label='Équipe B', color='orange')

ax.set_title('Utilisation des ressources par équipe')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Ajout des lignes de contraintes maximales
ax.axhline(y=4250, color='r', linestyle='--', alpha=0.3, label='Limite Budget/Equipe')
ax.axhline(y=250, color='brown', linestyle='--', alpha=0.3, label='Limite Poids')

plt.savefig('graph3_repartition.png')
print("Graphique 3 (Répartition) généré avec succès.")
plt.show()