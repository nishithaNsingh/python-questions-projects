n=int(input("Enter list size: "))
li=[]
for i in range(0,n):
    a=int(input("Enter a value: "))
    li.append(a)
    li.sort()

print(li)
