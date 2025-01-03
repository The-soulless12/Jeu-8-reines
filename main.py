def afficher_matrice(matrice):
    for ligne in matrice:
        print(" ".join("🔴" if case == 1 else "⚪" for case in ligne))

def est_safe(echiquier, ligne, colonne, n):
    # On vérifie la colonne
    for i in range(ligne):
        if echiquier[i][colonne] == 1:
            return False

    # On vérifie la diagonale supérieure gauche
    for i, j in zip(range(ligne, -1, -1), range(colonne, -1, -1)):
        if echiquier[i][j] == 1:
            return False

    # On vérifie la diagonale supérieure droite
    for i, j in zip(range(ligne, -1, -1), range(colonne, n)):
        if echiquier[i][j] == 1:
            return False

    return True

def placer_reines(echiquier, ligne, n, solution_count):
    if ligne == n:
        solution_count[0] += 1
        print(f"Solution {solution_count[0]} :")
        afficher_matrice(echiquier)
        print()
        return

    for colonne in range(n):
        if est_safe(echiquier, ligne, colonne, n):
            # On place une reine sur echiquier
            echiquier[ligne][colonne] = 1
            
            # Appel récursif pour placer la reine sur la ligne suivante
            placer_reines(echiquier, ligne + 1, n, solution_count)
            
            # On retire la reine (backtracking)
            echiquier[ligne][colonne] = 0

def main():
    try:
        n = int(input("Entrez la taille de l'échiquier (n x n) : "))
        if n <= 0:
            raise ValueError("La taille doit être un entier positif.")
    except ValueError as e:
        print(f"Erreur : {e}")
        return
    
    echiquier = [[0 for _ in range(n)] for _ in range(n)]
    solution_count = [0]
    
    print("\nSolutions possibles :")
    placer_reines(echiquier, 0, n, solution_count)

if __name__ == "__main__":
    main()
