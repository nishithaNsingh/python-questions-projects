def bitwis(a,b):
    print(a&b)
    print(a/b)
    print(a^b)
    print(~a)
    print(~b)
    print(a>>1,b>>1)
    print(a<<1,b<<1)

a=int(input())
b=int(input())
print(bitwis(a,b))
