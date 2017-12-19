# -*-encoding=utf-8-*-
# plt.rc('font', family='STXihei', size=15) 设置字体
# plt.grid(color=‘#95a5a6’,linestyle=‘--’, linewidth=3,axis=‘both’,alpha=0.4) 设置网格
# plt.gcf().savefig() 导出图片

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
"""
1.通过pandas包将数据scmd_CalculationData.csv读入，从中取出winddirection和windspeed1这2个字
段，绘制风速与风向的散点图。（要求：有标题(风速与风向的函数)、横纵坐标的标题、设置网格，保存图
片文件命名为1风速与风向的函数.png）
"""

scm = pd.read_csv("scmd_CalculationData.csv")
sc = scm.loc[:, ['winddirection', 'windspeed1']]
plt.plot(sc.loc[:, 'winddirection'], sc.loc[:, 'windspeed1'], 'ro')
plt.rc('font', family='STXihei', size=15)
plt.ylabel('winddirection')
plt.xlabel('windspeed1')
plt.title('Wind speed and wind direction')
plt.grid(color='#95a5a6', linestyle='--', linewidth=3, axis='both', alpha=0.4)

plt.gcf().savefig("1Wind speed and wind direction.png")
plt.show()

scm2 = pd.read_csv("scmd_CalculationData.csv")
sc2 = scm2.loc[:, ['windspeed1', 'power_max', 'power_min', 'power', 'power_dev']]
x = sc2.loc[:, 'windspeed1']
y1 = sc2.loc[:, 'power_max']
y2 = sc2.loc[:, 'power_min']
y3 = sc2.loc[:, 'power']
y4 = sc2.loc[:, 'power_dev']
plt.plot(x, y1, 'r--')
plt.plot(x, y2, 'bs')
plt.plot(x, y3, 'g^')
plt.plot(x, y4, 'ys')
plt.legend(loc="upper left")
plt.grid(color='#95a5a6', linestyle='--', linewidth=3, axis='both', alpha=0.4)
plt.ylabel('kindofpower')
plt.xlabel('windspeed1')
plt.title('Power characteristic scatter plot')
plt.gcf().savefig("2Power characteristic scatter plot.png")
plt.show()

bzd = pd.read_csv("bz_df_wt.csv")
bin_bz_fs_less20 = bzd[(bzd.bin_bz_fs) < 20]
bzdf1 = bin_bz_fs_less20.loc[:, ['bin_bz_fs', 'bin_bz_power']]
bzg = pd.read_csv("bzglqx.csv")
bzg.columns = ['fs', 'gl']
bzdf2 = bzg.loc[:, ['fs', 'gl']]
plt.plot(bzdf1.loc[:, 'bin_bz_fs'], bzdf1.loc[:, 'bin_bz_power'])
plt.plot(bzdf2.loc[:, 'fs'], bzdf2.loc[:, 'gl'])
plt.legend(loc="best")
plt.grid(color='#95a5a6', linestyle='--', linewidth=3, axis='both', alpha=0.4)
plt.ylabel('windSpeed')
plt.xlabel('power')
plt.title('Comparison of measured and designed power curves')
plt.gcf().savefig("3Comparison of measured and designed power curves")
plt.show()
