import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

# making matric
A=np.array([[0,1,0,1,0,1],[0,1,1,0,1,0]])
print(A)

rowX=0
rowY=0
print('enter condition for x: ')
condX=input('0 or 1: ')
if condX == '0':
    rowX=0
else:
    rowX=1
print('enter condition for y: ')
condY=input('0 or 1: ')
if condY == '0':
    rowY=0
else:
    rowY=1
#finding individual probabilty
#for x event
px=0
py=0
for i in A[0]:
    if i==rowX:
        px=px+1
px=px/6
for i in A[1]:
    if i==rowY:
        py=py+1
py=py/6
print(px)
print(py)
#condition probability for x and y at same
pz=0
print(A[0])
for i in range(len(A[0])):
    for j in range(len(A[1])):
        if i==j:
            if A[0][i] == rowX and A[1][j]==rowY:
                pz=pz+1
pz=pz/6
print(pz)
print('p(x|y ):',(pz/py))
print('p(y|x):',(pz/px))
