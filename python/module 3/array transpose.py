import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
res=np.empty([3,2])
for i in range(2):
    for j in range(3):
            res[j][i]=arr[i][j]
print(res)
