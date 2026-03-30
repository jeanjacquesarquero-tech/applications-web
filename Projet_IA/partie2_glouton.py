# --- Données des joueurs ---
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

# 1. Stratégie Meilleur Score Absolu
def strategie_score_absolu(liste):
    # On trie par score uniquement
    tries = sorted(liste, key=lambda x: x['score'], reverse=True)
    selection, cout, score = [], 0, 0
    for j in tries:
        if cout + j['salaire'] <= budget_max:
            selection.append(j['nom'])
            cout += j['salaire']
            score += j['score']
    print(f"\nStratégie A (Meilleur Score): \nSélection: {selection} \nScore: {score} | Coût: {cout}")

# 2. Stratégie Meilleur Ratio Score/Salaire
def strategie_ratio(liste):
    # On trie par le rapport qualité/prix
    tries = sorted(liste, key=lambda x: x['score']/x['salaire'], reverse=True)
    selection, cout, score = [], 0, 0
    for j in tries:
        if cout + j['salaire'] <= budget_max:
            selection.append(j['nom'])
            cout += j['salaire']
            score += j['score']
    print(f"\nStratégie B (Meilleur Ratio): \nSélection: {selection} \nScore: {score} | Coût: {cout}")

# 3. Stratégie Alternance Score/Ratio
def strategie_alternance(liste):
    selection, cout, score = [], 0, 0
    disponibles = liste.copy()
    tour_score = True # On alterne le critère à chaque choix
    
    while disponibles:
        if tour_score:
            disponibles.sort(key=lambda x: x['score'], reverse=True)
        else:
            disponibles.sort(key=lambda x: x['score']/x['salaire'], reverse=True)
        
        candidat = disponibles.pop(0)
        if cout + candidat['salaire'] <= budget_max:
            selection.append(candidat['nom'])
            cout += candidat['salaire']
            score += candidat['score']
            tour_score = not tour_score # On change de critère
            
    print(f"\nStratégie C (Alternance): \nSélection: {selection} \nScore: {score} | Coût: {cout}")

# --- Exécution des 3 stratégies ---
strategie_score_absolu(joueurs)
strategie_ratio(joueurs)
strategie_alternance(joueurs)