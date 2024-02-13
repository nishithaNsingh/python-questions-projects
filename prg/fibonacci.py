# Get user input for the range
start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

# Initialize the first two numbers in the Fibonacci series
a, b = 0, 1

# Print the Fibonacci series within the given range using a for loop
for i in range(end_range + 1):
    if a >= start_range and a <= end_range:
        print(a, end=" ")
    a, b = b, a + b
