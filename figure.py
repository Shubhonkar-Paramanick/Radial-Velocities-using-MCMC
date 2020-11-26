#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
import numpy as np

def gaussian(x, a, mu, sig):
    return a*np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

x_values = np.linspace(-9, 12, 1200)
a=2
mu=0
sig=1


#[(1, 3,2), (3, -2,1), (2, 0, 1)]:
plt.plot(x_values, gaussian(x_values, a, mu, sig), 'g',alpha=0.2)
#plt.fill_between(x_values, gaussian(x_values, a, mu, sig), color='g',alpha=0.7)

a2=1
mu2=3
sig2=2


#[(1, 3,2), (3, -2,1), (2, 0, 1)]:
plt.plot(x_values, gaussian(x_values, a2, mu2, sig2), 'b',alpha=0.2)



a1=3
mu1=-2
sig1=1


#[(1, 3,2), (3, -2,1), (2, 0, 1)]:
plt.plot(x_values, gaussian(x_values, a1, mu1, sig1), 'r',alpha=0.2)


a3=3.7
mu3=-1
sig3=1


#[(1, 3,2), (3, -2,1), (2, 0, 1)]:
plt.plot(x_values, gaussian(x_values, a3, mu3, sig3), 'k',alpha=1)


plt.axis([-9, 12, 0, 4])    
plt.tick_params(top=False, bottom=False, left=False, right=False,
                labelleft=False, labelbottom=False)      
plt.title('Posterior', fontsize=20)
plt.xlabel('Model Parameter', fontsize=16)
plt.ylabel('Probability Density', fontsize=16)
mp.show()      
