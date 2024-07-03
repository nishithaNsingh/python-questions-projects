def pal(str1):
    str1=str1.lower()
    start=0
    a=str1.len()-1
    last=a-1
    
    while start<last:
        if str1[start]!=str1[last]:
            return("not palindrome")
        start+=1
        last-=1
    else:
        return("palindrome")

str1=input("enter a sentence")
print(pal(str1))
