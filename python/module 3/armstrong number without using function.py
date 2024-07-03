def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number

def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
result = find_armstrong_numbers(start_range, end_range)
print(f"Armstrong numbers between {start_range} and {end_range}: {result}")
