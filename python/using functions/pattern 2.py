def pattern(n):
    for row in range(1,n+1):
        for sp in range(n-row):
            print(" ",end="")
        for st in range(2*row-1):
            print("*",end = "")
        print()
n=int(input())
print(pattern(n))
