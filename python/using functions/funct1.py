def logic_prime(ele):
    for i in range(2,ele//2+1):
        if ele%i==0:
            return False
    else:
        return True
li=[10,5,7,11,20]
prime=list(filter(logic_prime,li))
print(prime)
    
