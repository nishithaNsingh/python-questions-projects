import numpy as np
li=[10,20,30,40]
res=np.gcd(li[o],li[1])
for i in range(2,len(li)):
    res=np.gcd(res,li[i])
print(res)
