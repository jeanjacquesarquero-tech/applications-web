import pulp

# 1. Données du problème 
joueurs = [
    {"nom": "Alice",  "score": 88, "salaire": 1200, "poids": 72},
    {"nom": "Bob",    "score": 91, "salaire": 1800, "poids": 85},
    {"nom": "Clara",  "score": 84, "salaire":  950, "poids": 68},
    {"nom": "David",  "score": 93, "salaire": 2100, "poids": 90},
    {"nom": "Emma",   "score": 79, "salaire":  800, "poids": 65},
    {"nom": "Frank",  "score": 87, "salaire": 2400, "poids": 95},
    {"nom": "Grace",  "score": 85, "salaire": 1050, "poids": 70},
    {"nom": "Hugo",   "score": 89, "salaire": 1600, "poids": 80},
]

# Paramètres de la ligue
BUDGET_TOTAL_MAX = 8500
POIDS_MAX_EQUIPE = 250
NB_JOUEURS_PAR_EQUIPE = 3

# 2. Création du problème
prob = pulp.LpProblem("Optimisation_Equipes_Basket", pulp.LpMaximize)

# 3. Variables de décision (Binaire: 1 si choisi, 0 sinon)
# Créons deux variables par joueur: une pour l'Équipe A y otra pour l'Équipe B
equipe_A = pulp.LpVariable.dicts("Eq_A", [j["nom"] for j in joueurs], cat='Binary')
equipe_B = pulp.LpVariable.dicts("Eq_B", [j["nom"] for j in joueurs], cat='Binary')

# 4. Fonction Objectif (Maximiser le score total des deux équipes)
prob += pulp.lpSum([j["score"] * (equipe_A[j["nom"]] + equipe_B[j["nom"]]) for j in joueurs])

# 5. Contraintes
# Chaque joueur peut être au maximum dans UNE seule équipe
for j in joueurs:
    prob += equipe_A[j["nom"]] + equipe_B[j["nom"]] <= 1

# Taille des équipes (exactement 3 joueurs par équipe)
prob += pulp.lpSum([equipe_A[j["nom"]] for j in joueurs]) == NB_JOUEURS_PAR_EQUIPE
prob += pulp.lpSum([equipe_B[j["nom"]] for j in joueurs]) == NB_JOUEURS_PAR_EQUIPE

# Budget total (La somme des salaires des deux équipes <= 8500)
prob += pulp.lpSum([j["salaire"] * (equipe_A[j["nom"]] + equipe_B[j["nom"]]) for j in joueurs]) <= BUDGET_TOTAL_MAX

# Poids par équipe (Chaque équipe <= 250 kg)
prob += pulp.lpSum([j["poids"] * equipe_A[j["nom"]] for j in joueurs]) <= POIDS_MAX_EQUIPE
prob += pulp.lpSum([j["poids"] * equipe_B[j["nom"]] for j in joueurs]) <= POIDS_MAX_EQUIPE

# 6. Résolution
prob.solve(pulp.PULP_CBC_CMD(msg=0))

# 7. Affichage des résultats
print(f"Statut: {pulp.LpStatus[prob.status]}")
print(f"Score Total Optimal: {pulp.value(prob.objective)}")

print("\n--- Équipe A ---")
for j in joueurs:
    if pulp.value(equipe_A[j["nom"]]) == 1:
        print(f"- {j['nom']} (Score: {j['score']}, Salaire: {j['salaire']}, Poids: {j['poids']})")

print("\n--- Équipe B ---")
for j in joueurs:
    if pulp.value(equipe_B[j["nom"]]) == 1:
        print(f"- {j['nom']} (Score: {j['score']}, Salaire: {j['salaire']}, Poids: {j['poids']})")