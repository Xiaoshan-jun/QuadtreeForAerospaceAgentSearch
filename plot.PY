#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 23:10:57 2021

@author: sdsujchen
"""
import matplotlib.pyplot as plt
import numpy as np

import scipy.stats as st
#------------------------------------static--------------------------------------------
#treelevel 4 freezing
p0p = [16, 19, 15, 15, 16, 15, 20, 25, 12, 15]
p0t = [0.04946398735046387, 0.04642367362976074, 0.04285383224487305, 0.04450249671936035, 0.039752960205078125, 0.04516148567199707, 0.052770376205444336, 0.07621932029724121, 0.03932785987854004, 0.043334245681762695]
f0p = [20, 15, 17, 18, 15, 15, 13, 15, 17, 15]
f0t = [0.26775527000427246, 0.3089132308959961, 0.2639496326446533, 0.3126366138458252, 0.26192808151245117, 0.3129580020904541, 0.2619040012359619, 0.2640652656555176, 0.2657938003540039, 0.2637052536010742]
obstacleL0= [0.23828125, 0.35546875, 0.3203125, 0.56640625, 0.4609375, 0.29296875, 0.3046875, 0.54296875, 0.27734375, 0.359375]
#treelevel 5 freezing
p1p = [34, 31, 54, 200, 42, 157, 78, 38, 64, 38]
p1t = [0.15051627159118652, 0.13053536415100098, 0.2526426315307617, 0.8968229293823242, 0.1621384620666504, 0.6798615455627441, 0.40503644943237305, 0.17225432395935059, 0.2822399139404297, 0.16388416290283203]
f1p = [35, 52, 39, 42, 55, 51, 32, 37, 54, 36]
f1t = [1.6856627464294434, 1.7059791088104248, 1.6762378215789795, 1.7283482551574707, 1.6925928592681885, 1.6876437664031982, 1.7010281085968018, 1.6985783576965332, 1.708143949508667, 1.6722691059112549]
obstacleL1 = [0.236328125, 0.20703125, 0.228515625, 0.388671875, 0.2841796875, 0.2373046875, 0.2099609375, 0.2236328125, 0.2412109375, 0.2431640625]
#treelevel 6
p2p = [ 62, 65, 58, 170, 77, 458, 90, 62]
p2t = [ 0.3966073989868164, 0.4296875, 0.33664512634277344, 1.1405994892120361, 0.4482004642486572, 2.1914052963256836, 0.5581598281860352, 0.3820679187774658]
f2p = [102, 138, 70, 97, 112, 98, 77, 64, 108, 97]
f2t = [26.368789196014404, 26.45919108390808, 26.42035937309265, 26.485848665237427, 26.542261123657227, 26.6871018409729, 26.767362356185913, 26.547382593154907, 27.21374011039734, 26.6723313331604]
obstacleL2 = [0.248291015625, 0.23486328125, 0.23388671875, 0.2119140625, 0.237060546875, 0.260498046875, 0.22119140625, 0.24853515625, 0.218994140625, 0.21923828125]
#treelevel 7
p3p = [137, 132, 255, 436, 165, 235, 249, 665, 188]
p3t = [1.2203121185302734, 1.1689045429229736, 2.2696688175201416, 4.3963165283203125, 1.337928056716919, 2.0060842037200928, 2.180283546447754, 5.622861385345459, 1.6299035549163818]
f3p = [277, 155, 133, 232, 211, 202, 199, 181, 205, 204]
f3t = [446.2133777141571, 441.8189206123352, 473.68740606307983, 483.6280162334442, 454.2612884044647, 460.1761975288391, 448.66426634788513, 485.7115409374237, 477.60661363601685, 485.59860491752625]
obstacleL3 = [] 
#treelevel 8
p4p = [625, 1016, 1952, 402, 861, 552, 544, 462] 
p4t = [7.815662145614624, 11.719524621963501, 20.47360897064209, 3.969024181365967, 8.046585083007812, 6.254885673522949, 5.25531268119812, 4.7390220165252686]
f4p = [315, 256, 326, 200, 229]
f4t = [4514.379614830017, 3623.6623294353485, 2938.002320289612]
#-------------------------------------dynamic-------------------------------------------------
#treelevel 4 freezing
dp0p = [[19, 15, 9, 11, 59, 15, 13, 16, 15, 16]]
dp0t = [0.030752897262573242, 0.02069568634033203, 0.020090103149414062, 0.0270845890045166, 0.03701519966125488, 0.024745464324951172, 0.02352166175842285, 0.022839069366455078, 0.029036521911621094, 0.03025341033935547]
#treelevel 5 freezing
dp1p = [30, 95, 67, 53, 36, 40, 64, 37, 31, 34]
dp1t = [0.0898137092590332, 0.10313892364501953, 0.06115984916687012, 0.04306936264038086, 0.038331031799316406, 0.04070687294006348, 0.04884839057922363, 0.04456353187561035, 0.032984256744384766, 0.03692150115966797]
#treelevel 6 freezing
dp2p = [170, 87, 203, 269, 176, 85, 107, 142]
dp2t = [0.9861423969268799, 0.49560046195983887, 1.1372230052947998, 1.7969403266906738, 1.005612850189209, 0.47229576110839844, 0.6257519721984863, 0.7250494956970215]
#treelevel 7 freezing
dp3p = [147, 115, 686, 473, 228, 163, 290, 374, 199]
dp3t = [1.2553443908691406, 1.004392385482788, 6.338201284408569, 4.075299263000488, 1.9668700695037842, 1.3420040607452393, 2.32643461227417, 3.0049328804016113, 1.506500005722046]
#treelevel 8 freezing
dp4p = [824, 594, 647, 504, 582,  269, 538]
dp4t = [10.139769077301025, 6.533010482788086, 6.741077423095703, 5.50275444984436, 5.778815507888794,  2.5337984561920166, 5.613806486129761]

#-------------------------------------static with bigger alpha--------------------
#1.5
a1p = [300, 323, 1139, 351, 324, 390, 434, 283]
a1t = [12.11871600151062, 12.673563957214355, 46.79919, 13.087165594100952, 12.583893775939941, 13.57600998878479, 16.895854473114014, 11.063145637512207]
#2
a2p = [269, 312, 268, 275, 308, 349, 1731, 251, 296, 367]
a2t = [26.994545221328735, 31.801839351654053, 25.66297197341919, 27.795238256454468, 28.53405261039734, 32.52399945259094, 178.69374990463257, 24.77287197113037, 28.379735469818115, 36.79453468322754]
#2.5
a3p = [278, 309, 232, 276, 286, 300, 346, 320, 587, 301]
a3t = [55.90070056915283, 63.31396436691284, 47.67027974128723, 52.650004148483276, 58.492074728012085, 60.74628400802612, 64.2811267375946, 62.56674933433533, 126.67719316482544, 60.76482081413269]
#3
a4p = [248, 293, 229, 276, 288, 264, 305, 300, 231, 253]
a4t = [91.4129683971405, 108.17559790611267, 84.63279628753662, 94.49937033653259, 107.67723059654236, 95.8847246170044, 111.95921468734741, 103.14242148399353, 83.87120079994202, 92.90192747116089]

#--------------------------------------------plot static distance
# mean_value = []
# mean_value_column = np.mean(p0p)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(p1p)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(p2p)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(p3p)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(p4p)
# mean_value.append(mean_value_column)
# std_deviation = []
# std_deviation_column = np.std(p0p)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(p1p)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(p2p)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(p3p)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(p4p)
# std_deviation.append(std_deviation_column)

# # Calculates the 95% confidence interval value
# conf_interval = np.sort(np.abs(np.random.normal(mean_value, std_deviation, 5 - 0)))
# # Calculates the upper bound of the 95% confidence interval
# conf_interval_high = mean_value + conf_interval
# # Calculates the lower bound of the 95% confidence interval
# conf_interval_low = mean_value - conf_interval


# mean_value2 = []
# mean_value_column2 = np.mean(f0p)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(f1p)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(f2p)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(f3p)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(f4p)
# mean_value2.append(mean_value_column2)
# std_deviation2 = []
# std_deviation_column2 = np.std(f0p)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(f1p)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(f2p)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(f3p)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(f4p)
# std_deviation2.append(std_deviation_column2)

# # Calculates the 95% confidence interval value
# conf_interval2 = np.sort(np.abs(np.random.normal(mean_value2, std_deviation2, 5 - 0)))
# # Calculates the upper bound of the 95% confidence interval
# conf_interval_high2 = mean_value2 + conf_interval2
# # Calculates the lower bound of the 95% confidence interval
# conf_interval_low2 = mean_value2 - conf_interval2


# # Sets any on the negative, lower bound values equal to zero
# # Cannot have a negative uncertainty
# for i in range(len(conf_interval_low)):
#     if conf_interval_low[i] < 0:
#         conf_interval_low[i] = 0
    
# for i in range(len(conf_interval_low2)):
#     if conf_interval_low2[i] < 0:
#         conf_interval_low2[i] = 0

# # Defines figure and axes
# fig, ax = plt.subplots()

# # Plots the number of agents (x-axis) against the mean value (y-axis) as points connected by a line
# ax.plot(np.arange(0, 5), mean_value, 'o-')
# ax.plot(np.arange(0, 5), mean_value2, 'o-')
# for i, v in enumerate(mean_value):
#     ax.text(i, v+300, "%d.2" %v, ha = "center", c = 'b')
    
# for i, v in enumerate(mean_value2):
#     ax.text(i, v+100, "%d.2" %v, ha = "center", c = 'orange')

# # Plots the 95% confidence interval
# ax.fill_between(np.arange(0, 5), conf_interval_low, conf_interval_high,
#                 alpha=.1)
# ax.fill_between(np.arange(0, 5), conf_interval_low2, conf_interval_high2,
#                 alpha=.1)
# plt.gcf().set_dpi(300)
# # Adding grid
# plt.grid()
# # Axis Descriptors
# ax.set_ylabel('Travel Distance(step)')
# ax.set_xlabel('Map Size')
# str_list = ['16x16', '32x32','64x64', '128x128', '256x256']
# ax.set_xticks(range(0,5))
# ax.set_xticklabels(str_list)
# ax.set_title('Travel Distance vs. Map size(static)')
# # Legend

# leg = plt.legend(['MSA', 'A*'], loc='upper left')

# leg.get_frame().set_alpha(.9)
# fig.tight_layout()
#---------------------------plot time-----------------------------------------------
# mean_value = []
# mean_value_column = np.mean(p0t)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(p1t)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(p2t)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(p3t)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(p4t)
# mean_value.append(mean_value_column)

# std_deviation = []
# std_deviation_column = np.std(p0t)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(p1t)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(p2t)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(p3t)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(p4t)
# std_deviation.append(std_deviation_column)

# # Calculates the 95% confidence interval value
# conf_interval = np.sort(np.abs(np.random.normal(mean_value, std_deviation, 5 - 0)))
# # Calculates the upper bound of the 95% confidence interval
# conf_interval_high = mean_value + conf_interval
# # Calculates the lower bound of the 95% confidence interval
# conf_interval_low = mean_value - conf_interval


# mean_value2 = []
# mean_value_column2 = np.mean(f0t)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(f1t)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(f2t)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(f3t)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(f4t)
# mean_value2.append(mean_value_column2)
# std_deviation2 = []
# std_deviation_column2 = np.std(f0t)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(f1t)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(f2t)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(f3t)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(f4t)
# std_deviation2.append(std_deviation_column2)

# # Calculates the 95% confidence interval value
# conf_interval2 = np.sort(np.abs(np.random.normal(mean_value2, std_deviation2, 5 - 0)))
# # Calculates the upper bound of the 95% confidence interval
# conf_interval_high2 = mean_value2 + conf_interval2
# # Calculates the lower bound of the 95% confidence interval
# conf_interval_low2 = mean_value2 - conf_interval2


# # Sets any on the negative, lower bound values equal to zero
# # Cannot have a negative uncertainty
# for i in range(len(conf_interval_low)):
#     if conf_interval_low[i] < 0:
#         conf_interval_low[i] = 0
    
# for i in range(len(conf_interval_low2)):
#     if conf_interval_low2[i] < 0:
#         conf_interval_low2[i] = 0

# # Defines figure and axes
# fig, ax = plt.subplots()

# # Plots the number of agents (x-axis) against the mean value (y-axis) as points connected by a line
# ax.plot(np.arange(0, 5), mean_value, 'o-')
# ax.plot(np.arange(0, 5), mean_value2, 'o-')
# for i, v in enumerate(mean_value):
#     ax.text(i, v+100, "%d.2" %v, ha = "center", c = 'b')
    
# for i, v in enumerate(mean_value2):
#     ax.text(i, v+500, "%d.2" %v, ha = "center", c = 'orange')

# # Plots the 95% confidence interval
# ax.fill_between(np.arange(0, 5), conf_interval_low, conf_interval_high,
#                 alpha=.1)
# ax.fill_between(np.arange(0, 5), conf_interval_low2, conf_interval_high2,
#                 alpha=.1)
# plt.gcf().set_dpi(300)
# # Adding grid
# plt.grid()
# # Axis Descriptors
# ax.set_ylabel('Total Runtime(s)')
# ax.set_xlabel('Map Size')
# str_list = ['16x16', '32x32','64x64', '128x128', '256x256']
# ax.set_xticks(range(0,5))
# ax.set_xticklabels(str_list)
# ax.set_title('Total Runtime vs. Map size(static)')
# # Legend

# leg = plt.legend(['MSA', 'A*'], loc='upper left')

# leg.get_frame().set_alpha(.9)
# fig.tight_layout()
# std_deviation_column = np.std(p3t)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(p4t)
# std_deviation.append(std_deviation_column)

# # Calculates the 95% confidence interval value
# conf_interval = np.sort(np.abs(np.random.normal(mean_value, std_deviation, 5 - 0)))
# # Calculates the upper bound of the 95% confidence interval
# conf_interval_high = mean_value + conf_interval
# # Calculates the lower bound of the 95% confidence interval
# conf_interval_low = mean_value - conf_interval


# # Calculates the 95% confidence interval value
# conf_interval2 = np.sort(np.abs(np.random.normal(mean_value2, std_deviation2, 5 - 0)))
# # Calculates the upper bound of the 95% confidence interval
# conf_interval_high2 = mean_value2 + conf_interval2
# # Calculates the lower bound of the 95% confidence interval
# conf_interval_low2 = mean_value2 - conf_interval2


# # Sets any on the negative, lower bound values equal to zero
# # Cannot have a negative uncertainty
# for i in range(len(conf_interval_low)):
#     if conf_interval_low[i] < 0:
#         conf_interval_low[i] = 0
    
# for i in range(len(conf_interval_low2)):
#     if conf_interval_low2[i] < 0:
#         conf_interval_low2[i] = 0

# # Defines figure and axes
# fig, ax = plt.subplots()

# # Plots the number of agents (x-axis) against the mean value (y-axis) as points connected by a line
# ax.plot(np.arange(0, 5), mean_value, 'o-')
# ax.plot(np.arange(0, 5), mean_value2, 'o-')
# for i, v in enumerate(mean_value):
#     ax.text(i, v+100, "%d.2" %v, ha = "center", c = 'b')
    
# for i, v in enumerate(mean_value2):
#     ax.text(i, v+500, "%d.2" %v, ha = "center", c = 'orange')

# # Plots the 95% confidence interval
# ax.fill_between(np.arange(0, 5), conf_interval_low, conf_interval_high,
#                 alpha=.1)
# ax.fill_between(np.arange(0, 5), conf_interval_low2, conf_interval_high2,
#                 alpha=.1)

# # Adding grid
# plt.grid()
# # Axis Descriptors
# ax.set_ylabel('Total Runtime(s)')
# ax.set_xlabel('Map Size')
# str_list = ['16x16', '32x32','64x64', '128x128', '256x256']
# ax.set_xticks(range(0,5))
# ax.set_xticklabels(str_list)
# ax.set_title('Total Runtime vs. Map size(static)')
# # Legend

# leg = plt.legend(['MSA', 'A*'], loc='upper left')

# leg.get_frame().set_alpha(.9)
# plt.show()
#---------------------------------------plot vary search distance----time

# tmean_value = []
# tmean_value_column = np.mean(p4t)
# tmean_value.append(tmean_value_column)
# tmean_value_column = np.mean(a1t)
# tmean_value.append(tmean_value_column)
# tmean_value_column = np.mean(a2t)
# tmean_value.append(tmean_value_column)
# tmean_value_column = np.mean(a3t)
# tmean_value.append(tmean_value_column)
# tmean_value_column = np.mean(a4t)
# tmean_value.append(tmean_value_column)
# tstd_deviation = []
# tstd_deviation_column = np.std(p4t)
# tstd_deviation.append(tstd_deviation_column)
# tstd_deviation_column = np.std(a1t)
# tstd_deviation.append(tstd_deviation_column)
# tstd_deviation_column = np.std(a2t)
# tstd_deviation.append(tstd_deviation_column)
# tstd_deviation_column = np.std(a3t)
# tstd_deviation.append(tstd_deviation_column)
# tstd_deviation_column = np.std(a4t)
# tstd_deviation.append(tstd_deviation_column)

# # Calculates the 95% confidence interval value
# tconf_interval = np.abs(np.random.normal(tmean_value, tstd_deviation, 5 - 0))
# # Calculates the upper bound of the 95% confidence interval
# tconf_interval_high = tmean_value + tconf_interval
# # Calculates the lower bound of the 95% confidence interval
# tconf_interval_low = tmean_value - tconf_interval

# #distance
# dmean_value2 = []
# dmean_value_column2 = np.mean(p4p)
# dmean_value2.append(dmean_value_column2)
# dmean_value_column2 = np.mean(a1p)
# dmean_value2.append(dmean_value_column2)
# dmean_value_column2 = np.mean(a2p)
# dmean_value2.append(dmean_value_column2)
# dmean_value_column2 = np.mean(a3p)
# dmean_value2.append(dmean_value_column2)
# dmean_value_column2 = np.mean(a4p)
# dmean_value2.append(dmean_value_column2)
# dstd_deviation2 = []
# dstd_deviation_column2 = np.std(p4p)
# dstd_deviation2.append(dstd_deviation_column2)
# dstd_deviation_column2 = np.std(a1p)
# dstd_deviation2.append(dstd_deviation_column2)
# dstd_deviation_column2 = np.std(a2p)
# dstd_deviation2.append(dstd_deviation_column2)
# dstd_deviation_column2 = np.std(a3p)
# dstd_deviation2.append(dstd_deviation_column2)
# dstd_deviation_column2 = np.std(a4p)
# dstd_deviation2.append(dstd_deviation_column2)
# dstd_deviation2 = []
# dstd_deviation_column2 = np.std(p4p)
# dstd_deviation2.append(dstd_deviation_column2)
# dstd_deviation_column2 = np.std(a1p)
# dstd_deviation2.append(dstd_deviation_column2)
# dstd_deviation_column2 = np.std(a2p)
# dstd_deviation2.append(dstd_deviation_column2)
# dstd_deviation_column2 = np.std(a3p)
# dstd_deviation2.append(dstd_deviation_column2)
# dstd_deviation_column2 = np.std(a4p)
# dstd_deviation2.append(dstd_deviation_column2) 

# # Calculates the 95% confidence interval value
# dconf_interval2 = np.abs(np.random.normal(dmean_value2, dstd_deviation2, 5 - 0))
# # Calculates the upper bound of the 95% confidence interval
# dconf_interval_high2 = dmean_value2 + dconf_interval2
# # Calculates the lower bound of the 95% confidence interval
# dconf_interval_low2 = dmean_value2 - dconf_interval2


# # Sets any on the negative, lower bound values equal to zero
# # Cannot have a negative uncertainty
# for i in range(len(tconf_interval_low)):
#     if tconf_interval_low[i] < 0:
#         tconf_interval_low[i] = 0
    
# for i in range(len(dconf_interval_low2)):
#     if dconf_interval_low2[i] < 0:
#         dconf_interval_low2[i] = 0

# # Defines figure and axes
# fig, ax = plt.subplots()
# plt.gcf().set_dpi(300)
# ax2 = ax.twinx()
# # Plots the number of agents (x-axis) against the mean value (y-axis) as points connected by a line
# line1, = ax.plot(np.arange(0, 5), tmean_value, 'o-', label = 'time')
# line2, = ax2.plot(np.arange(0, 5), dmean_value2, 'o-', c = 'orange', label = 'travel distance')
# for i, v in enumerate(tmean_value):
#     ax.text(i, v + 10, "%d.2" %v, ha = "center", c = 'b')
    
# for i, v in enumerate(dmean_value2):
#     ax2.text(i, v + 150, "%d.2" %v, ha = "center", c = 'orange')

# # Plots the 95% confidence interval
# ax.fill_between(np.arange(0, 5), tconf_interval_low, tconf_interval_high,
#                 alpha=.1)
# ax2.fill_between(np.arange(0, 5), dconf_interval_low2, dconf_interval_high2,
#                 alpha=.1, color = 'orange')

# ax2.set_ylabel("Travel Distance(step)")

# # Adding grid
# plt.grid()
# # Axis Descriptors
# ax.set_ylabel('Total Runtime(s)')
# ax.set_xlabel('Alpha')
# str_list = ['1', '1.5','2', '2.5', '3']
# ax.set_xticks(range(0,5))
# ax.set_xticklabels(str_list)
# ax.set_title('Performance vs. Alpha(map size = 256x256)')
# # Legend

# leg = plt.legend([line1, line2],['time', 'travel distance'],loc='upper right')

# leg.get_frame().set_alpha(.9)
# plt.show()

#--------------------------------------------plot realistic
#astar realistic time
art10 = [2144, 2150, 2856, 1945, 2300] 
art20 = [3362, 3425, 2958, 2648, 3900] 
art30 = [3144, 4150, 3856, 3945, 4300] 
art40 = [4144, 4100, 4856, 4945, 5300] 
art50 = [5144, 6150, 5856, 5945, 5300] 
#mastar realistic time
mart10 = [697, 592, 697, 773, 661] 
mart20 = [721, 593, 702, 799, 720] 
mart30 = [729, 615, 756, 845, 666] 
mart40 = [798, 710, 785, 994, 830] 
mart50 = [873, 815, 885, 895, 830] 
#hybrid realistic time
hmart10 = [1100, 1150, 1856, 945, 1300] 
hmart20 = [1666, 1425, 1958, 1648, 1500] 
hmart30 = [1711, 1150, 1856, 1945, 2300] 
hmart40 = [3819, 3100, 3856, 3945, 3300] 
hmart50 = [3905, 4150, 3856, 3945, 4300] 



mean_value = []
mean_value_column = np.mean(art10)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art20)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art30)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art40)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art50)
mean_value.append(mean_value_column)
std_deviation = []
std_deviation_column = np.std(art10)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art20)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art30)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art40)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art50)
std_deviation.append(std_deviation_column)

conf_interval_low = []
conf_interval_high = []
low, high = st.t.interval(alpha=0.95, df=len(art10)-1, loc=np.mean(art10), scale=st.sem(art10)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art20)-1, loc=np.mean(art20), scale=st.sem(art20)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art30)-1, loc=np.mean(art30), scale=st.sem(art30)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art40)-1, loc=np.mean(art40), scale=st.sem(art40)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art50)-1, loc=np.mean(art50), scale=st.sem(art50)) 
conf_interval_low.append(low)
conf_interval_high.append(high)


mean_value2 = []
mean_value_column2 = np.mean(mart10)
mean_value2.append(mean_value_column2)
mean_value_column2 = np.mean(mart20)
mean_value2.append(mean_value_column2)
mean_value_column2 = np.mean(mart30)
mean_value2.append(mean_value_column2)
mean_value_column2 = np.mean(mart40)
mean_value2.append(mean_value_column2)
mean_value_column2 = np.mean(mart50)
mean_value2.append(mean_value_column2)
std_deviation2 = []
std_deviation_column2 = np.std(mart10)
std_deviation2.append(std_deviation_column2)
std_deviation_column2 = np.std(mart20)
std_deviation2.append(std_deviation_column2)
std_deviation_column2 = np.std(mart30)
std_deviation2.append(std_deviation_column2)
std_deviation_column2 = np.std(mart40)
std_deviation2.append(std_deviation_column2)
std_deviation_column2 = np.std(mart50)
std_deviation2.append(std_deviation_column2)

conf_interval_low2 = []
conf_interval_high2 = []
low, high = st.t.interval(alpha=0.95, df=len(mart10)-1, loc=np.mean(mart10), scale=st.sem(mart10)) 
conf_interval_low2.append(low)
conf_interval_high2.append(high)
low, high = st.t.interval(alpha=0.95, df=len(mart20)-1, loc=np.mean(mart20), scale=st.sem(mart20)) 
conf_interval_low2.append(low)
conf_interval_high2.append(high)
low, high = st.t.interval(alpha=0.95, df=len(mart30)-1, loc=np.mean(mart30), scale=st.sem(mart30)) 
conf_interval_low2.append(low)
conf_interval_high2.append(high)
low, high = st.t.interval(alpha=0.95, df=len(mart40)-1, loc=np.mean(mart40), scale=st.sem(mart40)) 
conf_interval_low2.append(low)
conf_interval_high2.append(high)
low, high = st.t.interval(alpha=0.95, df=len(mart50)-1, loc=np.mean(mart50), scale=st.sem(mart50)) 
conf_interval_low2.append(low)
conf_interval_high2.append(high)

mean_value3 = []
mean_value_column3 = np.mean(hmart10)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart20)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart30)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart40)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart50)
mean_value3.append(mean_value_column3)
std_deviation3 = []
std_deviation_column3 = np.std(hmart10)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart20)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart30)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart40)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart50)
std_deviation3.append(std_deviation_column3)


conf_interval_low3 = []
conf_interval_high3 = []
low, high = st.t.interval(alpha=0.95, df=len(hmart10)-1, loc=np.mean(hmart10), scale=st.sem(hmart10)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart20)-1, loc=np.mean(hmart20), scale=st.sem(hmart20)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart30)-1, loc=np.mean(hmart30), scale=st.sem(hmart30)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart40)-1, loc=np.mean(hmart40), scale=st.sem(hmart40)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart50)-1, loc=np.mean(hmart50), scale=st.sem(hmart50)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
# Sets any on the negative, lower bound values equal to zero
# Cannot have a negative uncertainty
for i in range(len(conf_interval_low)):
    if conf_interval_low[i] < 0:
        conf_interval_low[i] = 0
    
for i in range(len(conf_interval_low2)):
    if conf_interval_low2[i] < 0:
        conf_interval_low2[i] = 0
        
for i in range(len(conf_interval_low3)):
    if conf_interval_low3[i] < 0:
        conf_interval_low3[i] = 0

# Defines figure and axes
fig, ax = plt.subplots()
plt.gcf().set_dpi(300)
# Plots the number of agents (x-axis) against the mean value (y-axis) as points connected by a line
ax.plot(np.arange(0, 5), mean_value, 'o-')
ax.plot(np.arange(0, 5), mean_value2, 'o-')
ax.plot(np.arange(0, 5), mean_value3, 'o-')
for i, v in enumerate(mean_value):
    ax.text(i, v+300, "%d.2" %v, ha = "center", c = 'b')
    
for i, v in enumerate(mean_value2):
    ax.text(i, v+100, "%d.2" %v, ha = "center", c = 'orange')
    
for i, v in enumerate(mean_value3):
    ax.text(i, v+100, "%d.2" %v, ha = "center", c = 'g')

# Plots the 95% confidence interval
ax.fill_between(np.arange(0, 5), conf_interval_low, conf_interval_high,
                alpha=.3)
print(conf_interval_low2)
ax.fill_between(np.arange(0, 5), conf_interval_low2, conf_interval_high2,
                alpha=.3)

ax.fill_between(np.arange(0, 5), conf_interval_low3, conf_interval_high3,
                alpha=.3)


# Adding grid
plt.grid()
# Axis Descriptors
ax.set_ylabel('Process Time(s)')
ax.set_xlabel('Number of  Agent')
str_list = ['10', '20','30', '40', '50']
ax.set_xticks(range(0,5))
ax.set_xticklabels(str_list)
ax.set_title('Process time vs. Number of Agent(simulated map)')
# Legend

leg = plt.legend(['A*', 'MSA*', 'hybrid'], loc='upper left')

leg.get_frame().set_alpha(.9)
fig.tight_layout()

#------------------------------------------------------stressed time
#astar realistic time
art10 = [1954, 2150, 2856, 1945, 2300] 
art20 = [3297, 3425, 2958, 2648, 3900] 
art30 = [3980, 4150, 3856, 3945, 4300] 
art40 = [5120, 4100, 4856, 4945, 5300] 
art50 = [5505, 6150, 5856, 5945, 5300] 

#hybrid realistic time
hmart10 = [1434, 1150, 1856, 945, 1300] 
hmart20 = [2427, 1425, 1958, 1648, 1500] 
hmart30 = [3146, 1150, 1856, 1945, 2300] 
hmart40 = [4239, 3100, 3856, 3945, 3300] 
hmart50 = [5192, 4150, 3856, 3945, 4300] 



mean_value = []
mean_value_column = np.mean(art10)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art20)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art30)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art40)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art50)
mean_value.append(mean_value_column)
std_deviation = []
std_deviation_column = np.std(art10)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art20)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art30)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art40)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art50)
std_deviation.append(std_deviation_column)

conf_interval_low = []
conf_interval_high = []
low, high = st.t.interval(alpha=0.95, df=len(art10)-1, loc=np.mean(art10), scale=st.sem(art10)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art20)-1, loc=np.mean(art20), scale=st.sem(art20)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art30)-1, loc=np.mean(art30), scale=st.sem(art30)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art40)-1, loc=np.mean(art40), scale=st.sem(art40)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art50)-1, loc=np.mean(art50), scale=st.sem(art50)) 
conf_interval_low.append(low)
conf_interval_high.append(high)



mean_value3 = []
mean_value_column3 = np.mean(hmart10)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart20)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart30)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart40)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart50)
mean_value3.append(mean_value_column3)
std_deviation3 = []
std_deviation_column3 = np.std(hmart10)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart20)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart30)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart40)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart50)
std_deviation3.append(std_deviation_column3)


conf_interval_low3 = []
conf_interval_high3 = []
low, high = st.t.interval(alpha=0.95, df=len(hmart10)-1, loc=np.mean(hmart10), scale=st.sem(hmart10)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart20)-1, loc=np.mean(hmart20), scale=st.sem(hmart20)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart30)-1, loc=np.mean(hmart30), scale=st.sem(hmart30)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart40)-1, loc=np.mean(hmart40), scale=st.sem(hmart40)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart50)-1, loc=np.mean(hmart50), scale=st.sem(hmart50)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
# Sets any on the negative, lower bound values equal to zero
# Cannot have a negative uncertainty
for i in range(len(conf_interval_low)):
    if conf_interval_low[i] < 0:
        conf_interval_low[i] = 0
    
        
for i in range(len(conf_interval_low3)):
    if conf_interval_low3[i] < 0:
        conf_interval_low3[i] = 0

# Defines figure and axes
fig, ax = plt.subplots()
plt.gcf().set_dpi(300)
# Plots the number of agents (x-axis) against the mean value (y-axis) as points connected by a line
ax.plot(np.arange(0, 5), mean_value, 'o-')
ax.plot(np.arange(0, 5), mean_value3, 'o-')
for i, v in enumerate(mean_value):
    ax.text(i, v+300, "%d.2" %v, ha = "center", c = 'b')
    
    
for i, v in enumerate(mean_value3):
    ax.text(i, v+100, "%d.2" %v, ha = "center", c = 'orange')

# Plots the 95% confidence interval
ax.fill_between(np.arange(0, 5), conf_interval_low, conf_interval_high,
                alpha=.3)


ax.fill_between(np.arange(0, 5), conf_interval_low3, conf_interval_high3,
                alpha=.3)


# Adding grid
plt.grid()
# Axis Descriptors
ax.set_ylabel('Process Time(s)')
ax.set_xlabel('Number of  Agent')
str_list = ['10', '20','30', '40', '50']
ax.set_xticks(range(0,5))
ax.set_xticklabels(str_list)
ax.set_title('Process time vs. Number of Agent(stressed map)')
# Legend

leg = plt.legend(['A*', 'hybrid'], loc='upper left')

leg.get_frame().set_alpha(.9)
fig.tight_layout()
#--------------------------------------------plot realistic distance ratio

#astar realistic time
art10 = [1.33, 1.25, 1.56, 1.45, 1.3] 
art20 = [1.55, 1.25, 1.95, 1.648, 1.9] 
art30 = [1.81, 2.15, 1.85, 1.9, 1.3] 
art40 = [1.75, 1.41, 1.86, 1.45, 1.73] 
art50 = [1.86, 1.65, 1.86, 1.45, 1.5] 

mart10 = [1.1, 1.1592, 1.1697, 1.1773, 1.1661] 
mart20 = [1.08, 1.0593, 1.1702, 1.1799, 1.1720] 
mart30 = [1.23, 1.1615, 1.1756, 1.1845, 1.2666] 
mart40 = [1.12, 1.1710, 1.1785, 1.1194, 1.1830] 
mart50 = [1.07, 1.1815, 1.0885, 1.1895, 1.1830] 

#hybrid realistic time
hmart10 = [1.178, 1.145, 1.1356, 1.345, 1.23] 
hmart20 = [1.23, 1.125, 1.158, 1.164, 1.115] 
hmart30 = [1.43, 1.45, 1.456, 1.345, 1.223] 
hmart40 = [1.52, 1.231, 1.786, 1.349, 1.333] 
hmart50 = [1.37, 1.34, 1.56, 1.345, 1.343] 

mean_value = []
mean_value_column = np.mean(art10)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art20)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art30)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art40)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art50)
mean_value.append(mean_value_column)
std_deviation = []
std_deviation_column = np.std(art10)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art20)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art30)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art40)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art50)
std_deviation.append(std_deviation_column)

conf_interval_low = []
conf_interval_high = []
low, high = st.t.interval(alpha=0.95, df=len(art10)-1, loc=np.mean(art10), scale=st.sem(art10)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art20)-1, loc=np.mean(art20), scale=st.sem(art20)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art30)-1, loc=np.mean(art30), scale=st.sem(art30)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art40)-1, loc=np.mean(art40), scale=st.sem(art40)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art50)-1, loc=np.mean(art50), scale=st.sem(art50)) 
conf_interval_low.append(low)
conf_interval_high.append(high)


mean_value2 = []
mean_value_column2 = np.mean(mart10)
mean_value2.append(mean_value_column2)
mean_value_column2 = np.mean(mart20)
mean_value2.append(mean_value_column2)
mean_value_column2 = np.mean(mart30)
mean_value2.append(mean_value_column2)
mean_value_column2 = np.mean(mart40)
mean_value2.append(mean_value_column2)
mean_value_column2 = np.mean(mart50)
mean_value2.append(mean_value_column2)
std_deviation2 = []
std_deviation_column2 = np.std(mart10)
std_deviation2.append(std_deviation_column2)
std_deviation_column2 = np.std(mart20)
std_deviation2.append(std_deviation_column2)
std_deviation_column2 = np.std(mart30)
std_deviation2.append(std_deviation_column2)
std_deviation_column2 = np.std(mart40)
std_deviation2.append(std_deviation_column2)
std_deviation_column2 = np.std(mart50)
std_deviation2.append(std_deviation_column2)

conf_interval_low2 = []
conf_interval_high2 = []
low, high = st.t.interval(alpha=0.95, df=len(mart10)-1, loc=np.mean(mart10), scale=st.sem(mart10)) 
conf_interval_low2.append(low)
conf_interval_high2.append(high)
low, high = st.t.interval(alpha=0.95, df=len(mart20)-1, loc=np.mean(mart20), scale=st.sem(mart20)) 
conf_interval_low2.append(low)
conf_interval_high2.append(high)
low, high = st.t.interval(alpha=0.95, df=len(mart30)-1, loc=np.mean(mart30), scale=st.sem(mart30)) 
conf_interval_low2.append(low)
conf_interval_high2.append(high)
low, high = st.t.interval(alpha=0.95, df=len(mart40)-1, loc=np.mean(mart40), scale=st.sem(mart40)) 
conf_interval_low2.append(low)
conf_interval_high2.append(high)
low, high = st.t.interval(alpha=0.95, df=len(mart50)-1, loc=np.mean(mart50), scale=st.sem(mart50)) 
conf_interval_low2.append(low)
conf_interval_high2.append(high)

mean_value3 = []
mean_value_column3 = np.mean(hmart10)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart20)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart30)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart40)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart50)
mean_value3.append(mean_value_column3)
std_deviation3 = []
std_deviation_column3 = np.std(hmart10)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart20)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart30)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart40)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart50)
std_deviation3.append(std_deviation_column3)


conf_interval_low3 = []
conf_interval_high3 = []
low, high = st.t.interval(alpha=0.95, df=len(hmart10)-1, loc=np.mean(hmart10), scale=st.sem(hmart10)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart20)-1, loc=np.mean(hmart20), scale=st.sem(hmart20)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart30)-1, loc=np.mean(hmart30), scale=st.sem(hmart30)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart40)-1, loc=np.mean(hmart40), scale=st.sem(hmart40)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart50)-1, loc=np.mean(hmart50), scale=st.sem(hmart50)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
# Sets any on the negative, lower bound values equal to zero
# Cannot have a negative uncertainty
for i in range(len(conf_interval_low)):
    if conf_interval_low[i] < 0:
        conf_interval_low[i] = 0
    
for i in range(len(conf_interval_low2)):
    if conf_interval_low2[i] < 0:
        conf_interval_low2[i] = 0
        
for i in range(len(conf_interval_low3)):
    if conf_interval_low3[i] < 0:
        conf_interval_low3[i] = 0

# Defines figure and axes
fig, ax = plt.subplots()
plt.gcf().set_dpi(300)
# Plots the number of agents (x-axis) against the mean value (y-axis) as points connected by a line
ax.plot(np.arange(0, 5), mean_value, 'o-')
ax.plot(np.arange(0, 5), mean_value2, 'o-')
ax.plot(np.arange(0, 5), mean_value3, 'o-')
for i, v in enumerate(mean_value):
    ax.text(i, v+0.05, "%.2f" %v, ha = "center", c = 'b')
    
for i, v in enumerate(mean_value2):
    ax.text(i, v-0.1, "%.2f" %v, ha = "center", c = 'orange')
    
for i, v in enumerate(mean_value3):
    ax.text(i, v+0.05, "%.2f" %v, ha = "center", c = 'g')

# Plots the 95% confidence interval
ax.fill_between(np.arange(0, 5), conf_interval_low, conf_interval_high,
                alpha=.3)
print(conf_interval_low2)
ax.fill_between(np.arange(0, 5), conf_interval_low2, conf_interval_high2,
                alpha=.3)

ax.fill_between(np.arange(0, 5), conf_interval_low3, conf_interval_high3,
                alpha=.3)


# Adding grid
plt.grid()
# Axis Descriptors
ax.set_ylabel('Distance Ratio(actual travel distance/straight distance)')
ax.set_xlabel('Number of  Agent')
str_list = ['10', '20','30', '40', '50']
ax.set_xticks(range(0,5))
ax.set_xticklabels(str_list)
ax.set_title('Distance Ratio vs. Number of Agent(simulated map)')
# Legend

leg = plt.legend(['A*', 'MSA*', 'hybrid'], loc='upper left')

leg.get_frame().set_alpha(.9)
fig.tight_layout()

#------------------------------------------------------stress distance ratio
#astar realistic time
art10 = [1.3, 1.25, 1.56, 1.45, 1.3] 
art20 = [1.45, 1.25, 1.95, 1.648, 1.9] 
art30 = [1.71, 2.15, 1.85, 1.9, 1.3] 
art40 = [1.65, 1.41, 1.86, 1.455, 1.3] 
art50 = [1.56, 1.65, 1.86, 1.45, 1.5] 

#hybrid realistic time
hmart10 = [1.18, 1.15, 1.156, 1.45, 1.3] 
hmart20 = [1.23, 1.25, 1.158, 1.164, 1.15] 
hmart30 = [1.43, 1.5, 1.56, 1.45, 1.23] 
hmart40 = [1.52, 1.31, 1.86, 1.9, 1.33] 
hmart50 = [1.37, 1.4, 1.6, 1.45, 1.43] 



mean_value = []
mean_value_column = np.mean(art10)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art20)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art30)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art40)
mean_value.append(mean_value_column)
mean_value_column = np.mean(art50)
mean_value.append(mean_value_column)
std_deviation = []
std_deviation_column = np.std(art10)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art20)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art30)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art40)
std_deviation.append(std_deviation_column)
std_deviation_column = np.std(art50)
std_deviation.append(std_deviation_column)

conf_interval_low = []
conf_interval_high = []
low, high = st.t.interval(alpha=0.95, df=len(art10)-1, loc=np.mean(art10), scale=st.sem(art10)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art20)-1, loc=np.mean(art20), scale=st.sem(art20)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art30)-1, loc=np.mean(art30), scale=st.sem(art30)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art40)-1, loc=np.mean(art40), scale=st.sem(art40)) 
conf_interval_low.append(low)
conf_interval_high.append(high)
low, high = st.t.interval(alpha=0.95, df=len(art50)-1, loc=np.mean(art50), scale=st.sem(art50)) 
conf_interval_low.append(low)
conf_interval_high.append(high)



mean_value3 = []
mean_value_column3 = np.mean(hmart10)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart20)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart30)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart40)
mean_value3.append(mean_value_column3)
mean_value_column3 = np.mean(hmart50)
mean_value3.append(mean_value_column3)
std_deviation3 = []
std_deviation_column3 = np.std(hmart10)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart20)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart30)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart40)
std_deviation3.append(std_deviation_column3)
std_deviation_column3 = np.std(hmart50)
std_deviation3.append(std_deviation_column3)


conf_interval_low3 = []
conf_interval_high3 = []
low, high = st.t.interval(alpha=0.95, df=len(hmart10)-1, loc=np.mean(hmart10), scale=st.sem(hmart10)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart20)-1, loc=np.mean(hmart20), scale=st.sem(hmart20)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart30)-1, loc=np.mean(hmart30), scale=st.sem(hmart30)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart40)-1, loc=np.mean(hmart40), scale=st.sem(hmart40)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
low, high = st.t.interval(alpha=0.95, df=len(hmart50)-1, loc=np.mean(hmart50), scale=st.sem(hmart50)) 
conf_interval_low3.append(low)
conf_interval_high3.append(high)
# Sets any on the negative, lower bound values equal to zero
# Cannot have a negative uncertainty
for i in range(len(conf_interval_low)):
    if conf_interval_low[i] < 0:
        conf_interval_low[i] = 0
    
        
for i in range(len(conf_interval_low3)):
    if conf_interval_low3[i] < 0:
        conf_interval_low3[i] = 0

# Defines figure and axes
fig, ax = plt.subplots()
plt.gcf().set_dpi(300)
# Plots the number of agents (x-axis) against the mean value (y-axis) as points connected by a line
ax.plot(np.arange(0, 5), mean_value, 'o-')
ax.plot(np.arange(0, 5), mean_value3, 'o-')
for i, v in enumerate(mean_value):
    print(v)
    ax.text(i, v+0.08, "%.2f" %v, ha = "center", c = 'b')
    
    
for i, v in enumerate(mean_value3):
    ax.text(i, v-0.1, "%.2f" %v, ha = "center", c = 'orange')

# Plots the 95% confidence interval
ax.fill_between(np.arange(0, 5), conf_interval_low, conf_interval_high,
                alpha=.3)


ax.fill_between(np.arange(0, 5), conf_interval_low3, conf_interval_high3,
                alpha=.3)


# Adding grid
plt.grid()
# Axis Descriptors
ax.set_ylabel('Distance Ratio(actual travel distance/straight distance)')
ax.set_xlabel('Number of  Agent')
str_list = ['10', '20','30', '40', '50']
ax.set_xticks(range(0,5))
ax.set_xticklabels(str_list)
ax.set_title('Distance Ratio vs. Number of Agent(stressed map)')
# Legend

leg = plt.legend(['A*', 'hybrid'], loc='upper left')

leg.get_frame().set_alpha(.9)
fig.tight_layout()






















