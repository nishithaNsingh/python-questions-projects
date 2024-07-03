def pal(str1):
    str2=str1.lower()
    if str2==str2[::-1]:
        return("Palindrome")
    else:
        return("not palindrome")

str1=input("Enter a sentence: ")
print(pal(str1))
