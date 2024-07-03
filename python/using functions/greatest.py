def great(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print(num1," is the greatest.")
    elif(num2>num1 and num2>num3):
        print(num2," is the greatest.")
    else:
        print(num3," is the greatest.")
    return 

num1=int(input())
num2=int(input())
num3=int(input())
k=great(num1,num2,num3)
print(k)
         
