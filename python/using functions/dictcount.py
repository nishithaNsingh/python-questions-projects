def cnt(li,str1):
    dict1={}
    for i in li:
            dict1[i]=li.count(i)
    if str1 in li:
            return(dict1[str1])
    else:
            return("invalid")

li=['Suresh','Mahesh','Hitesh']
str1=input()
print(cnt(li,str1))

