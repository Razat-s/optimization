import numpy as np
import matplotlib.pyplot as plt
% matplotlib inline

mu = None
var = None
# Gaussian Distribution of sum of random variables
def gaussian():
    return (1/np.sqrt(2 * np.pi*var)) * np.exp(-((x-mu)**2)/2*(var))

x = np.linspace(-5,5,200)
for i in range(4):
    for j in range(4):
        mu = i
        var = j
        plt.plot(x,gaussian())
        
plt.xlabel('Random variable')
plt.ylabel('$P_X(x_i)$')
plt.legend(["mean = 0,1,2,3","variance = 1,2,3,4"])
plt.show()