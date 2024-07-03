def dupli(sen):
    dup=[]
    li=list(sen)
    li=sen.split(" ")
    for i in li:
        if i not in dup:
            dup.append(i)
    return(" ".join(dup))
sen=input("Enter a sentence: ")
print(dupli(sen))
