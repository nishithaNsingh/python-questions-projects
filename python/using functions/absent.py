def absent(li,s):
    if s in li:
        return("present ")
    else:
        return("absent ")
li=eval(input("Enter a list of numbers"))
s=int(input("ENter roll no: "))
print(absent(li,s))




