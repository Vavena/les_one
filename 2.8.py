import numpy as  np
import math
r = 2.5
v = 1
A = np.array([
 [1.0, 0.0, 2.0],
 [-1.0, 0.5, 2.0],
 [-2.0, 1.5, 0.0],
 [2.5, -1.2, -0.5],
 [1.5, 0.2, -0.2]
 ]
)
x1 = A[v,0]
y1 = A[v,1]
z1 = A[v,2]
sum = 0
for i in range(len(A)):
    for j in range(2):
        x2 = A[i, j]
        y2 = A[i, j]
        z2 = A[i, j]
    dis = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    if dis <= r:
        sum += 1
print(sum)