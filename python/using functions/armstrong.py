def armstrng(n):
    sum=0
    count=0
    while n>0:
        count+=1
        n//=10
    
    t=n
    while t>0:
       digit=t%10
       sum+=(digit**count)
       t//=10


    if sum==n:
      return "Armstrong number"
    else:
      return "not an Armstrong number"

n=int(input("Enter a number"))
print(armstrng(n))
