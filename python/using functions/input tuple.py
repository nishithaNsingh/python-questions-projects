def tup(n):
    li=[]
    for i in range(0,n):
        a=int(input("Enter a number: "))
        li.append(a)
    return(tuple(li))

n=int(input("Enter number of val: "))
print(tup(n))
