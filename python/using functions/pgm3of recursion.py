def print_digits(n):
    if n<9:
        print(n)
    else:
        print_digits(n//10)
        print(n%10)
num=int(input())
if num<0:
    print("-")
    print(-num)
else:
    print_digits(num)
    


