import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,20)
print(x)
y=x**2
plt.plot(x,y)
plt.title('Graph Plotting')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.show()
