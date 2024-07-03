def logic(arg):
    return arg[1]
res=[]
li=["sanjana","varun","keerthana","varun"]
dict1={}
for i in li:
    dict1[i]=li.count(i)
li=sorted(dict1.items(),key=logic)
for i in li:
    for j in range(i[1]):
        res.append(i[0])
print(res)
