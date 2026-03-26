import pulp

# 1. Données des joueurs (Base du projet)
joueurs = [
    {"nom": "Alice", "score": 88, "salaire": 1200},
    {"nom": "Bob", "score": 91, "salaire": 1800},
    {"nom": "Clara", "score": 84, "salaire": 950},
    {"nom": "David", "score": 93, "salaire": 2100},
    {"nom": "Emma", "score": 79, "salaire": 800},
    {"nom": "Frank", "score": 87, "salaire": 2400},
    {"nom": "Grace", "score": 85, "salaire": 1050},
    {"nom": "Hugo", "score": 89, "salaire": 1600},
]

budget_max = 5000

# 2. Création du problème d'optimisation (Maximiser le score total)
probleme = pulp.LpProblem("Selection_Joueurs_Basket", pulp.LpMaximize)

# 3. Variables de décision (1 si invité, 0 sinon)
# On crée un dictionnaire pour stocker les variables binaires
selection = {}
for j in joueurs:
    selection[j['nom']] = pulp.LpVariable(j['nom'], cat='Binary')

# 4. Fonction Objective : Maximiser la somme des scores
probleme += pulp.lpSum([selection[j['nom']] * j['score'] for j in joueurs])

# 5. Contrainte : La somme des salaires ne doit pas dépasser le budget
probleme += pulp.lpSum([selection[j['nom']] * j['salaire'] for j in joueurs]) <= budget_max

# 6. Résolution du problème
probleme.solve()

# 7. Affichage des résultats
print(f"Statut de la solution : {pulp.LpStatus[probleme.status]}")
print("Joueurs sélectionnés pour le tournoi :")

for j in joueurs:
    # Si la valeur est 1, le joueur est sélectionné
    if pulp.value(selection[j['nom']]) == 1:
        print(f"- {j['nom']} (Score: {j['score']}, Salaire: {j['salaire']})")

print(f"Poids total du talent (Score optimal) : {pulp.value(probleme.objective)}")