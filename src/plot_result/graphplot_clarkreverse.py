# Scenario 3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
matplotlib.rc('font', family='BIZ UDGothic')

x = [1,2,3,4,5,6,7,8,9,10]
x_np = np.array(x)

################################## clark_reverse gpt4o & gpt4omini ##################################
gpt0 = [4016.0, 2330.213, float('nan'), 2509.537, 5001.0, 4101.483, 2173.332, 5274.555, 465.5715, float('nan')]
gpt0_np = np.array(gpt0)
mask = ~np.isnan(gpt0_np)
gpt1 = [float('nan'), 1683.176, 2590.92, 1802.717, 2264.6, 3796.244, 3655.648, 4491.0, 3071.57, 1088.617]
gpt1_np = np.array(gpt1)
mask = ~np.isnan(gpt1_np)
gpt2 = [582.7657, 4888.992, 5388.994, float('nan'), 5612.98, 592.0618, 2847.756, 5354.255, 1984.886, 4277.196]
gpt2_np = np.array(gpt2)
mask = ~np.isnan(gpt2_np)
gpt3 =  [4078.199, float('nan'), float('nan'), 4649.283, 4469.227, 4843.106, 756.9624, float('nan'), 150.1091, 5026.0]
gpt3_np = np.array(gpt3)
mask = ~np.isnan(gpt3_np)
gpt4 = [4956.273, -520.3974, 1196.99, -320.3099, 5302.173, 4572.283, 4462.354, 5594.1, 5606.1, 5606.1]

################################## clark_reverse gpt4o & gpt4omini ##################################

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot(111)

ax.plot(x, gpt0, color = 'darkgreen', alpha=0.3, marker="o", linestyle='None')
ax.plot(x, gpt1, color = 'darkgreen', alpha=0.3, marker="s", linestyle='None')
ax.plot(x, gpt2, color = 'darkgreen', alpha=0.3, marker="v", linestyle='None')
ax.plot(x, gpt3, color = 'darkgreen', alpha=0.3, marker="1", linestyle='None')
ax.plot(x, gpt4, color = 'darkgreen', alpha=0.3, marker="*", linestyle='None')



data = np.array([gpt0,gpt1,gpt2,gpt3,gpt4])
means = np.nanmean(data, axis=0)
stds = np.nanstd(data, axis=0)

# 90パーセント信頼区間の計算
confidence_interval = 1.645 * (stds / np.sqrt(data.shape[0]))

# 平均値と信頼区間のプロット
ax.plot(x_np, means, color='red', label='Mean Utility')
ax.fill_between(x, means - confidence_interval, means + confidence_interval, color='red', alpha=0.2, label='90% Confidence Interval')

# 一次の線形回帰を計算
slope, intercept = np.polyfit(x_np, means, 1)
regression_line = slope * x_np + intercept



# 回帰線のプロット
ax.plot(x, regression_line, color='blue', linestyle='--', linewidth=2, label='Linear Regression')

# タイトルとラベルの設定
#ax.set_title("シナリオ5におけるイテレーション毎のユーティリティ値", fontsize=14)
ax.set_xlabel("イテレーション", fontsize=12)
ax.set_ylabel("ユーティリティ", fontsize=12)

# グリッドの追加
ax.grid(True, linestyle='--', alpha=0.6)

# 凡例の表示
ax.legend(fontsize=10)

# グラフの表示
plt.tight_layout()
plt.show()

# 回帰直線の傾きを表示
print("Slope of the regression line:", slope)
