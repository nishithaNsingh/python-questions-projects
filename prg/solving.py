'''dig = []
for i in range(2, 7):
    dig = [i]
print(dig)'''

'''list_a = ["V", "I","B","G","Y","O","R"]
print(list_a[1:6:2])'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a loop to find the sum of odd numbers
sum_of_odd = 0
for number in my_list:
    if number % 2 != 0:  # Check if the number is odd
        sum_of_odd += number

print("Sum of odd numbers:", sum_of_odd)

