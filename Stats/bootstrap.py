import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
pop = np.random.randint(0,500 , size=1000)
sample = np.random.choice(pop, size=30) #so n=30
sample_mean = []

for _ in range(10):  #so B=10
    sample_n = np.random.choice(sample, size=30)
    sample_mean.append(sample_n.mean())
    plt.hist(sample_mean)
    plt.show()
print(np.mean(sample_mean))
print(pop.mean())
print(sample.mean())

