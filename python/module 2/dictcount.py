li = ['Suresh', 'Mahesh', 'Hitesh']
str1 = input()
dict1 = {}

for i in li:
    dict1[i] = li.count(i)

if str1 in li:
    print(dict1[str1])
else:
    print("invalid")
