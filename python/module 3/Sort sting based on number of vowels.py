def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

input_string = input()
strings_list = input_string.split()

sorted_strings = ' '.join(sorted(strings_list, key=lambda x: (count_vowels(x), x), reverse=True))

print(sorted_strings)
