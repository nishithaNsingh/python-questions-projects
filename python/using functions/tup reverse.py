def rev(tup):
    for i in range(len(tup)-1,-1,-1):
        print(tup[i])

    print(tup[::-1])

tup=(10,20,30)
print(rev(tup))
