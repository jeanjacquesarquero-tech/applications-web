# --- Données du problème ---
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

BUDGET_TOTAL_MAX = 8500
POIDS_MAX_EQUIPE = 250
SCORE_PULP = 536.0

def glouton_complet(critere):
    # Définition du tri selon la stratégie
    if critere == "score":
        tri = lambda x: x["score"]
    elif critere == "ratio_salaire":
        tri = lambda x: x["score"] / x["salaire"]
    elif critere == "ratio_poids":
        tri = lambda x: x["score"] / x["poids"]
    
    joueurs_tries = sorted(joueurs, key=tri, reverse=True)
    
    eq_a, eq_b = [], []
    budget_restant = BUDGET_TOTAL_MAX
    disponibles = joueurs_tries.copy()

    # Remplissage Équipe A (3 joueurs)
    for j in disponibles[:]:
        if len(eq_a) < 3:
            poids_actuel = sum(p["poids"] for p in eq_a)
            if poids_actuel + j["poids"] <= POIDS_MAX_EQUIPE and j["salaire"] <= budget_restant:
                eq_a.append(j)
                budget_restant -= j["salaire"]
                disponibles.remove(j)

    # Remplissage Équipe B (3 joueurs)
    for j in disponibles[:]:
        if len(eq_b) < 3:
            poids_actuel = sum(p["poids"] for p in eq_b)
            if poids_actuel + j["poids"] <= POIDS_MAX_EQUIPE and j["salaire"] <= budget_restant:
                eq_b.append(j)
                budget_restant -= j["salaire"]
                disponibles.remove(j)

    score_total = sum(j["score"] for j in eq_a + eq_b)
    budget_use = BUDGET_TOTAL_MAX - budget_restant
    return score_total, budget_use

# Calculs
res_score = glouton_complet("score")
res_ratio_s = glouton_complet("ratio_salaire")
res_ratio_p = glouton_complet("ratio_poids")

# Affichage du Tableau Comparatif
print(f"{'Stratégie':<25} | {'Score':<7} | {'Budget':<8} | {'Écart Pts':<10} | {'Écart %':<8}")
print("-" * 75)

for nom, res in [("Meilleur Score", res_score), ("Ratio Score/Salaire", res_ratio_s), ("Ratio Score/Poids", res_ratio_p)]:
    score, budget = res
    ecart_pts = SCORE_PULP - score
    ecart_per = (ecart_pts / SCORE_PULP) * 100
    print(f"{nom:<25} | {score:<7} | {budget:<8} | {ecart_pts:<10.1f} | {ecart_per:<8.2f}%")