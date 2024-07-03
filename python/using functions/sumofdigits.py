def sumdig(num):
    sum = 0
    while num!=0:
        digit = num%10
        sum+=digit
        num//=10
    return(sum)

num=int(input("Enter a number"))
print(sumdig(num))

