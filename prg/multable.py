# using for loop
'''num = int(input("Enter a number: "))
table_range = int(input("Enter the range for the multiplication table: "))

# Check if the range is positive
if table_range < 0:
    print("Invalid range. Please enter a positive range.")
else:
    # Loop to calculate and print the multiplication table
    for i in range(1, table_range + 1):
        result = num * i
        print(f"{num} x {i} = {result}")

    print("Table calculated successfully.")'''

# using while loop 
num = int(input("Enter a number: "))
table_range = int(input("Enter the range for the multiplication table: "))

# Check if the range is positive
if table_range < 0:
    print("Invalid range. Please enter a positive range.")
else:
    # Initialize a variable to keep track of the current index
    i = 1

    # Loop to calculate and print the multiplication table
    while i <= table_range:
        result = num * i
        print(f"{num} x {i} = {result}")
        i += 1

    if i > table_range:
        print("Table calculated successfully.")
    else:
        print("Sorry, the table was not calculated.")



