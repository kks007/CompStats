import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
# making matrics

# matric A

print("Do you want to enter matrix manually? (y/n): ")
ans = input()
if ans == 'y':
    f1 = pd.read_csv('dataset1.csv')
    f2 = pd.DataFrame(f1)
    A = f1.to_numpy()
else:
    A = np.array([[90, 80, 40], [90, 60, 80], [60, 50, 70], [30, 40, 70], [30, 20, 90]])
print(A)

# finding mean of A
mean = np.zeros((1, 3))
print(len(A[0]))
for i in range(len(A)):
    X = A[i]
    for j in range(len(X)):
        mean[0][j] = mean[0][j]+X[j]
mean = mean/len(A)
# print(mean)
# deviation matrix

# DevM = A -[1].A.(1/5)
nes = np.ones((len(A), len(A)))
print(nes)
M1 = nes.dot(A)
M2 = M1/5
DevM = A - M2
print(DevM)

# co varience matrix

#covM = DevM^transpose . DevM

covM = DevM.transpose().dot(DevM)
print(covM)

# now calculate mulltivariate normal distribution (probability)
w = [x for x in range(len(A))]
y = list()
mu = mean[0]
sigma = covM
d = len(A[0])
for val in A:
    print("For row :", end=" ")
    print(val)
    Z = (-1/2) * (np.transpose((val - mu)).dot(np.linalg.inv(sigma))).dot((val - mu))
    # print(Z)
    Px = (1/(math.sqrt((2*np.pi)**d * np.linalg.det(sigma)))) * math.exp(Z)
    y.append(Px)
    print(Px)

plt.plot(w, y)
plt.xlabel("values")
plt.ylabel("Probability")
plt.grid()
plt.show()
