import math as m
import random as r
import numpy as np
import matplotlib.pyplot as plt



def gaussian(n):
    sdev = 2
    return np.exp(-(n**2) / (2*sdev**2)) / (m.sqrt(2*m.pi*sdev**2))
    
def angle():
    x = r.random()
    y = 10*r.random()-5
    if x<gaussian(y):
        return y
    else:
        return False

ar=[]
        
for i in range(100000):
    x=False
    while x == False:
        x=angle()
    ar+=[x]
    
plt.hist(ar,bins=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    
fig2 = plt.gcf()
plt.show()
plt.savefig("peter.pdf")