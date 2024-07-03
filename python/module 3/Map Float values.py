def square_root(value):
    return value ** 0.5

def map_to_square_root(values):
    return map(square_root, values)
if __name__ == "__main__":
    num = input("Enter a list of float values separated by spaces: ")
    float_values = list(map(float, num.split()))
    sqrt_values = list(map_to_square_root(float_values))
    print("Input Float Values:", float_values)
    print("Square Root Values:", sqrt_values)
