input_string = input()
strings_list = input_string.split()

sorted_strings = ' '.join(sorted(strings_list, key=lambda x: (len(x), x)))

print(sorted_strings)
