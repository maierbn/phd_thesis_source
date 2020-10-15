#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def phat(x):
  sigma = 1
  a = np.pi**2 / (4*sigma**4)
  return 1 / (1+a*x**2)
 
 
xlist = np.linspace(-3,3,200)
ylist = [phat(x) for x in xlist]

plt.rcParams.update({'font.size': 22})
fig = plt.figure()
ax = fig.gca()
plt.plot(xlist, ylist, '-', lw=5)
ax.set_ylim(-0.1,1.1)
plt.grid(which='major')
plt.tight_layout()
plt.savefig("phat.pdf")
plt.show()
