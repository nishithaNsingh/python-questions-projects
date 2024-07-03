def sum(n):
    sum=0

    for var in range(1,n,1):
        sum+=var
    print(sum)

n = int(input("Enter a number"))
print(sum(n))
