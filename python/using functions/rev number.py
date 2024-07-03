def rev(num):
    rnum = 0

    while num != 0:
        digit = num % 10
        rnum = rnum * 10 + digit
        num //= 10
    print("revered number: ",end='')
    return(rnum)

num=int(input("Enter a number: "))
print(rev(num))
