#coding: UTF-8
from matplotlib import pyplot as plt
import numpy as np
import math

y_0_0 = np.loadtxt('/home/cdx/Desktop/KITTI_odometry_evaluation_tool-master/data/mapping_speed.txt')
y_0_1 = np.loadtxt('/home/cdx/Desktop/KITTI_odometry_evaluation_tool-master/data/localization_speed.txt')
plt.plot(y_0_0)
plt.plot(y_0_1)
#plt.ylim(-1, 1)
plt.tick_params(labelsize=20)
plt.xlabel('laser frame', fontdict={'style': 'normal', 'weight': 'normal', 'size': 20})
plt.ylabel('pitch /deg', fontdict={'style': 'normal', 'weight': 'normal', 'size': 20})
plt.legend(['slam pitch','gnss pitch'],loc='upper right')
plt.show()

y_0_2 = np.loadtxt('/home/cdx/Desktop/KITTI_odometry_evaluation_tool-master/data/delt_time.txt')
m_0_2 = y_0_2.mean()
v_0_2 = y_0_2.std()
print('average error:', m_0_2)
print('standard deviation:', v_0_2)
plt.plot(y_0_2)
#plt.ylim(-1, 1)
plt.tick_params(labelsize=20)
plt.xlabel('laser frame', fontdict={'style': 'normal', 'weight': 'normal', 'size': 20})
plt.ylabel('pitch error/deg', fontdict={'style': 'normal', 'weight': 'normal', 'size': 20})
plt.legend(['pitch_error %.05f' %m_0_2],loc='upper right')
plt.show()
