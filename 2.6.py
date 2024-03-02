import numpy as np

def nonzero(A):
    for i in range(100):
        for j in range(100):
            if(A[i,j]!=0):
                print(i," ", j)
                break
A = np.zeros((100,100))
A[76,35]=1
nonzero(A)