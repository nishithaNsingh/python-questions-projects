def strig(str1):
    for i in str1:
        ascii=ord(i)
        if ascii>=ord('a') and ascii<=ord('z'):
            print(chr(ascii-32))
        else:
            print(i,end='')

str1=str(input("Enter a sentence"))
print(strig(str1))
