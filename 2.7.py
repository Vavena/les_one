import numpy as np
import math

A = np.array([3,2,5,4,1,7])
MIN1 = math.inf
MIN2 = math.inf
MIN1i= 0
MIN2i = 0
min = np.min(A)
for i in range(len(A)):
    if (A[i] < MIN1) and (A[i]!= min):
        MIN2 = MIN1
        MIN1=A[i]
        MIN2i = MIN1i
        MIN1i = i
    if(A[i]== min):
        I = i
print(I, MIN1i, MIN2i)