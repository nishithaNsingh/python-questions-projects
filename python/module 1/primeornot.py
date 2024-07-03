factor=0
num=int(input())
for i in range(1,num+1):
    if num%i==0:
        factor+=1
if factor == 2:
    print("prime")
else:
    print("not prime")
