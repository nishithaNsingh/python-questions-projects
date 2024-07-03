def logical(a,b):
    print(a<b and a!=b)
    print(a<b or a==b)
    return(not a!=b)

a=int(input())
b=int(input())
print(logical(a,b))


