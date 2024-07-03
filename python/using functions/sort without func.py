def sort(li):
    for i in range(0, len(li)):
        for j in range(i+1, len(li)):
            if li[i] >= li[j]:
                li[i], li[j] = li[j],li[i]
 
    return("Sorted List", li)

li=[1,0,3]
print(sort(li))
