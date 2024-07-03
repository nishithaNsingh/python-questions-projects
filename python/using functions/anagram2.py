def anag(str1,str2):
    if sorted(str1)==sorted(str2):
        return("Anagram")
    else:
        return("not anagram")

str1=input()
str2=input()
print(anag(str1,str2))
