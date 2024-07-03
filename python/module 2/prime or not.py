li=eval(input("Enter a list"))
for i in range(len(li)):
    if i==0 or i==1:
        print(i," is neither prime nor composite")
    else:
        for j in range(2,i):
            if i%j==0:
                print(i," is not prime")
                break
        else:
            print(i," is prime")


            

