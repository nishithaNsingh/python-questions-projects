def cnt(num):
    count = 0
    if num==0:
        print("1")
    else:
        while num>0:
            count+=1
            num//=10
    return count

num=int(input())
print(cnt(num))
