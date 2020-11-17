
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
