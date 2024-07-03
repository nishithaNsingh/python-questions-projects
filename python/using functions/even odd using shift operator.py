def evenodd(num):
    res=num>>1
    if num==res<<1:
        return "even"
    else:
        return "odd"

num=int(input("Enter a number: "))
print(evenodd(num))
