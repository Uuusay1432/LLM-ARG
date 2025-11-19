# Scenario 4
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rc('font', family='BIZ UDGothic')
x = [1,2,3,4,5,6,7,8,9,10]
x_np = np.array(x)

################################## wc_reverse gpt4o & gpt4omini ##################################
gpt0 = [3019.391, 1473.233, 2547.967, 2479.815, 3019.391, 3019.391, 3019.391, 3019.391, 2860.358, 3019.391]
gpt0_np = np.array(gpt0)
mask = ~np.isnan(gpt0_np)
gpt1 = [2718.0, 2762.745, 1982.801, 2212.937, 2455.183, 2700.745, 2569.745, 2551.391, 2379.745, 2668.745]
gpt1_np = np.array(gpt1)
mask = ~np.isnan(gpt1_np)
gpt2 = [2358.391, 1689.571, float('nan'), 3019.391, 2467.391, 3019.391, 2930.503, float('nan'), 1338.799, 2529.391]
gpt2_np = np.array(gpt2)
mask = ~np.isnan(gpt2_np)
gpt3 = [2953.503, 908.9795, 2410.918, 2380.219, 2379.613, 760.9869, 2574.358, 2569.358, 1744.547, 2291.872]
gpt3_np = np.array(gpt3)
mask = ~np.isnan(gpt3_np)
gpt4 = [2657.391, 1891.234, 2771.745, 1690.949, 2556.391, 2211.0, 2501.391, 2663.391, 2473.967, float('nan')]
gpt4_np = np.array(gpt4)
mask = ~np.isnan(gpt4_np)

################################## wc_reverse gpt4o & gpt4omini ##################################

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
#ax.set_title("シナリオ2におけるイテレーション毎のユーティリティ値", fontsize=14)
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
