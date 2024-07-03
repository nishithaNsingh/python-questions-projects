def compute_sum(num):
    global res
    if num<10:
        res=num
    else:
        compute_sum(num//10)
        res+=num%10
res=0
num=int(input())
compute_sum(num)
print(res)
