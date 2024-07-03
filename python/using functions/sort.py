def sort(li,n):
    for i in range(0,n):
        a=int(input("Enter a value: "))
        li.append(a)
        li.sort()

    return(li)

n=int(input("Enter list size: "))
li=[]
print(sort(li,n))
