def marks(d):
    marks=[]*6
    for i in range(2):
        name=input("Enter your name:")
        for j in range(6):
            marks[j]=float(input("Enter your marks:"))
        d[name]=marks
    for i in d.keys():
        print(i,"has got:",sum(d[i]))

d={}
print(marks(d))
