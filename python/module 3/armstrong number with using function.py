start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

armstrong_numbers = []

for num in range(start_range, end_range + 1):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    if armstrong_sum == num:
        armstrong_numbers.append(num)

print(f"Armstrong numbers between {start_range} and {end_range}: {armstrong_numbers}")
