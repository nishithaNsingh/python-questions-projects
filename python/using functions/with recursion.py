def total_ways(n):
    if n<=2:
        return n
    else:
        return total_ways(n-1)+total_ways(n-2)
n=int(input())
print(total_ways(n))
