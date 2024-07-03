def filter_even_elements(numbers):
    return [num for num in numbers if num % 2 == 0]

if __name__ == "__main__":
    try:
        numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
        num = filter_even_elements(numbers)
        print("Even elements:", num)
    except ValueError:
        print("Invalid input. Please enter a list of numbers.")
