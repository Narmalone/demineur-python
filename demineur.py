# --------------------------------------
"""   Démineur """
# --------------------------------------

# Variables
# Modifiez ces variables pour changer les settings du jeu

import random


hauteur = 5
largeur = 5
minesMax = 5

# --------------------------------------
"""   Nombre de mines """
# --------------------------------------

def mines(max):
    nMine = random.randint(2,minesMax)
    return nMine
print("Il y a |",mines(minesMax),"| mines.")

# --------------------------------------
"""   Position des mines """
# --------------------------------------
def _mines_(hauteur, largeur):

    listOflist=[]

    for i in range(hauteur):
        listRow=[]

        for j in range(largeur):
            listRow.append(0)
        listOflist.append(listRow)
        
    return listOflist

# Position aléatoire des mines

def minesPos(list):
    c = random.randint(2,hauteur)-1
    d = random.randint(2,largeur)-1

    list[c][d]="0"

# --------------------------------------
"""   Tableau visible """
# --------------------------------------

# Paramètre de la grille
def _init_(hauteur, largeur):

    listOflist=[]

    for i in range(hauteur):
        listRow=[]

        for j in range(largeur):
            listRow.append("X")
        listOflist.append(listRow)
        
    return listOflist

# Position du joueur
def modifyTableau(list,mines):
    pasPerdu=True
    a = int(input("Choix de la ligne entre 0 et 4 : "))
    b = int(input("Choix de la colonne entre 0 et 4 : "))
    if (mines[a][b]==1):

        print("Vous avez perdu, dommage.")
        pasPerdu=False
    compteur=0
    if (a>0 and b>0 and mines[a-1][b-1]==1):
        compteur+=1
    if (a<largeur-1 and b<hauteur-1 and mines[a+1][b+1]==1):
        compteur+=1
    if (a>largeur-1 and b<hauteur-1 and mines[a-1][b+1]==1):
        compteur+=1
    if (a<largeur-1 and b>hauteur-1 and mines[a+1][b-1]==1):
        compteur+=1
    if (a>largeur-1 and mines[a+1][b]==1):
        compteur+=1
    if (a<largeur-1 and mines[a-1][b]==1):
        compteur+=1
    if (b<hauteur-1 and mines[a][b-1]==1):
        compteur+=1
    if (b>hauteur-1 and mines[a][b+1]==1):
        compteur+=1

    list[a][b]=compteur

    return pasPerdu

# Affichage 
def affiche(tableau):
    for i in tableau:
        print(i)

def placerMines(mines):
    for i in range(minesMax): 
     x = random.randrange(1,5) 
     y = random.randrange(1,5) 
     mines[x][y] = 1
    print()

# Durée de jeu 
def demineur():
    liste = _init_(hauteur,largeur)
    mines = _mines_(hauteur,largeur)
    placerMines(mines)
    pasPerdu=True
    while (pasPerdu):
        pasPerdu=modifyTableau(liste,mines)
        affiche(liste)

demineur()


