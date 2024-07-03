def cap(sen):
    li=sen.split()
    for i in li:
        return(i.capitalize())

sen=input("Enter a sentence")
print(cap(sen))
