import random

def afficher_grille(grille):
    """
    Affiche la grille de jeu avec un cadre et des symboles en rouge.
    """
    taille = len(grille)
    
    # Afficher la ligne supérieure du cadre
    print("┌" + "───┬" * (taille - 1) + "───┐")

    for i, ligne in enumerate(grille):
        symboles = []
        for symbole in ligne:
            if symbole == "X":
                symboles.append("\033[91mX\033[0m")  # Rouge pour le symbole X
            elif symbole == "O":
                symboles.append("\033[91mO\033[0m")  # Rouge pour le symbole O
            else:
                symboles.append(symbole)
        print("│ " + " | ".join(symboles) + " │")

        # Afficher les lignes horizontales intermédiaires sauf pour la dernière ligne
        if i < taille - 1:
            print("├" + "───┼" * (taille - 1) + "───┤")
    
    # Afficher la ligne inférieure du cadre
    print("└" + "───┴" * (taille - 1) + "───┘")


def creer_grille(taille):
    """
    Crée une grille de jeu de la taille spécifiée.
    """
    return [["-" for _ in range(taille)] for _ in range(taille)]

def poser_pion(grille, ligne, colonne, symbole):
    """
    Pose un pion à l'emplacement spécifié s'il est vide.
    """
    if grille[ligne][colonne] == "-":
        grille[ligne][colonne] = symbole
        return True
    else:
        return False

def est_gagnant(grille, symbole):
    """
    Vérifie si le joueur avec le symbole spécifié a gagné.
    """
    taille = len(grille)
    for i in range(taille):
        if all(grille[i][j] == symbole for j in range(taille)) or \
           all(grille[j][i] == symbole for j in range(taille)) or \
           all(grille[i][i] == symbole for i in range(taille)) or \
           all(grille[i][taille - i - 1] == symbole for i in range(taille)):
            return True
    return False

def est_match_nul(grille):
    """
    Vérifie si la grille est pleine et qu'aucun joueur n'a gagné.
    """
    return all(cellule != "-" for ligne in grille for cellule in ligne)

def choisir_coup_gagnant(grille, symbole):
    """
    Choisit un coup gagnant si disponible.
    """
    taille = len(grille)
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == "-":
                grille[i][j] = symbole
                if est_gagnant(grille, symbole):
                    grille[i][j] = "-"
                    return i, j
                grille[i][j] = "-"
    return None

def choisir_coup_bloquant(grille, symbole, adversaire):
    """
    Choisit un coup pour bloquer l'adversaire s'il est sur le point de gagner.
    """
    return choisir_coup_gagnant(grille, adversaire)

def choisir_coup_aleatoire(grille):
    """
    Choisit un coup aléatoire parmi les coups disponibles.
    """
    coups_disponibles = [(i, j) for i in range(len(grille)) for j in range(len(grille)) if grille[i][j] == "-"]
    return random.choice(coups_disponibles)

def jouer(taille=3):
    """
    Fonction principale pour jouer au jeu.
    """
    grille = creer_grille(taille)
    symboles = ["X", "O"]
    random.shuffle(symboles)
    print("Le joueur", symboles[0], "commence.")

    for tour in range(taille * taille):
        afficher_grille(grille)
        symbole = symboles[tour % 2]
        print("C'est au tour de", symbole)

        if symbole == "X":
            while True:
                try:
                    ligne = int(input("Entrez le numéro de ligne : "))
                    colonne = int(input("Entrez le numéro de colonne : "))
                    if 0 <= ligne < taille and 0 <= colonne < taille:
                        if poser_pion(grille, ligne, colonne, symbole):
                            break
                        else:
                            print("Cette case est déjà occupée, veuillez choisir une autre.")
                    else:
                        print("Les coordonnées saisies sont hors de la grille, veuillez réessayer.")
                except ValueError:
                    print("Veuillez entrer un numéro valide.")
        else:
            coup = choisir_coup_gagnant(grille, symbole)
            if coup is None:
                coup = choisir_coup_bloquant(grille, symbole, symboles[0])
            if coup is None:
                ligne, colonne = choisir_coup_aleatoire(grille)
            else:
                ligne, colonne = coup
            poser_pion(grille, ligne, colonne, symbole)

        if est_gagnant(grille, symbole):
            afficher_grille(grille)
            print("Le joueur", symbole, "a gagné !")
            return True

        if est_match_nul(grille):
            afficher_grille(grille)
            print("Match nul !")
            return False

    afficher_grille(grille)
    print("Fin de la partie.")

if __name__ == "__main__":
    while True:
        taille = int(input("Entrez la taille de la grille (3 ou plus) : "))
        if taille >= 3:
            if jouer(taille):
                choix = input("Voulez-vous rejouer ? (O/N) : ")
                if choix.lower() != 'o':
                    break
            else:
                choix = input("Voulez-vous rejouer ? (O/N) : ")
                if choix.lower() != 'o':
                    break
        else:
            print("La taille de la grille doit être au moins de 3.")
