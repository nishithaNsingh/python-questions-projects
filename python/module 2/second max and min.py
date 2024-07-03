li=[0,3,2,1]
n=len(li)-2
for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
print("Second largest: ",li[n])
print("Second minimum: ",li[1])
            
