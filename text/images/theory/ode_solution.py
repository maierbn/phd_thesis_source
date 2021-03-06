#!/bin/python

import numpy as np
import matplotlib.pyplot as plt

ninfty = 2
tau = 3.0

def f(t):
  return ninfty*(1 - np.exp(-1/tau*t))
  
xmax = 10
xlist = np.linspace(0, xmax, 100)
ylist = [f(t) for t in xlist]
print xlist
print ylist

plt.plot([0, xmax], [ninfty, ninfty])
plt.plot([0, tau], [0, ninfty], 'r-.')
plt.plot(xlist, ylist)
plt.xlabel("t")
plt.ylabel("y")
plt.ylim([0, 2.5])

plt.show()
