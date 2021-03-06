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
  [0,0,961,0.009207047641658117,0.13630521542049936],  # 31x31fibers_l1_m1_n4_qN1s_stl_i.no_boundary.bin
  [0,0,961,0.00842558142873716,0.1364137037704869],  # 31x31fibers_l1_m1_n4_qN2s_stl_i.no_boundary.bin
  [0,0,961,0.008357521764688947,0.136426368252718],  # 31x31fibers_l1_m1_n4_qN3s_stl_i.no_boundary.bin
  [0,0,961,0.008254995299047874,0.13736601291283357],  # 31x31fibers_l1_m1_n4_lN3s_stl_i.no_boundary.bin
  [0,0,961,0.008261753820951642,0.13812111253064582],  # 31x31fibers_l1_m1_n4_lN2s_stl_i.no_boundary.bin
  [0,0,961,0.00832645628230525,0.13902686665706845],  # 31x31fibers_l1_m1_n4_lN1s_stl_i.no_boundary.bin
  [0,0,961,0.00937505779596801,0.13941976300628128],  # 31x31fibers_l1_m1_n4_lD2gstl_i.no_boundary.bin
  [0,0,961,0.008393926736294235,0.13953869782677517],  # 31x31fibers_l1_m1_n4_qD2s_stl_i.no_boundary.bin
  [0,0,961,0.008284945928878415,0.13958944556192845],  # 31x31fibers_l1_m1_n4_qD1s_stl_i.no_boundary.bin
  [0,0,961,0.008779987688150347,0.14073744863437396],  # 31x31fibers_l1_m1_n4_qD3s_stl_i.no_boundary.bin
  [0,0,961,0.00832810248431571,0.14086194839986355],  # 31x31fibers_l1_m1_n4_lD3s_stl_i.no_boundary.bin
  [0,0,961,0.00804071564555107,0.14107481519214615],  # 31x31fibers_l1_m1_n4_lD2s_stl_i.no_boundary.bin
  [0,0,961,0.007963460398338127,0.1419521638251051],  # 31x31fibers_l1_m1_n4_lD1s_stl_i.no_boundary.bin
  [0,0,961,0.011083960504678268,0.14327642693121156],  # 31x31fibers_l1_m1_n4_lN2gstl_i.no_boundary.bin
  [0,0,961,0.01124856925083364,0.146324964076447],  # 31x31fibers_l1_m1_n4_lD1gstl_i.no_boundary.bin
  [0,0,961,0.1898623791333157,0.1476048391938951],  # 31x31fibers_l1_m1_n4_lN3gstl_i.no_boundary.bin
  [0,0,961,0.23077562969538115,0.15434445671209043],  # 31x31fibers_l1_m1_n4_lD3gstl_i.no_boundary.bin
  
  [0,0,961,0.025325334940143027,0.17180355701558128],  # 31x31fibers_l1_m1_n4_qN1s_splines_i.no_boundary.bin
  [0,0,961,0.02353197544390207,0.17215551074529672],  # 31x31fibers_l1_m1_n4_qN3s_splines_i.no_boundary.bin
  [0,0,961,0.02362565370716781,0.17216790016706393],  # 31x31fibers_l1_m1_n4_qN2s_splines_i.no_boundary.bin
  [0,0,961,0.02279069343729177,0.17303847377613202],  # 31x31fibers_l1_m1_n4_lN3s_splines_i.no_boundary.bin
  [0,0,961,0.02256885014109251,0.17373766086401768],  # 31x31fibers_l1_m1_n4_lN2s_splines_i.no_boundary.bin
  [0,0,961,0.02172551863866662,0.17570834792809492],  # 31x31fibers_l1_m1_n4_lN1s_splines_i.no_boundary.bin
  [0,0,961,0.023090891085746173,0.17642000854213855],  # 31x31fibers_l1_m1_n4_qD2s_splines_i.no_boundary.bin
  [0,0,961,0.0235189753778893,0.17669639456493952],  # 31x31fibers_l1_m1_n4_qD1s_splines_i.no_boundary.bin
  [0,0,961,0.02262334513170297,0.1775006588346218],  # 31x31fibers_l1_m1_n4_lD3s_splines_i.no_boundary.bin
  [0,0,961,0.02318735053418354,0.1776304156447477],  # 31x31fibers_l1_m1_n4_qD3s_splines_i.no_boundary.bin
  [0,0,961,0.022513404683013924,0.178339151364342],  # 31x31fibers_l1_m1_n4_lD2s_splines_i.no_boundary.bin
  [0,0,961,0.021976329915120444,0.1800369480233215],  # 31x31fibers_l1_m1_n4_lD1s_splines_i.no_boundary.bin
  [0,0,961,0.023570567760521324,0.18126217220267465],  # 31x31fibers_l1_m1_n4_lD2gsplines_i.no_boundary.bin
  [0,0,961,0.14138016822249463,0.1867526253339399],  # 31x31fibers_l1_m1_n4_lN3gsplines_i.no_boundary.bin
  [0,0,961,0.5440973271164149,0.18890705819503686],  # 31x31fibers_l1_m1_n4_lD1gsplines_i.no_boundary.bin
  [0,0,961,0.22203189014440647,0.1972393222674189],  # 31x31fibers_l1_m1_n4_lD3gsplines_i.no_boundary.bin
  [0,0,961,0.9499203558443023,0.2077006101125799],  # 31x31fibers_l1_m1_n4_lN2gsplines_i.no_boundary.bin
  [0,0,961,0.9837357563225981,0.22652401674723224],  # 31x31fibers_l1_m1_n4_lN1gsplines_i.no_boundary.bin
])
# columns:
# 0 scenario name; filename; n valid fibers; variance element lengths; variance angles
# 1 filename; 
# 2 n valid fibers; 
# 3 variance element lengths; 
# 4 variance angles; 

all_labels = [
  "qN1s_stl", "qN2s_stl", "qN3s_stl", "$\ell$N3s_stl", "$\ell$N2s_stl", "$\ell$N1s_stl", "$\ell$D2g_stl", "qD2s_stl", "qD1s_stl", "qD3s_stl", "$\ell$D3s_stl", "$\ell$D2s_stl", "$\ell$D1s_stl", "$\ell$N2g_stl", "$\ell$D1g_stl", "$\ell$N3g_stl", "$\ell$D3g_stl", "qN1s_splines", "qN3s_splines", "qN2s_splines", "$\ell$N3s_splines", "$\ell$N2s_splines", "$\ell$N1s_splines", "qD2s_splines", "qD1s_splines", "$\ell$D3s_splines", "qD3s_splines", "$\ell$D2s_splines", "$\ell$D1s_splines", "$\ell$D2g_splines", "$\ell$N3g_splines", "$\ell$D1g_splines", "$\ell$D3g_splines", "$\ell$N2g_splines", "$\ell$N1g_splines"
]
plt.rcParams.update({'font.size': 16})

for i in range(2):
  if i == 0:
    labels = all_labels[0:17]
    datalist = data[0:17,4]
  else:
    labels = all_labels[17:]
    datalist = data[17:,4]
    
  tlist = np.arange(len(labels))  # the label locations
      
  width = 0.7  # the width of the bars

  # reverse direction
  #tlist = list(reversed(tlist))
  labels = list(reversed(labels))
  datalist = list(reversed(datalist))

  textcolor = "#800000"
  textcolor = "k"
  color = "#ffcc00"
  fig, ax = plt.subplots(figsize=(5,8))
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
  plt.savefig("mesh_quality_options_{}.pdf".format(i))

plt.show()
