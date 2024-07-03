import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def calculate_lcm():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = lcm(num1, num2)
        print(f"The LCM of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter valid integers.")

calculate_lcm()
