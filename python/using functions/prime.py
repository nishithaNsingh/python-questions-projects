def prime(num):
    if num==1 or num==0:
        print("neither prime nor composite")
    for i in range(2,num//2+1):
        if num%i==0:
            print("not prime")
            break
        else:
            print("prime")
            break

num=int(input("Enter a number: "))
print(prime(num))
