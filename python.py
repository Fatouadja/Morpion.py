import random

def afficher_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * len(ligne) * 3)

def creer_grille(taille):
    return [[" " for _ in range(taille)] for _ in range(taille)]

def poser_pion(grille, ligne, colonne, symbole):
    if grille[ligne][colonne] == " ":
        grille[ligne][colonne] = symbole
        return True
    else:
        return False

def ligne_gagnante(grille, symbole):
    for ligne in grille:
        if all(cellule == symbole for cellule in ligne):
            return True
    return False

def colonne_gagnante(grille, symbole):
    taille = len(grille)
    for j in range(taille):
        if all(grille[i][j] == symbole for i in range(taille)):
            return True
    return False

def diagonale_gagnante(grille, symbole):
    taille = len(grille)
    if all(grille[i][i] == symbole for i in range(taille)) or \
            all(grille[i][taille - i - 1] == symbole for i in range(taille)):
        return True
    return False

def grille_pleine(grille):
    for ligne in grille:
        if " " in ligne:
            return False
    return True

def adversaire_aleatoire(grille, symbole):
    while True:
        ligne = random.randint(0, len(grille) - 1)
        colonne = random.randint(0, len(grille) - 1)
        if poser_pion(grille, ligne, colonne, symbole):
            break

def jouer():
    taille = 3  # Taille fixe de la grille pour une version plus simple
    grille = creer_grille(taille)
    symboles = ["X", "O"]
    tour = 0

    while True:
        afficher_grille(grille)
        symbole = symboles[tour % 2]
        print("C'est au tour de", symbole)

        if symbole == "X":
            ligne = int(input("Entrez le numéro de ligne : "))
            colonne = int(input("Entrez le numéro de colonne : "))
            if not poser_pion(grille, ligne, colonne, symbole):
                print("Position invalide, réessayez.")
                continue
        else:
            adversaire_aleatoire(grille, symbole)

        if ligne_gagnante(grille, symbole) or \
                colonne_gagnante(grille, symbole) or \
                diagonale_gagnante(grille, symbole):
            afficher_grille(grille)
            print("Le joueur", symbole, "a gagné !")
            break
        elif grille_pleine(grille):
            afficher_grille(grille)
            print("Match nul !")
            break

        tour += 1

if __name__ == "__main__":
    jouer()
