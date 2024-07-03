def maxmin(li,n):
    for i in range(0,len(li)):
        for j in range(i+1,len(li)):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
    print("largest: ",li[n])
    print("minimum: ",li[0])

li=[0,3,2,1]
n=len(li)-1
print(maxmin(li,n))


