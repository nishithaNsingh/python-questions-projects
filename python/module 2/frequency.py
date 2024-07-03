frq=[0]*26
str1="Rohit"
str1=str1.lower()
for i in str1:
    frq[ord(i)-97]=str1.count(i)
for i in range(26):
    if chr(i+97) in str1:
            print(chr(i+97),':',frq[i])	
