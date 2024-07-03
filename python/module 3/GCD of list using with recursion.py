import math
def find_gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return find_gcd_recursive(b, a % b)
def find_gcd_of_list_recursive(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return find_gcd_recursive(numbers[0], find_gcd_of_list_recursive(numbers[1:]))

numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
gcd_result = find_gcd_of_list_recursive(numbers)
print(f"The GCD of the list {numbers} is: {gcd_result}")
