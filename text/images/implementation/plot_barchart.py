#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
now = datetime.datetime.now()
print(" ======= plot_mesh_quality.py =======") 
print(now.strftime("%d/%m/%Y %H:%M:%S"))

import sys, os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

# load data
if len(sys.argv) == 2:
  filename = sys.argv[1]
else:
  print("usage: <filename>")

# columns:
# 0 scenario name; filename; n valid fibers; variance element lengths; variance angles
# 1 filename; 
# 2 n valid fibers; 
# 3 variance element lengths; 
# 4 variance angles; 

labels = [
  "Combined quadrature,\nexplicit vectorization",            # 5.239
  "Combined quadrature,\nno explicit vectorization",         # 7.857
  "Single quadrature,\nexplicit vectorization",              # 352.502
  "Single quadrature,\nno explicit vectorization",           # 1408.36
]
plt.rcParams.update({'font.size': 18})

tlist = np.arange(len(labels))  # the label locations
width = 0.7  # the width of the bars

#datalist = [data[5,4], data[4,4], data[3,4]]
datalist = [5.239, 7.857, 352.502, 1408.36]

color = "#800000"  # maroon
color = "#ffcc00"  # yellow
textcolor="k"

fig = plt.figure(figsize=(10,5))
ax = fig.add_axes([0.4,0.2,0.5,0.7])  # [left, bottom, width, height] 
rects1 = ax.barh(tlist, datalist, width, color=color)

for t,d in zip(tlist,datalist):
  x = d-0.1
  y = t-0.05
  if x < 10:
    ax.text(x+50,y,"{:.1f} s".format(d),color="k",verticalalignment='center',horizontalalignment='left')
  else:
    ax.text(x,y,"{:.1f} s".format(d),color=textcolor,verticalalignment='center',horizontalalignment='right')

ax.set_xlabel('Runtime [s]')
#ax.set_ylabel(r'')
ax.set_yticks(tlist)
ax.set_yticklabels(labels)
plt.grid(which='major', axis='x')
#ax.set_ylim(0,0.8)

#plt.legend([rects1[0]], ['Standard deviation of \nrelative element lengths', 'Duration [s]'], fontsize=16, loc='upper center')
# Add some text for labels, title and custom x-axis tick labels, etc.

plt.savefig("matrix_runtimes.pdf")
plt.show()
