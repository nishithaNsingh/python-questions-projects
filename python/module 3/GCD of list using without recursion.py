import math
numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

def find_gcd_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = math.gcd(result, num)
    return result

gcd_result = find_gcd_of_list(numbers)
print(f"The GCD of the list {numbers} is: {gcd_result}")
