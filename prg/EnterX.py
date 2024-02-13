sum = 0
print("Enter numbers (enter 'x' to finish):")

while True:
    num = input()

    if num == 'x':
        break

    try:
        num = int(num)
        sum += num
    except ValueError:
        print("Error: Invalid input. Please enter a number or 'x' to finish.")

print("The sum of the numbers is:", sum)
