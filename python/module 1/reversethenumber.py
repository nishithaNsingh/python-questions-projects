rev = 0
num=int(input())
while (num>0):
    digit=num%10
    print(digit,end=" ")
    rev = rev*10
    num//=10
print(rev)    
