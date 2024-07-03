n=int(input("enter list size"))
li=[]

for i in range (0,n):
    a=int(input("Enter a number"))
    li.insert(i,a)
    if a%2==0:
        print("Even")
    else:
        print("odd")

print(li)
