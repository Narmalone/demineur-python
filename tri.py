#tri sélection
list=[2,8,6,3,]
def selectMin(list):
    var=list[0]
    for i in list:
        if var>i:
            var=i
    return var
print("Oh non, la liste est dans le désordre !")
print(list)

def triSelect (list):
    result=[]
    while len(list)>0:
        var=selectMin(list)
        list.remove(var)
        result.append(var)
    return result
print("Bien joué, la liste est triée:")
print(triSelect(list))

#Tri fusion
def fusion(t,d,p,f):
    i=d
    j=p
    res=[]
    while i<p and j<f:
        if t[i]<t[j]:
            res.append(t[i])
            i=i+1
        else:
            res.append(t[j])
            j=j+1
    while i<p:
        res.append(t[i])
        i=i+1
    while j<f:
        res.append(t[j])
        j=j+1
    return res
 
def tri_fusion(t,i,j):
    if i<j:
        m = (i+j)//2
        tri_fusion(t,1,m)
        tri_fusion(t,m+1,j)
        t=fusion(t,i,m,j)
 
tab=[4,3,5,2,1]

tri_fusion(tab,0,len(tab))
print(tri_fusion(tab,0,len(tab)))

tab_1 = [20, 2, 3]
def modif_1(tableau):
    for i in range(list):
        tab_1.append(i) 
 
#Appel de la fonction()
print(tab_1)
 
 
tab_2 = [1, 2, 3]
def modif_2(tableau):
    for i in range(4, 9):
        tableau.append(i)
    return tableau
 
tab_2 = modif_2(tab_2)
print(tab_2)
