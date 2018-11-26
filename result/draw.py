import pandas as pd
import matplotlib.pyplot as plt

LogSig_datapath = 'LogSig/LogSig.out'
IPLoM_datapath = 'IPLoM/IPLoM.out'
SLCT_datapath = 'SLCT/SLCT.out'
LKE_datapath = 'LKE/LKE.out'

with open(LogSig_datapath, "r") as file:
    LogSig_data = [[x for x in line.split()] for line in file]
with open(IPLoM_datapath, "r") as file:
    IPLoM_data = [[x for x in line.split()] for line in file]
with open(SLCT_datapath, "r") as file:
    SLCT_data = [[x for x in line.split()] for line in file]
with open(LKE_datapath, "r") as file:
    LKE_data = [[x for x in line.split()] for line in file]

# in Order:
# BGL
# HPC
# HDFS
# Zookeeper
# Proxifier

F_measure_BGL = [LogSig_data[0][6], IPLoM_data[0]
                 [6], SLCT_data[0][6], LKE_data[0][6]]
F_measure_HPC = [LogSig_data[1][6], IPLoM_data[1]
                 [6], SLCT_data[1][6], LKE_data[1][6]]
F_measure_HDFS = [LogSig_data[2][6], IPLoM_data[2]
                  [6], SLCT_data[2][6], LKE_data[2][6]]
F_measure_Zoo = [LogSig_data[3][6], IPLoM_data[3]
                 [6], SLCT_data[3][6], LKE_data[3][6]]
F_measure_Prox = [LogSig_data[4][6], IPLoM_data[4]
                  [6], SLCT_data[4][6], LKE_data[4][6]]

RI_BGL = [LogSig_data[0][7], IPLoM_data[0]
          [7], SLCT_data[0][7], LKE_data[0][7]]
RI_HPC = [LogSig_data[1][7], IPLoM_data[1]
          [7], SLCT_data[1][7], LKE_data[1][7]]
RI_HDFS = [LogSig_data[2][7], IPLoM_data[2]
           [7], SLCT_data[2][7], LKE_data[2][7]]
RI_Zoo = [LogSig_data[3][7], IPLoM_data[3]
          [7], SLCT_data[3][7], LKE_data[3][7]]
RI_Prox = [LogSig_data[4][7], IPLoM_data[4]
           [7], SLCT_data[4][7], LKE_data[4][7]]

Runtime_BGL = [LogSig_data[0][8], IPLoM_data[0]
               [8], SLCT_data[0][8], LKE_data[0][10]]
Runtime_HPC = [LogSig_data[1][8], IPLoM_data[1]
               [8], SLCT_data[1][8], LKE_data[1][10]]
Runtime_HDFS = [LogSig_data[2][8], IPLoM_data[2]
                [8], SLCT_data[2][8], LKE_data[2][10]]
Runtime_Zoo = [LogSig_data[3][8], IPLoM_data[3]
               [8], SLCT_data[3][8], LKE_data[3][10]]
Runtime_Prox = [LogSig_data[4][8], IPLoM_data[4]
                [8], SLCT_data[4][8], LKE_data[4][10]]

index = ['LogSig', 'IPLoM', 'SLCT', 'LKE']

F_measure = pd.DataFrame({'2kBGL': F_measure_BGL, '2kHPC': F_measure_HPC, '2kHDFS': F_measure_HDFS,
                          '2kZookeeper': F_measure_Zoo, '2kProxifier': F_measure_Prox}, index=index)

RI = pd.DataFrame({'2kBGL': RI_BGL, '2kHPC': RI_HPC, '2kHDFS': RI_HDFS,
                   '2kZookeeper': RI_Zoo, '2kProxifier': RI_Prox}, index=index)

Runtime = pd.DataFrame({'2kBGL': Runtime_BGL, '2kHPC': Runtime_HPC, '2kHDFS': Runtime_HDFS,
                        '2kZookeeper': Runtime_Zoo, '2kProxifier': Runtime_Prox}, index=index)

F_measure = F_measure.astype(float)
RI = RI.astype(float)
Runtime = Runtime.astype(float)

ax = F_measure.plot.bar()
bx = RI.plot.bar()
cx = Runtime.plot.bar()
cx.set_yscale('log')

ax.set_title("F measure")
bx.set_title("RandIndex")
cx.set_title("Runtime")
plt.show()
