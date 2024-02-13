'''age = int(input("Enter your age"))

if(age>=18):
    print("yes")
else:
    print("no")   '''


n = int(input("Enter the number you want to know the table: "))

for mul in range(1, 11):
    print(str(n)+ "X" +str(mul)+ "=" +str(mul*n))