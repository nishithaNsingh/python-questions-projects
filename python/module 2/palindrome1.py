str1=input("Enter a sentence: ")
str2=str1.lower()
if str2==str2[::-1]:
    print("Palindrome")
else:
    print("not palindrome")
