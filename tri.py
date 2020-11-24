import random

hauteur = 5
largeur =5



def _init_(hauteur, largeur):

    listOfList=[] 
       
    for i in range(hauteur):
        listRow = []

        for j in range(largeur):
            listRow.append("X")
        listOfList.append(listRow)
        
    
    return listOfList 

def modifyTableau(list):
    a = int(input("Entrez l'axe des ordonnées"))
    b =int(input("Entre l'axe des abscisses"))

    list[a][b]="0"

def affiche(tableau):
    for i  in tableau:
        print(i)

def demineur():
    liste = _init_(hauteur, largeur)
    pasPerdu=True
    while (pasPerdu):
        modifyTableau(liste)
        affiche(liste)

demineur()
