def sum_digits(n):
    if n<9:
        return(n)
    else:
        return sum_digits(n//10)+(n%10)
num=int(input())
if num<0:
    print("invalid")
    
else:
    print(sum_digits(num))
    
