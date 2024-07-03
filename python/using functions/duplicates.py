def duplicate(li):
    L=[]
    for i in li:
        if i not in L:
            L.append(i)
    return("list without duplicates: ",L)

li=[0,3,3,1]
print(duplicate(li))
