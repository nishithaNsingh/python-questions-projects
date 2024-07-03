def total_ways(n):
    if n<=2:
        return n
    else:
        return total_ways(n-1)+total_ways(n-2)
n=int(input("Enter no of stairs:"))
print("No of ways:",total_ways(n))
