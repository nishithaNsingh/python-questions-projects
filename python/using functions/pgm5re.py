sum=0
def sum_digits(n):
    global sum#=10
    if n<=9:
        sum=n
    else:
      sum_digits(n//10)
      sum+=(n%10)
num=int(input())
if num<0:
    print("invalid")
    
else:
    sum_digits(num)
    print(sum)
    
