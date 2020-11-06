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
  #quit()

#data = np.genfromtxt(filename, delimiter=";")

data = np.array([
  [0,0,961,0.02190327871339396,0.1703234817249599], # 31x31fibers_l1_m1_4In_neumann.no_boundary.bin
  [0,0,961,0.021851135102074922,0.17050822677704625], # 31x31fibers_l1_m1_3In_neumann.no_boundary.bin
  [0,0,961,0.021813104172269338,0.17081704640689485], # 31x31fibers_l1_m1_2In_neumann.no_boundary.bin
  [0,0,961,0.022020439851158917,0.17388858740852675], # 31x31fibers_l1_m1_3In_dirichlet.no_boundary.bin
  [0,0,961,0.021958865533939623,0.1749230361859109], # 31x31fibers_l1_m1_2In_dirichlet.no_boundary.bin
  [0,0,961,0.025242259874085154,0.17506040702962086], # 31x31fibers_l1_m1_1IG_dirichlet.no_boundary.bin
  [0,0,961,0.022535321251316052,0.17586747159571584], # 31x31fibers_l1_m1_2IG_dirichlet.no_boundary.bin
  [0,0,961,0.02166185838487164,0.1759734570956548],   # 31x31fibers_l1_m1_1In_dirichlet.no_boundary.bin
])
# columns:
# 0 scenario name; filename; n valid fibers; variance element lengths; variance angles
# 1 filename; 
# 2 n valid fibers; 
# 3 variance element lengths; 
# 4 variance angles; 

labels = [
  "N4s", "N3s", "N2s", "D3s", "D2s", "D1g", "D2g", "D1s"
]
plt.rcParams.update({'font.size': 18})

tlist = np.arange(len(labels))  # the label locations
width = 0.7  # the width of the bars

#datalist = [data[5,4], data[4,4], data[3,4]]
datalist = data[:,4]

textcolor = "#800000"
textcolor = "k"
color = "#ffcc00"
fig, ax = plt.subplots(figsize=(4.5,5))
rects1 = ax.barh(tlist, datalist, width, color=color)
for t,d in zip(tlist,datalist):
  ax.text(d-0.01,t-0.05,"{:.4f}".format(d),color=textcolor,verticalalignment='center',horizontalalignment='right')

ax.set_xlabel('Variance of angles [rad${}^2$]')
#ax.set_ylabel(r'')
ax.set_yticks(tlist)
ax.set_yticklabels(labels)
plt.grid(which='major', axis='x')
#ax.set_ylim(0,0.8)

#plt.legend([rects1[0]], ['Standard deviation of \nrelative element lengths', 'Duration [s]'], fontsize=16, loc='upper center')
# Add some text for labels, title and custom x-axis tick labels, etc.

fig.tight_layout()
plt.savefig("mesh_quality_options.pdf")
plt.show()
