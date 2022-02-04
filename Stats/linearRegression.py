import pandas as pd
import matplotlib.pyplot as plt

a=0.0
b=0.0
dataset1=pd.read_csv('Stats/linear reg.csv', header=None)
def linear():
    

    print(dataset1.iloc[:,:])
    n=int(dataset1.size/2)
    SUMX=0
    for x in dataset1.iloc[:,0]:
        SUMX=SUMX+x
    print(SUMX)

    SUMY=0
    for x in dataset1.iloc[:,1]:
        SUMY=SUMY+x
    print(SUMY)

    SUMX2=0
    for x in dataset1.iloc[:,0]:
        SUMX2=SUMX2+(x**2)
    print(SUMX2)

    SUMXY=0
    for x in range(n):
        SUMXY=SUMXY+(dataset1.iloc[x,0]*dataset1.iloc[x,1])

    print(SUMXY)
    global a
    a=(SUMY*SUMX2 - SUMX*SUMXY)/(n*SUMX2 - (SUMX**2))
    print(a)
    #print(dataset1.loc[0,0])
    global b
    b= (n*SUMXY - SUMX*SUMY )/(n*SUMX2 - (SUMX**2))
    print(b)

def predict():
    #linear regression
    getX=float(input('Enter independent variable: '))
    global a
    global b
    Y=a+b*getX
    print(Y)

statement=int(input('1. prediction: '))
if (statement ==1):
   linear()
   predict()
    
else:
    print("No proper input")