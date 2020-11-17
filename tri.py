import random
def _init_(hauteur, largeur):

    listOfList=[]

    for i in range(hauteur):
        listRow = []

        for j in range(largeur):
            listRow.append("X")
        listOfList.append(listRow)

    return listOfList   

liste = _init_(5, 5)

for i in liste :
    print(i)


#joueurs interagis avec le plateau

#après la première intéraction, création d'un nombre aléatoire de mines
def mines(max):
    num1 = random.randint(2,max)
    return num1 
print (mines(10))


import random
def nbMines(hauteur, largeur):

    listOfList=[]

    for i in range(hauteur):
        listRow = []

        for j in range(largeur):
            listRow.append(0)
        listOfList.append(listRow)
    
    max=mines(hauteur*largeur//5)
    nbMines = 0

    while nbMines<max:
    
    #nombreDemines +=1
        x= random.randint(0,largeur) 
        y= random.randint (0,hauteur)
        # listOfList [x] [y] =1
        print (nbMines)
        if [x] [y] == 1:
            i=0
        nbMines += 1

    return listOfList   


for i in liste :
    print(i)


def premiereCase(x,y, height, width):
    listOfList=[]
    x-=1
    y-=1
    for i in range(height):
        listRow=[]
        if i==y:
             for i in range(width):
                if i == x :
                    listRow.append(0)
                else :
                    listRow.append("X") 
        else:
            for i in range(width):
                listRow.append("X")
        listOfList.append(listRow)
    return listOfList 


def joueur(coord):
    
