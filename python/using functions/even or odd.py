def eoro(li):
    for i in li:
        if i%2==0:
            print(i," is even")
        else:
            print(i,"is odd")

n=int(input("enter list size"))
li=[]

for i in range (0,n):
    a=int(input("Enter a number"))
    li.insert(i,a)
print(li)
print(eoro(li))
