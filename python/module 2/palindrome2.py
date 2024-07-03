str1=input()
str1=str1.lower()
start=0
last=str1.len()-1
while start<last:
    if str1[start]!=str1[last]:
        print("not palindrome")
    start+=1
    last-=1
else:
    print("palindrome")
