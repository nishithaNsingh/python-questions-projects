def listt(names,marks):
    for i in range(2):
        names.append(input("Enter Your name:"))
    for i in range(2):
        subject=[]*6
        for j in range(6):
            subject.append(float(input("Enter your marks:")))
        marks.append(subject)
    for i in range(2):
        sum1=0
        for j in range(6):
            sum1=sum(marks[i])
        print(names[i],"has got:",sum1)

names=[]
marks=[]
print(listt(names,marks))
