dup=[]
sen=input("Enter a sentence: ")
li=list(sen)
li=sen.split(" ")
for i in li:
    if i not in dup:
        dup.append(i)
print(" ".join(dup))
