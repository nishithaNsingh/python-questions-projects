def anagram(str1,str2):
    freq=[0]*26
    str1=str1.lower()
    str2=str2.lower()
    for i in str1:
        freq[ord(i)-97]+=1
    for i in str2:
        freq[ord(i)-97]-=1
    for i in range(26):
        if freq[i]!=0:
            return("Not anagram")
    else:
         return("Anagram")

str1='left'
str2='felt'
print(str1,str2)
print(anagram(str1,str2))

