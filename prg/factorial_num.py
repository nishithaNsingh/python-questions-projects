# Get user input for the number
num = int(input("Enter a number: "))

# Initialize the factorial variable
factorial_result = 1

# Calculate the factorial
for i in range(1, num + 1):
    factorial_result *= i

# Print the result
print(f"The factorial of {num} is: {factorial_result}")
