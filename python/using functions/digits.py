def digits(num):
    while num>0:
        dig=[]
        digit=num%10
        dig.append(digit)
        num//=10
        for i in dig:
            print i
       
num=int(input("Enter a number"))
k=digits(num)
print(k)
