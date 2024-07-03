if __name__ == "__main__":
    string1 = input("Enter a list of string values separated by spaces: ")
    string_values = string1.split()

    mapped_values = list(map(str, string_values))

    print("Input String Values:", string_values)
    print("Mapped String Values:", mapped_values)
