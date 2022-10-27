#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 23:10:57 2021

@author: sdsujchen
"""
import matplotlib.pyplot as plt
import numpy as np

import scipy.stats as st
#---------------------------------------------realistic data
# #astar realistic time
# art10 = [1481, 3020, 1104, 1195, 1429] 
# art20 = [2823.2461659908295, 2924.889178276062, 2871.5627772808075, 2728.3217067718506, 5338.553978681564]
# art30 = [3883.644555091858, 4357.549983024597, 5013.8888556957245, 4302.32173705101, 4886.306672096252]
# art40 = [5372.500425577164, 4935.198933601379, 6911.930958032608, 7197.417633056641, 6187.204947710037]
# art50 = [5984.57848072052, 7411.391969680786, 9638.985779047012, 8950.458555221558, 10701.746854305267] 
# #mastar realistic time
# mart10 = [939, 970, 1130, 915, 1171] 
# mart20 = [971.535754442215, 1084.0504598617554, 1081.923216342926, 971.8451781272888, 1007.8657977581024]
# mart30 = [821.4625942707062, 916.1573202610016, 774.5103521347046, 956.5836646556854, 793.624029636383]
# mart40 = [930.2986173629761, 1041.554292678833, 980.1571002006531, 927.7085957527161, 971.7245893478394]
# mart50 = [1019.4976751804352, 1147.3685052394867, 1126.1165025234222, 1095.688908815384, 1219.7430398464203]
# #hybrid realistic time
# hmart10 = [1180, 708, 855, 1052, 839] 
# hmart20 = [1130, 1515, 906, 934, 986] 
# hmart30 = [1917, 1073, 1116, 2153, 1841] 
# hmart40 = [2094, 1445, 1466, 2174, 1949] 
# hmart50 = [3132, 2724, 2102, 2091, 2929]
# mean_value = []
# mean_value_column = np.mean(art10)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(art20)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(art30)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(art40)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(art50)
# mean_value.append(mean_value_column)
# std_deviation = []
# std_deviation_column = np.std(art10)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(art20)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(art30)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(art40)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(art50)
# std_deviation.append(std_deviation_column)

# conf_interval_low = []
# conf_interval_high = []
# low, high = st.t.interval(alpha=0.95, df=len(art10)-1, loc=np.mean(art10), scale=st.sem(art10)) 
# conf_interval_low.append(low)
# conf_interval_high.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(art20)-1, loc=np.mean(art20), scale=st.sem(art20)) 
# conf_interval_low.append(low)
# conf_interval_high.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(art30)-1, loc=np.mean(art30), scale=st.sem(art30)) 
# conf_interval_low.append(low)
# conf_interval_high.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(art40)-1, loc=np.mean(art40), scale=st.sem(art40)) 
# conf_interval_low.append(low)
# conf_interval_high.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(art50)-1, loc=np.mean(art50), scale=st.sem(art50)) 
# conf_interval_low.append(low)
# conf_interval_high.append(high)


# mean_value2 = []
# mean_value_column2 = np.mean(mart10)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(mart20)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(mart30)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(mart40)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(mart50)
# mean_value2.append(mean_value_column2)
# std_deviation2 = []
# std_deviation_column2 = np.std(mart10)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(mart20)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(mart30)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(mart40)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(mart50)
# std_deviation2.append(std_deviation_column2)

# conf_interval_low2 = []
# conf_interval_high2 = []
# low, high = st.t.interval(alpha=0.95, df=len(mart10)-1, loc=np.mean(mart10), scale=st.sem(mart10)) 
# conf_interval_low2.append(low)
# conf_interval_high2.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(mart20)-1, loc=np.mean(mart20), scale=st.sem(mart20)) 
# conf_interval_low2.append(low)
# conf_interval_high2.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(mart30)-1, loc=np.mean(mart30), scale=st.sem(mart30)) 
# conf_interval_low2.append(low)
# conf_interval_high2.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(mart40)-1, loc=np.mean(mart40), scale=st.sem(mart40)) 
# conf_interval_low2.append(low)
# conf_interval_high2.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(mart50)-1, loc=np.mean(mart50), scale=st.sem(mart50)) 
# conf_interval_low2.append(low)
# conf_interval_high2.append(high)

# mean_value3 = []
# mean_value_column3 = np.mean(hmart10)
# mean_value3.append(mean_value_column3)
# mean_value_column3 = np.mean(hmart20)
# mean_value3.append(mean_value_column3)
# mean_value_column3 = np.mean(hmart30)
# mean_value3.append(mean_value_column3)
# mean_value_column3 = np.mean(hmart40)
# mean_value3.append(mean_value_column3)
# mean_value_column3 = np.mean(hmart50)
# mean_value3.append(mean_value_column3)
# std_deviation3 = []
# std_deviation_column3 = np.std(hmart10)
# std_deviation3.append(std_deviation_column3)
# std_deviation_column3 = np.std(hmart20)
# std_deviation3.append(std_deviation_column3)
# std_deviation_column3 = np.std(hmart30)
# std_deviation3.append(std_deviation_column3)
# std_deviation_column3 = np.std(hmart40)
# std_deviation3.append(std_deviation_column3)
# std_deviation_column3 = np.std(hmart50)
# std_deviation3.append(std_deviation_column3)


# conf_interval_low3 = []
# conf_interval_high3 = []
# low, high = st.t.interval(alpha=0.95, df=len(hmart10)-1, loc=np.mean(hmart10), scale=st.sem(hmart10)) 
# conf_interval_low3.append(low)
# conf_interval_high3.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(hmart20)-1, loc=np.mean(hmart20), scale=st.sem(hmart20)) 
# conf_interval_low3.append(low)
# conf_interval_high3.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(hmart30)-1, loc=np.mean(hmart30), scale=st.sem(hmart30)) 
# conf_interval_low3.append(low)
# conf_interval_high3.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(hmart40)-1, loc=np.mean(hmart40), scale=st.sem(hmart40)) 
# conf_interval_low3.append(low)
# conf_interval_high3.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(hmart50)-1, loc=np.mean(hmart50), scale=st.sem(hmart50)) 
# conf_interval_low3.append(low)
# conf_interval_high3.append(high)
# # Sets any on the negative, lower bound values equal to zero
# # Cannot have a negative uncertainty
# for i in range(len(conf_interval_low)):
#     if conf_interval_low[i] < 0:
#         conf_interval_low[i] = 0
    
# for i in range(len(conf_interval_low2)):
#     if conf_interval_low2[i] < 0:
#         conf_interval_low2[i] = 0
        
# for i in range(len(conf_interval_low3)):
#     if conf_interval_low3[i] < 0:
#         conf_interval_low3[i] = 0

# # Defines figure and axes
# fig, ax = plt.subplots()
# plt.gcf().set_dpi(300)
# # Plots the number of agents (x-axis) against the mean value (y-axis) as points connected by a line
# ax.plot(np.arange(0, 5), mean_value3, 'o-')
# ax.plot(np.arange(0, 5), mean_value, 'o-')
# ax.plot(np.arange(0, 5), mean_value2, 'o-')
# for i, v in enumerate(mean_value3):
#     ax.text(i, v+300, "%d.2" %v, ha = "center", c = 'b')
    
# for i, v in enumerate(mean_value):
#     ax.text(i, v+400, "%d.2" %v, ha = "center", c = 'orange')
    
# for i, v in enumerate(mean_value2):
#     ax.text(i, v - 400, "%d.2" %v, ha = "center", c = 'g')

# # Plots the 95% confidence interval
# ax.fill_between(np.arange(0, 5), conf_interval_low3, conf_interval_high3,
#                 alpha=.3)
# print(conf_interval_low2)
# ax.fill_between(np.arange(0, 5), conf_interval_low, conf_interval_high,
#                 alpha=.3)

# ax.fill_between(np.arange(0, 5), conf_interval_low2, conf_interval_high2,
#                 alpha=.3)


# # Adding grid
# plt.grid()
# # Axis Descriptors
# ax.set_ylabel('Process Time(s)')
# ax.set_xlabel('Number of  Agent')
# str_list = ['10', '20','30', '40', '50']
# ax.set_xticks(range(0,5))
# ax.set_xticklabels(str_list)
# ax.set_title('process time vs. number of agent(easy map)')
# # Legend

# leg = plt.legend(['hybrid', 'A*', 'MSA*'], loc='upper left')

# leg.get_frame().set_alpha(.9)
# fig.tight_layout()

#----


# #astar realistic iteration
# art10 = [1023, 1366, 686, 789, 799] 
# art20 = [1070, 1231, 1147, 868, 1484]
# art30 = [1047, 1502, 1494, 1260, 1299]
# art40 = [1366, 1369, 1406, 1502, 1419]
# art50 = [1288, 1351, 1502, 1502, 1435]
# #mastar realistic iteration
# mart10 = [719,801,590,660,732] 
# mart20 = [719, 859, 776, 724, 807]
# mart30 = [719, 859, 686, 873, 708]
# mart40 = [719, 859, 776, 724, 807]
# mart50 = [729, 859, 787, 807, 922] 
# #hybrid realistic iteration
# hmart10 = [1078, 707, 637, 1001, 787] 
# hmart20 = [956, 1206, 801, 7728, 822] 
# hmart30 = [1156, 854, 724, 1231, 1103] 
# hmart40 = [1117, 821, 842, 1098, 966]
# hmart50 = [1110, 1220, 925, 987, 1131]
# #astar realistic dr
# art10 = [1.37, 1.84, 1.38,1.15, 1.44] 
# art20 = [1.3807758833703978, 1.5681925996204933, 1.6646669166354207, 1.450956046684877, 1.7700920627021648]
# art30 = [1.503304609721409, 1.5163034833784, 1.7008857022353436, 1.6523655829331654, 1.799772382397572]
# art40 = [1.5487716325789664, 1.5433821239489256, 1.6562045564711585, 1.747770040858606, 1.553034123382081]
# art50 = [1.559832391346716, 1.5494899228663848, 1.6878869075117804, 1.5586554164398476, 1.6576454033771106]
# #mastar realistic dr
# mart10 = [1.12, 1.07, 1.05, 1.04, 1.12] 
# mart20 = [1.0594820283190125, 1.0940516972905636, 1.0734973339796412, 1.0832134430569142, 1.0543508712948955]
# mart30 = [1.0682673805739145, 1.0701447431207254, 1.0567692956558414, 1.0714791781468944, 1.0779969650986343]
# mart40 = [1.0594820283190125, 1.0940516972905636, 1.0734973339796412, 1.0832134430569142, 1.0543508712948955]
# mart50 = [1.07420580783473, 1.0718586713112714, 1.0885613970248544, 1.0662311740156052, 1.0889774859287054]
# #hybrid realistic dr
# hmart10 = [1.55, 1.07, 1.17, 1.18, 1.24] 
# hmart20 = [1.38, 1.3, 1.28, 1.15, 1.16] 
# hmart30 = [1.57, 1.23, 1.15, 1.35, 1.31] 
# hmart40 = [1.39, 1.25, 1.15, 1.26, 1.24]
# hmart50 = [1.57, 1.36, 1.34, 1.19, 1.37] 

# mean_value = []
# mean_value_column = np.mean(art10)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(art20)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(art30)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(art40)
# mean_value.append(mean_value_column)
# mean_value_column = np.mean(art50)
# mean_value.append(mean_value_column)
# std_deviation = []
# std_deviation_column = np.std(art10)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(art20)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(art30)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(art40)
# std_deviation.append(std_deviation_column)
# std_deviation_column = np.std(art50)
# std_deviation.append(std_deviation_column)

# conf_interval_low = []
# conf_interval_high = []
# low, high = st.t.interval(alpha=0.95, df=len(art10)-1, loc=np.mean(art10), scale=st.sem(art10)) 
# conf_interval_low.append(low)
# conf_interval_high.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(art20)-1, loc=np.mean(art20), scale=st.sem(art20)) 
# conf_interval_low.append(low)
# conf_interval_high.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(art30)-1, loc=np.mean(art30), scale=st.sem(art30)) 
# conf_interval_low.append(low)
# conf_interval_high.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(art40)-1, loc=np.mean(art40), scale=st.sem(art40)) 
# conf_interval_low.append(low)
# conf_interval_high.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(art50)-1, loc=np.mean(art50), scale=st.sem(art50)) 
# conf_interval_low.append(low)
# conf_interval_high.append(high)


# mean_value2 = []
# mean_value_column2 = np.mean(mart10)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(mart20)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(mart30)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(mart40)
# mean_value2.append(mean_value_column2)
# mean_value_column2 = np.mean(mart50)
# mean_value2.append(mean_value_column2)
# std_deviation2 = []
# std_deviation_column2 = np.std(mart10)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(mart20)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(mart30)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(mart40)
# std_deviation2.append(std_deviation_column2)
# std_deviation_column2 = np.std(mart50)
# std_deviation2.append(std_deviation_column2)

# conf_interval_low2 = []
# conf_interval_high2 = []
# low, high = st.t.interval(alpha=0.95, df=len(mart10)-1, loc=np.mean(mart10), scale=st.sem(mart10)) 
# conf_interval_low2.append(low)
# conf_interval_high2.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(mart20)-1, loc=np.mean(mart20), scale=st.sem(mart20)) 
# conf_interval_low2.append(low)
# conf_interval_high2.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(mart30)-1, loc=np.mean(mart30), scale=st.sem(mart30)) 
# conf_interval_low2.append(low)
# conf_interval_high2.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(mart40)-1, loc=np.mean(mart40), scale=st.sem(mart40)) 
# conf_interval_low2.append(low)
# conf_interval_high2.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(mart50)-1, loc=np.mean(mart50), scale=st.sem(mart50)) 
# conf_interval_low2.append(low)
# conf_interval_high2.append(high)

# mean_value3 = []
# mean_value_column3 = np.mean(hmart10)
# mean_value3.append(mean_value_column3)
# mean_value_column3 = np.mean(hmart20)
# mean_value3.append(mean_value_column3)
# mean_value_column3 = np.mean(hmart30)
# mean_value3.append(mean_value_column3)
# mean_value_column3 = np.mean(hmart40)
# mean_value3.append(mean_value_column3)
# mean_value_column3 = np.mean(hmart50)
# mean_value3.append(mean_value_column3)
# std_deviation3 = []
# std_deviation_column3 = np.std(hmart10)
# std_deviation3.append(std_deviation_column3)
# std_deviation_column3 = np.std(hmart20)
# std_deviation3.append(std_deviation_column3)
# std_deviation_column3 = np.std(hmart30)
# std_deviation3.append(std_deviation_column3)
# std_deviation_column3 = np.std(hmart40)
# std_deviation3.append(std_deviation_column3)
# std_deviation_column3 = np.std(hmart50)
# std_deviation3.append(std_deviation_column3)


# conf_interval_low3 = []
# conf_interval_high3 = []
# low, high = st.t.interval(alpha=0.95, df=len(hmart10)-1, loc=np.mean(hmart10), scale=st.sem(hmart10)) 
# conf_interval_low3.append(low)
# conf_interval_high3.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(hmart20)-1, loc=np.mean(hmart20), scale=st.sem(hmart20)) 
# conf_interval_low3.append(low)
# conf_interval_high3.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(hmart30)-1, loc=np.mean(hmart30), scale=st.sem(hmart30)) 
# conf_interval_low3.append(low)
# conf_interval_high3.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(hmart40)-1, loc=np.mean(hmart40), scale=st.sem(hmart40)) 
# conf_interval_low3.append(low)
# conf_interval_high3.append(high)
# low, high = st.t.interval(alpha=0.95, df=len(hmart50)-1, loc=np.mean(hmart50), scale=st.sem(hmart50)) 
# conf_interval_low3.append(low)
# conf_interval_high3.append(high)
# # Sets any on the negative, lower bound values equal to zero
# # Cannot have a negative uncertainty
# for i in range(len(conf_interval_low)):
#     if conf_interval_low[i] < 0:
#         conf_interval_low[i] = 0
    
# for i in range(len(conf_interval_low2)):
#     if conf_interval_low2[i] < 0:
#         conf_interval_low2[i] = 0
        
# for i in range(len(conf_interval_low3)):
#     if conf_interval_low3[i] < 0:
#         conf_interval_low3[i] = 0

# # Defines figure and axes
# fig, ax = plt.subplots()
# plt.gcf().set_dpi(300)
# # Plots the number of agents (x-axis) against the mean value (y-axis) as points connected by a line
# ax.plot(np.arange(0, 5), mean_value3, 'o-')
# ax.plot(np.arange(0, 5), mean_value, 'o-')
# ax.plot(np.arange(0, 5), mean_value2, 'o-')
# for i, v in enumerate(mean_value3):
#     ax.text(i, v+0.05, "%.2f" %v, ha = "center", c = 'b')
    
# for i, v in enumerate(mean_value):
#     ax.text(i, v-0.1, "%.2f" %v, ha = "center", c = 'orange')
    
# for i, v in enumerate(mean_value2):
#     ax.text(i, v+0.05, "%.2f" %v, ha = "center", c = 'g')

# # Plots the 95% confidence interval
# ax.fill_between(np.arange(0, 5), conf_interval_low3, conf_interval_high3,
#                 alpha=.3)
# print(conf_interval_low2)
# ax.fill_between(np.arange(0, 5), conf_interval_low, conf_interval_high,
#                 alpha=.3)

# ax.fill_between(np.arange(0, 5), conf_interval_low2, conf_interval_high2,
#                 alpha=.3)


# # Adding grid
# plt.grid()
# # Axis Descriptors
# ax.set_ylabel('Distance Ratio(actual travel distance/straight distance)')
# ax.set_xlabel('Number of  Agent')
# str_list = ['10', '20','30', '40', '50']
# ax.set_xticks(range(0,5))
# ax.set_xticklabels(str_list)
# ax.set_title('distance ratio vs. number of agent(easy map)')
# # Legend

# leg = plt.legend(['hybrid', 'A*', 'MSA*'], loc='upper left')

# leg.get_frame().set_alpha(.9)
# fig.tight_layout()

#----------------------------------------------stressed data
#astar fail
#msatar fail
mart10 = [3, 6, 4, 5, 1]
mart20 = [9, 8, 4, 6, 6]
mart30 = [13, 9, 10, 8, 6]
mart40 = [20, 13, 11, 14, 13]
mart50 = [22, 18, 11, 18, 22]
#hastar fail

# #astar stressed time
# art10 = [1481, 3020, 1104, 1195, 1429] 
# art20 = [2823.2461659908295, 2924.889178276062, 2871.5627772808075, 2728.3217067718506, 5338.553978681564]
# art30 = [3883.644555091858, 4357.549983024597, 5013.8888556957245, 4302.32173705101, 4886.306672096252]
# art40 = [5372.500425577164, 4935.198933601379, 6911.930958032608, 7197.417633056641, 6187.204947710037]
# art50 = [5984.57848072052, 7411.391969680786, 9638.985779047012, 8950.458555221558, 10701.746854305267] 
# #mastar stressed time
# mart10 = [939, 970, 1130, 915, 1171] 
# mart20 = [971.535754442215, 1084.0504598617554, 1081.923216342926, 971.8451781272888, 1007.8657977581024]
# mart30 = [821.4625942707062, 916.1573202610016, 774.5103521347046, 956.5836646556854, 793.624029636383]
# mart40 = [930.2986173629761, 1041.554292678833, 980.1571002006531, 927.7085957527161, 971.7245893478394]
# mart50 = [1019.4976751804352, 1147.3685052394867, 1126.1165025234222, 1095.688908815384, 1219.7430398464203]
# #hybrid stressed time
# hmart10 = [1180, 708, 855, 1052, 839] 
# hmart20 = [1130, 1515, 906, 934, 986] 
# hmart30 = [1917, 1073, 1116, 2153, 1841] 
# hmart40 = [2094, 1445, 1466, 2174, 1949] 
# hmart50 = [3132, 2724, 2102, 2091, 2929]
# #astar stressed iteration
# art10 = [1023, 1366, 686, 789, 799] 
# art20 = [1070, 1231, 1147, 868, 1484]
# art30 = [1047, 1502, 1494, 1260, 1299]
# art40 = [1366, 1369, 1406, 1502, 1419]
# art50 = [1288, 1351, 1502, 1502, 1435]
# #mastar stressed iteration
# mart10 = [719,801,590,660,732] 
# mart20 = [719, 859, 776, 724, 807]
# mart30 = [719, 859, 686, 873, 708]
# mart40 = [719, 859, 776, 724, 807]
# mart50 = [729, 859, 787, 807, 922] 
# #hybrid stressed iteration
# hmart10 = [1078, 707, 637, 1001, 787] 
# hmart20 = [956, 1206, 801, 7728, 822] 
# hmart30 = [1156, 854, 724, 1231, 1103] 
# hmart40 = [1117, 821, 842, 1098, 966]
# hmart50 = [1110, 1220, 925, 987, 1131]
# #astar stressed dr
# art10 = [1.37, 1.84, 1.38,1.15, 1.44] 
# art20 = [1.3807758833703978, 1.5681925996204933, 1.6646669166354207, 1.450956046684877, 1.7700920627021648]
# art30 = [1.503304609721409, 1.5163034833784, 1.7008857022353436, 1.6523655829331654, 1.799772382397572]
# art40 = [1.5487716325789664, 1.5433821239489256, 1.6562045564711585, 1.747770040858606, 1.553034123382081]
# art50 = [1.559832391346716, 1.5494899228663848, 1.6878869075117804, 1.5586554164398476, 1.6576454033771106]
# #mastar stressed dr
# mart10 = [1.12, 1.07, 1.05, 1.04, 1.12] 
# mart20 = [1.0594820283190125, 1.0940516972905636, 1.0734973339796412, 1.0832134430569142, 1.0543508712948955]
# mart30 = [1.0682673805739145, 1.0701447431207254, 1.0567692956558414, 1.0714791781468944, 1.0779969650986343]
# mart40 = [1.0594820283190125, 1.0940516972905636, 1.0734973339796412, 1.0832134430569142, 1.0543508712948955]
# mart50 = [1.07420580783473, 1.0718586713112714, 1.0885613970248544, 1.0662311740156052, 1.0889774859287054]
# #hybrid stressed dr
# hmart10 = [1.55, 1.07, 1.17, 1.18, 1.24] 
# hmart20 = [1.38, 1.3, 1.28, 1.15, 1.16] 
# hmart30 = [1.57, 1.23, 1.15, 1.35, 1.31] 
# hmart40 = [1.39, 1.25, 1.15, 1.26, 1.24]
# hmart50 = [1.57, 1.36, 1.34, 1.19, 1.37] 








#------------------------------------------------------stressed time
#astar hard time
# art10 = [1591.4074339866638, 1657.7161989212036, 2023.2810487747192, 1606.7373728752136, 1762.8377168178558]
# art20 = [3113.5203201770782, 3395.8058059215546, 2448.1489627361298, 3216.406983613968, 2821.5841932296753]
# art30 = [6772.641670703888, 4613.278887987137, 4051.9304325580597, 3657.045259475708, 4410.570475578308]
# art40 = [8116.536029338837, 6412.762358665466, 6016.935415506363, 8112.061033248901, 6687.163062572479]
# art50 = [8899.014533042908, 9942.178032398224, 8840.536116361618, 7391.382253170013, 7026.855218887329]

#hybrid hard time
hmart10 = [1178.2264566421509, 1425.3807799816132, 1825.0345323085785, 1085.1276590824127, 958.5480966567993]
hmart20 = [1934.2473089694977, 2387.5100960731506, 1358.7994418144226, 2402.4492399692535, 1560.2103326320648]
hmart30 = [3736.119804382324, 2031.1993882656097, 1939.2188913822174, 1792.8967700004578, 1984.3342459201813]
hmart40 = [3261.2338325977325, 2496.7814638614655, 3091.425865650177, 4238.834998130798, 3749.325303554535]
hmart50 = [4755.698483943939, 5519.822639942169, 5775.318786144257, 8361.803695201874, 4454.281238794327]




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
ax.plot(np.arange(0, 5), mean_value3, 'o-')
ax.plot(np.arange(0, 5), mean_value, 'o-')
for i, v in enumerate(mean_value3):
    ax.text(i, v+100, "%d.2" %v, ha = "center", c = 'b')
    
    
for i, v in enumerate(mean_value):
    ax.text(i, v+400, "%d.2" %v, ha = "center", c = 'orange')

# Plots the 95% confidence interval
ax.fill_between(np.arange(0, 5), conf_interval_low3, conf_interval_high3,
                alpha=.3)


ax.fill_between(np.arange(0, 5), conf_interval_low, conf_interval_high,
                alpha=.3)


# Adding grid
plt.grid()
# Axis Descriptors
ax.set_ylabel('Process Time(s)')
ax.set_xlabel('Number of  Agent')
str_list = ['10', '20','30', '40', '50']
ax.set_xticks(range(0,5))
ax.set_xticklabels(str_list)
ax.set_title('process time vs. number of agent(hard map)')
# Legend

leg = plt.legend(['hybrid' , 'A*'], loc='upper left')

leg.get_frame().set_alpha(.9)
fig.tight_layout()

#------------------------------------------------------stress distance ratio
# #astar hard dr
art10 = [1.621673459602014, 1.370831659300924, 1.3930552701869734, 1.4671909560088474, 1.3632275793155133]
art20 = [1.6156957044485736, 1.5678155774395703, 1.4628241366597026, 1.6083899127061105, 1.5616772306192102]
art30 = [1.7057648401826484, 1.6233819433065706, 1.6140138687308498, 1.473374714145704, 1.5248709701548357]
art40 = [1.6942770251589716, 1.596948428440647, 1.6516648371752654, 1.7278841769265847, 1.8756301524227508]
art50 = [1.6105124954726548, 1.5548430972505587, 1.5302137921439503, 1.7180547632629777, 1.6802836080199088]

# #hybrid hard dr
hmart10 = [1.4754255574202828, 1.5110486139011652, 1.5543455927676186, 1.583435733595478, 1.2273295028728453]
hmart20 = [1.6232375122964258, 1.8084153983885407, 1.3632788496989063, 1.526066925315228, 1.4205265724037055]
#[1.7878456661930267, 1.802820053715309, 1.4860513702838885, 1.2697623666343356, 1.408946855192589]
[1.6420373811345503, 1.6547672336615935, 1.4485682684035885, 1.5678952473326868, 1.4037055095075572]
hmart30 = [1.7932363013698631, 1.679747665082746, 1.4676665054023545, 1.4646357399542633, 1.5212057745530705]
hmart40 = [1.7468620403649433, 1.5849252364967958, 1.5686059275521405, 1.9868331053351573, 1.933100053377617]
hmart50 = [1.7873505976095618, 1.7290877295249198, 1.6859898900895052, 1.9529853584331622, 2.024087899704184]

# #astar fail
# art10 = [0, 0, 0, 0, 0]
# art20 = [0, 0, 0, 0, 0]
# art30 = [1, 0, 0, 0, 0]
# art40 = [1, 1, 2, 1, 1]
# art50 = [1, 2, 2, 0, 1]

# hastar fail
# hmart10 = [0, 0, 0, 0, 0]
# # #hart20 = [0, 0, 0, 0, 0]
# # #hart30 = [1, 0, 0, 0, 0]
# hart40 = [0, 0, 0, 0, 0]
# # hart50 = [0, 0, 0, 0, 0]




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
ax.plot(np.arange(0, 5), mean_value3, 'o-')
ax.plot(np.arange(0, 5), mean_value, 'o-')
for i, v in enumerate(mean_value3):
    print(v)
    ax.text(i, v+0.06, "%.2f" %v, ha = "center", c = 'b')
    
    
for i, v in enumerate(mean_value):
    ax.text(i, v-0.06, "%.2f" %v, ha = "center", c = 'orange')

# Plots the 95% confidence interval
ax.fill_between(np.arange(0, 5), conf_interval_low3, conf_interval_high3,
                alpha=.3)


ax.fill_between(np.arange(0, 5), conf_interval_low, conf_interval_high,
                alpha=.3)


# Adding grid
plt.grid()
# Axis Descriptors
ax.set_ylabel('Distance Ratio(actual travel distance/straight distance)')
ax.set_xlabel('Number of  Agent')
str_list = ['10', '20','30', '40', '50']
ax.set_xticks(range(0,5))
ax.set_xticklabels(str_list)
ax.set_title('distance ratio vs. number of agent(hard map)')
# Legend

leg = plt.legend(['A*', 'hybrid'], loc='upper left')

leg.get_frame().set_alpha(.9)
fig.tight_layout()






















