n=input("Enter a string: ")
L=["a","e","i","o","u","A","E","I","O","U"]
LI=[]
for i in n:
    for i in L:
        if i not in L:
            LI.append(i)
print("vowels are")
for j in LI:
    print(j,end='')
    
