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
#filename = "mesh_quality.csv"
#data = np.genfromtxt(filename, delimiter=";")

# columns:
# 0 triangulation_type; 
# 1 parametric_space_shape; 
# 2 improve_mesh; 
# 3 debugging_stl_output; n_grid_points_x; n_grid_points_y; number of rings; 
# 7 standard deviation of distance; 
# 8 standard deviation of relative distances (distance/mean distance on every slice); 
# 9 duration

# triangulation_type:  0 = scipy, 1 = triangle, 2 = custom (1 is best), 3 = optimized
# 1=0, 2=1, 3=2
# triangulation_type has to be in order 0,1,2

# parametric_space_shape: 0 = unit circle, 1 = unit square, 2 = unit square with adjusted grid, 3 = unit circle with adjusted grid
# □1=1, □2=2, ◯1=0, ◯2=3
# parametric_space_shape has to be in order 1,2,0,3
# !! Make sure that this holds for the input file !!

# the following is a valid input file:
#  # triangulation_type; parametric_space_shape; improve_mesh; debugging_stl_output; n_grid_points_x; n_grid_points_y; number of rings; standard deviation of distance; standard deviation of relative distances (distance/mean distance on every slice); duration
#  0;1;False;False;11;11;43;1.2577002603426162;0.30677434379997987;133.49186660395935
#  0;2;False;False;11;11;43;1.3072775652319828;0.3157216838085184;129.96488937182585
#  0;0;False;False;11;11;43;2.9489669391611915;0.6857425432973921;133.4854928869172
#  0;3;False;False;11;11;43;1.6802223895490362;0.3930713960722115;131.50187234085752
#  1;1;False;False;11;11;43;2.4211139435563545;0.4677754398343457;117.01870801573386
#  1;2;False;False;11;11;43;2.4069874142752155;0.46365389579551575;120.55410060181748
#  1;0;False;False;11;11;43;3.3835653027769053;0.6405593618912921;116.78817091009114
#  1;3;False;False;11;11;43;1.4323662501776169;0.32468976711104597;117.20788699615514
#  2;1;False;False;11;11;43;3.274789906191759;0.5889893785739018;72.28535732498858
#  2;2;False;False;11;11;43;3.229022551895105;0.5739286952747706;72.7385680390289
#  2;0;False;False;11;11;43;3.166845902394146;0.6754145244000737;72.75920189492172
#  2;3;False;False;11;11;43;1.3665423019600709;0.31804320311608;73.6103394899983

data = np.array([
  [0,1,False,False,11,11,43,1.2577002603426162,0.30677434379997987,133.49186660395935],
  [0,2,False,False,11,11,43,1.3072775652319828,0.3157216838085184,129.96488937182585],
  [0,0,False,False,11,11,43,2.9489669391611915,0.6857425432973921,133.4854928869172],
  [0,3,False,False,11,11,43,1.6802223895490362,0.3930713960722115,131.50187234085752],
  [1,1,False,False,11,11,43,2.4211139435563545,0.4677754398343457,117.01870801573386],
  [1,2,False,False,11,11,43,2.4069874142752155,0.46365389579551575,120.55410060181748],
  [1,0,False,False,11,11,43,3.3835653027769053,0.6405593618912921,116.78817091009114],
  [1,3,False,False,11,11,43,1.4323662501776169,0.32468976711104597,117.20788699615514],
  [2,1,False,False,11,11,43,3.274789906191759,0.5889893785739018,72.28535732498858],
  [2,2,False,False,11,11,43,3.229022551895105,0.5739286952747706,72.7385680390289],
  [2,0,False,False,11,11,43,3.166845902394146,0.6754145244000737,72.75920189492172],
  [2,3,False,False,11,11,43,1.3665423019600709,0.31804320311608,73.6103394899983],
])

labels = [
  u'□1', u'□2', u'◯1', u'◯2',
  u'□1', u'□2', u'◯1', u'◯2',
  u'□1', u'□2', u'◯1', u'◯2',
]
plt.rcParams.update({'font.size': 22})

x = np.array([0.0,1.,2.,3., 5.,6.,7.,8., 10.,11.,12.,13.])  # the label locations
#x = np.arange(len(labels))  # the label locations
print(x)
width = 0.35  # the width of the bars

color = (0.8,0.2,0.2)
fig, ax = plt.subplots(figsize=(14,8))
rects1 = ax.bar(x - width/2 - width*0.1, list(data[:,8]), width, color=color)
ax.set_ylabel('Standard deviation [-]')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.spines['left'].set_color(color)
ax.spines['right'].set_color(color)
ax.tick_params(axis='y', colors=color)
ax.yaxis.label.set_color(color)
ax.text(1.5, -0.1, "Triangulation 1", horizontalalignment='center')
ax.text(6.5, -0.1, "Triangulation 2", horizontalalignment='center')
ax.text(11.5, -0.1, "Triangulation 3", horizontalalignment='center')
ax.set_ylim(0,0.8)

color2 = (0.7,0.7,0.0)
color2b = (0.5,0.5,0.0)
ax2 = ax.twinx()
rects2 = ax2.bar(x + width/2 + width*0.1, list(data[:,9]), width, label='', color=color2)
ax2.set_ylabel('Mesh generation runtime [s]')
ax2.spines['right'].set_color(color2b)
ax2.tick_params(axis='y', colors=color2b)
ax2.yaxis.label.set_color(color2b)
ax2.set_ylim(0,160)
ax.grid(which='major', axis='y')

plt.legend([rects1[0],rects2[0]], ['Standard deviation of \nrelative element lengths', 'Mesh generation runtime [s]'], fontsize=16, loc='upper center')
# Add some text for labels, title and custom x-axis tick labels, etc.

#fig.tight_layout()
plt.savefig("mesh_quality.pdf")
plt.show()
