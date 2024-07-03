num = int(input())
while num>0:
    digit = num%10
    print(digit)
    num//=10
    if num==0:
        break
else:
    print("0")
    
