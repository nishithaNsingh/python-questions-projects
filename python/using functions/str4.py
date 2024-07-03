def vowel(n):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowel_list = []

    for char in n:
        if char in vowels:
            vowel_list.append(char)

    print("Vowels are:")
    for vowel in vowel_list:
        print(vowel)


n=input("Enter a string: ")
print(vowel(n))
