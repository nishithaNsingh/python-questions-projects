n=int(input())
if n<=2:
    print(n)
else:
    prev1=1
    prev2=2
    for i in range(3,n+1):
        current=prev1+prev2
        prev1=prev2
        prev2=current
    print(current)
