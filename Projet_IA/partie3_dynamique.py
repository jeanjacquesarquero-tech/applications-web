# --- Données du problème ---
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

# Table pour stocker les résultats et éviter les calculs inutiles
memo = {}

def resoudre_sac_a_dos(i, budget_restant):
    # Cas de base : plus de joueurs ou plus de budget
    if i < 0 or budget_restant <= 0:
        return 0, []
    
    # Si le résultat est déjà en mémoire, on le retourne
    if (i, budget_restant) in memo:
        return memo[(i, budget_restant)]
    
    actuel = joueurs[i]
    
    # Option 1 : On ne choisit pas ce joueur
    score_sans, liste_sans = resoudre_sac_a_dos(i - 1, budget_restant)
    
    # Option 2 : On choisit ce joueur (si on peut se le payer)
    score_avec = -1
    if actuel['salaire'] <= budget_restant:
        s, l = resoudre_sac_a_dos(i - 1, budget_restant - actuel['salaire'])
        score_avec = actuel['score'] + s
        liste_avec = l + [actuel['nom']]
    
    # On compare les deux options pour garder la meilleure
    if score_avec > score_sans:
        resultat = (score_avec, liste_avec)
    else:
        resultat = (score_sans, liste_sans)
    
    # On garde en mémoire pour la suite
    memo[(i, budget_restant)] = resultat
    return resultat

# Lancement de l'algorithme
meilleur_score, equipe_ideale = resoudre_sac_a_dos(len(joueurs) - 1, budget_max)

print("--- RÉSULTAT OPTIMAL (PROGRAMMATION DYNAMIQUE) ---")
print(f"Équipe sélectionnée : {equipe_ideale}")
print(f"Score total : {meilleur_score}")