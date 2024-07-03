def prime(li):
    for i in range(len(li)):
        if i==0 or i==1:
            print(i," is neither prime nor composite")
        else:
            for j in range(2,i):
                if i%j==0:
                    print(li[i]," is not prime")
                    break
            else:
                print(li[i]," is prime")

li=eval(input("Enter a list: "))
print(prime(li))
