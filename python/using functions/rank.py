def rank(uni):
    index=-1
    roll=int(input("Enter roll number: "))
    if roll in uni:
        index=uni.index(roll)
    print("rank: ",index+1)


uni=eval(input("Enter roll no acc to rank: "))
print(rank(uni))
