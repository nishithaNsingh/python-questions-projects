def freq(str1):
    for i in str1:
        dict1 = {str1.count(i)}
        print("the count of",str(i),"is",str(dict1))

str1="hello"
print(freq(str1))
