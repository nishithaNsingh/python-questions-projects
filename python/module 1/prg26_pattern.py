n = int(input())
for row in range(1,n+1):
    for sp in range(n-row, -1,-1):
        print(" ", end = " ")
    for st in range(1,2*row):
        print("*",end=" ")
    print()
