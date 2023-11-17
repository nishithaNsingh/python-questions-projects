def sum_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * sum_recursive(n - 1)

# You need to call the function with a value (e.g., sum_recursive(5))
result = sum_recursive(5)
print(result)
