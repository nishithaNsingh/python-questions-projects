
def counter(num):
    count=1
    if num==0:
        return 1
    else:
        while num>0:
            count+=1
            num//=10
            return count

num = int(input("Enter a number"))
print(counter(num))

