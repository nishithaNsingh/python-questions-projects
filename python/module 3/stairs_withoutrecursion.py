n=int(input("Enter number of stairs:"))
if n<=2:
    print(n)
else:
    prev_1=1
    prev_2=2
    for i in range(3,n+1):
        current=prev_1+prev_2
        prev_1=prev_2
        prev_2=current
    print("No of ways:",current)
