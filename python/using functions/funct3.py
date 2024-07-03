def logic(arg):
    cnt=0
    vowels='aeiouAEIOU'
    for i in arg:
        if i in vowels:
            cnt+=1
    return cnt 
li=["Sanjana","Yeshas","Keerthana","Varun"]
li=sorted(li,key=logic)
print(li)
