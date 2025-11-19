# Scenario 5
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
matplotlib.rc('font', family='BIZ UDGothic')

x = [1,2,3,4,5,6,7,8,9,10]
x_np = np.array(x)

################################## wc_double gpt4o & gpt4omini ##################################
gpt0 = [1157.501, 6814.43, 5268.841, 6126.0, 5758.941, float('nan'), 5215.92, 2338.537, 2752.082, 2465.529]
gpt0_np = np.array(gpt0)
mask = ~np.isnan(gpt0_np)
gpt1 = [2691.054, 2018.552, 1860.903, 1673.97, 1673.97, 1727.477, 1781.423, 7001.0, 6957.0, 4773.0]
gpt1_np = np.array(gpt1)
mask = ~np.isnan(gpt1_np)
gpt2 = [-1168.356, 2877.409, 5957.025, 5052.461, 6509.922, 5427.454, 6661.43, 3263.902, 2968.122, 4460.133]
gpt2_np = np.array(gpt2)
mask = ~np.isnan(gpt2_np)
gpt3 = [float('nan'), float('nan'), float('nan'), float('nan'), float('nan'), 7014.0, float('nan'), float('nan'), 3132.775, 3710.85]
gpt3_np = np.array(gpt3)
mask = ~np.isnan(gpt3_np)
gpt4 = [float('nan'), 7025.0, 4167.226, float('nan'), 2971.714, 6821.43, 6823.43, 5974.919, 2445.304, 4795.504]

################################## wc_double gpt4o & gpt4omini ##################################

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
#ax.set_title("シナリオ3におけるイテレーション毎のユーティリティ値", fontsize=14)
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
