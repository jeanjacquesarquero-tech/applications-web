import time

# --- Données ---
joueurs = [
    {"nom": "Alice", "score": 88}, {"nom": "Bob", "score": 91},
    {"nom": "Clara", "score": 84}, {"nom": "David", "score": 93},
    {"nom": "Emma", "score": 79}, {"nom": "Frank", "score": 87},
    {"nom": "Grace", "score": 85}, {"nom": "Hugo", "score": 89}
]

# 1. Score Cumulé Récursif
def score_cumule(liste_joueurs, k):
    # Trier par score d'abord
    joueurs_tries = sorted(liste_joueurs, key=lambda x: x["score"], reverse=True)
    
    def recursif(n):
        if n <= 0:
            return 0
        current_score = joueurs_tries[n-1]["score"]
        total = current_score + recursif(n-1)
        print(f"Étape {n}: Ajout de {joueurs_tries[n-1]['nom']} (+{current_score}) -> Total: {total}")
        return total

    print(f"\nCalcul du score cumulé pour les {k} meilleurs joueurs:")
    return recursif(k)

# 2. Fibonacci Naïf vs Mémoïsé
# Scores des deux meilleurs (ex: David 93, Bob 91)
val1, val2 = 93, 91

def fib_naif(n):
    if n == 0: return val1
    if n == 1: return val2
    return fib_naif(n-1) + fib_naif(n-2)

memo = {}
def fib_memo(n):
    if n == 0: return val1
    if n == 1: return val2
    if n not in memo:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

# --- Tests de performance ---
n_test = 30 # 

start = time.time()
res_naif = fib_naif(n_test)
end = time.time()
print(f"\nFibonacci Naïf({n_test}): {res_naif} | Temps: {end-start:.4f}s")

start = time.time()
res_memo = fib_memo(n_test)
end = time.time()
print(f"Fibonacci Mémo({n_test}): {res_memo} | Temps: {end-start:.4f}s")

# Exécution de score_cumule
score_cumule(joueurs, 3)