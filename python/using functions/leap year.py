def leapyear(y):
    if(y%4==0):
        if(y%100==0):
            if(y%400==0):
                return("leap")
            else:
                return("not leap")
        else:
            return("leap")
    else:
        return("not leap")

y=int(input("Enter a year: "))
print(leapyear(y))
