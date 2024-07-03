def member(num1,num2,num3):
    key=3
    print(key in num1)
    print(key in num2)
    return(key in num3)

num1=[5,1,2]
num2={3,1,2}
num3={5,1,2}
print(member(num1,num2,num3))
