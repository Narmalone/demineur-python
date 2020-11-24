#Démineur

#variables

import random 

#Terrain

hauteur = 5
largeur =5

#Mines

mineMax=5

#Fonction mines

def mines(max):
    nbMines= random.randint(2, mineMax)
    return nbMines
print("il y'a ", mines(mineMax), " mines ")

def _mines_(hauteur, largeur):

    listOfList=[] 
       
    for i in range(hauteur):
        listRow = []

        for j in range(largeur):
            listRow.append(mines)
            print(mines)
        listOfList.append(listRow)
        
    
    return listOfList 

def minesPosition(list):
    affiche(_init_)

    if modifyTableau==_mines_:
        print("vous avez perdu")


#Fonction terrain

def _init_(hauteur, largeur):

    listOfList=[] 
       
    for i in range(hauteur):
        listRow = []

        for j in range(largeur):
            listRow.append("X")
        listOfList.append(listRow)
        
    
    return listOfList 

#postion joueur

def modifyTableau(list):
    a = int(input("Choisissez votre ligne : "))-1
    b = int(input("Choisissez votre colonne : "))-1
    list[a][b]="0"

#Affichage du tableau

def affiche(tableau):
    for i in tableau:
        print(i)

#Si pas perdu continuer

def demineur():
    liste = _init_(hauteur, largeur)
    pasPerdu=True
    while (pasPerdu):
        modifyTableau(liste)
        affiche(liste)

demineur()

