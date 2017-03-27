
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
n = 100
T = 1
N = 20
h = T*1.0/n
t = np.array(range(n))*h
w = np.zeros(n);
X = np.zeros((N,n))
plt.figure(1)
for i in range(int(N)):
    for x in range(n):
        w [x]= np.random.normal(0,t[x]**0.5,1)
    X[i] = w
    plt.plot(w,linewidth = 1.0)
plt.xlabel('period')
plt.ylabel('value')
plt.title('Wt under P')

plt.figure(2)
for i in range(N):
    plt.plot(X[i],linewidth = 1.0)
plt.xlabel('period')
plt.ylabel('value')
plt.title('X_t under P measure')
plt.show()
