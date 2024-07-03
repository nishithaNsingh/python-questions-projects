num=int(input("Enter a number"))
li=[]
while num>0:
    dig=num%10
    li.append(dig)
    num//=10
for i in li[::-1]:
    print(i)
