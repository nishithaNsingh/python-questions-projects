def swap(num1,num2):
    num1,num2 = num2,num1
    return num1,num2

num1=int(input())
num2=int(input())
print("before swapping: ",num1,num2)
print("after swapping: ",end='')
print(swap(num1,num2))
