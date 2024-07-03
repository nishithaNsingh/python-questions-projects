def pdr(number):
    if number < 10:
        print(number)
    else:
        pdr(number // 10)
        print(number % 10)
        
user_input = int(input("Enter a number: "))
print("Digits from left to right:")
pdr(user_input)
