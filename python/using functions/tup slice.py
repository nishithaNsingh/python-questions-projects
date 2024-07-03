def slicee(tup):
    print(tup[5:8:2])
    print(tup[2:8:3])
    print(tup[2::2])
    print(tup[-5:8:2])
    print(tup[2:-2:3])
    print(tup[-2:3:-1])
    return(tup[-3:-6:1])

tup=(1,2,3,4,5,6,7,8,9,10)
print(slicee(tup))
