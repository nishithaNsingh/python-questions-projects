import math
from functools import reduce
numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

def find_gcd_of_list(numbers):
    return reduce(math.gcd, numbers)

gcd_result = find_gcd_of_list(numbers)
print(f"The GCD of the list {numbers} is: {gcd_result}")
