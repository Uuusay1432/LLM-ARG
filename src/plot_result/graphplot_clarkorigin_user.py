import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
matplotlib.rc('font', family='BIZ UDGothic')

x = [1,2,3,4,5,6,7,8,9,10]
x_np = np.array(x)

################################## clark_origin gpt4o & gpt4omini ##################################
gpt0 = [5511.558, 420.4516, 877.9587, 2309.529, 1641.68, 583.7272, 2746.658, 5453.093, 5512.13, 5043.0]
gpt1 = [-3159.374, 645.2041, 4980.761, float('nan'), 434.1372, 4896.255, 2333.346, 5320.285, float('nan'), 4914.391]
gpt1_np = np.array(gpt1)
mask = ~np.isnan(gpt1_np)
gpt2 = [float('nan'), 5193.723, 763.8909, -233.8607, 1400.35, 4754.124, 5198.001, 5697.963, 4905.264, 3424.114]
gpt2_np = np.array(gpt2)
mask = ~np.isnan(gpt2_np)
gpt3 = [5304.955, 4271.808, 5304.955, 5428.558, 5214.123, 5345.726, float('nan'), 5044.841, 5345.726, 4623.743]
gpt3_np = np.array(gpt3)
mask = ~np.isnan(gpt3_np)
gpt4 = [5304.955, 4060.0, 301.7518, 2267.903, 4424.978, 5218.123, 5266.726, float('nan'), 706.7771, 5332.895]
gpt4_np = np.array(gpt4)
mask = ~np.isnan(gpt4_np)

################################## clark_origin gpt4o & gpt4omini ##################################

########################################## user experiment ##########################################

hirano =    [463,  5333, 4028, 4028, -3356, 5333, 5531, float('nan'),   5417, -3356]
hirano_np = np.array(hirano)
mask = ~np.isnan(hirano_np)
takeuchi =  [5043, 5239, 5443, 5588,  5626, 5602, 5576, 5649,           5660, 5663]
yamauchi =  [464,  -494, -1030,3003,  4556, 4556, 4033, 4499,           -1526, -1606]
ikeda =     [5531, 5512, 5482, 5543,  5557, 5789, 5653, 5799,           5992, 5992]

########################################## user experiment ##########################################

fig = plt.figure(figsize=(9,  6))
ax = fig.add_subplot(111)

#ax.plot(x, gpt0, color = 'darkgreen', alpha=0.3, marker="o", linestyle='None')
#ax.plot(x, gpt1, color = 'darkgreen', alpha=0.3, marker="o", linestyle='None')
#ax.plot(x, gpt2, color = 'darkgreen', alpha=0.3, marker="o", linestyle='None')
#ax.plot(x, gpt3, color = 'darkgreen', alpha=0.3, marker="o", linestyle='None')
#ax.plot(x, gpt4, color = 'darkgreen', alpha=0.3, marker="o", linestyle='None')

ax.plot(x, hirano, color = 'orange', alpha=0.5, marker="o", linestyle='None' ,label = 'User Experiment Utility')
ax.plot(x, takeuchi, color = 'orange', alpha=0.5, marker="s", linestyle='None')
ax.plot(x, yamauchi, color = 'orange', alpha=0.5, marker="v", linestyle='None')
ax.plot(x, ikeda, color = 'orange', alpha=0.5, marker="*", linestyle='None')

userdata = np.array([hirano, takeuchi, yamauchi, ikeda])
usermeans = np.nanmean(userdata, axis=0)
userstds = np.nanstd(userdata, axis=0)

data = np.array([gpt0,gpt1,gpt2,gpt3,gpt4])
means = np.nanmean(data, axis=0)
stds = np.nanstd(data, axis=0)

# 90パーセント信頼区間の計算
#confidence_interval = 1.645 * (stds / np.sqrt(data.shape[0]))

# 平均値と信頼区間のプロット
ax.plot(x_np, means, color='red', label='Mean Utility(LLM-ARG)')
ax.plot(x_np, usermeans, color='green', label='User Mean Utility')
#ax.fill_between(x, means - confidence_interval, means + confidence_interval, color='red', alpha=0.2, label='90% Confidence Interval')

# 一次の線形回帰を計算
slope, intercept = np.polyfit(x_np, means, 1)
regression_line = slope * x_np + intercept

# 回帰線のプロット
#ax.plot(x, regression_line, color='blue', linestyle='--', linewidth=2, label='Linear Regression')


# 一次の線形回帰を計算
userslope, intercept = np.polyfit(x_np, usermeans, 1)
regression_line = userslope * x_np + intercept

# 回帰線のプロット
ax.plot(x, regression_line, color='brown', linestyle='--', linewidth=2, label='User Linear Regression')


# タイトルとラベルの設定
#ax.set_title("被験者が取り組んだイテレーション毎のユーティリティ値", fontsize=14)
ax.set_xlabel("イテレーション", fontsize=12)
ax.set_ylabel("ユーティリティ", fontsize=12)

# グリッドの追加
ax.grid(True, linestyle='--', alpha=0.6)

# 凡例を上部に配置、ncol=2 で2列（あるいは4列）に並べる
ax.legend(bbox_to_anchor=(0.5, 1.01), loc='lower center', borderaxespad=0, ncol=2, fontsize=14)

# グラフの表示
plt.tight_layout()
plt.show()

# 回帰直線の傾きを表示
print("Slope of the regression line:", slope)
