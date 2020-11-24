import random


hauteur = 5
largeur =5

def _init_(hauteur, largeur):
    a = int(input("Entrez l'axe des ordonnées"))
    b=int(input("Entre l'axe des abscisses"))
    a-=1
    b-=1
    listOfList=[] 

    for i in range(hauteur):
        listRow = []
        if i==b:
            listRow.append("X")

        for j in range(largeur):
            if j == a:
                listRow.append("0")
            else:
                listRow.append("X")
        listOfList.append(listRow)
        
    
    return listOfList   

liste = _init_(hauteur, largeur)
for i in liste:
    print(i)



