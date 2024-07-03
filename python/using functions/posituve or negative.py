def value(num):
    
    if num>0:
      return ("Positive")
    elif num == 0:
        return ("Neither positive nor negative")
    else:
        return ("Negative")

num=int(input())
print(value(num))

        
