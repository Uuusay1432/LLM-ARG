# Scenario 2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rc('font', family='BIZ UDGothic')

x = [1,2,3,4,5,6,7,8,9,10]
x_np = np.array(x)

################################## wc_origin gpt4o & gpt4omini ##################################
gpt0 = [1203.849, 2474.563, 2964.465, 3124.415, 2907.587, 2762.098, 2956.432, 2981.432, float('nan'), 2926.353]
gpt0_np = np.array(gpt0)
mask = ~np.isnan(gpt0_np)
gpt1 = [1119.852, 1118.689, 1089.427, 2739.6, float('nan'), 3138.922, float('nan'), 3138.922, 3138.922, 1087.405]
gpt1_np = np.array(gpt1)
mask = ~np.isnan(gpt1_np)
gpt2 = [2774.0, 2920.587, 2487.628, 2940.587, 2920.587, float('nan'), 2961.0, float('nan'), 2927.0, 3472.0]
gpt2_np = np.array(gpt2)
mask = ~np.isnan(gpt2_np)
gpt3 = [2187.703, 2779.565, 2052.613, 2855.135, float('nan'), 2932.135, 2848.135, 3047.135, float('nan'), 1053.109]
gpt3_np = np.array(gpt3)
mask = ~np.isnan(gpt3_np)
gpt4 = [3409.0, 2735.941, 2920.0, 2865.587, 2141.188, 1015.416, 2934.467, 1038.376, 2566.992, 2494.38]

################################## wc_origin gpt4o & gpt4omini ##################################

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
#ax.set_title("シナリオ1におけるイテレーション毎のユーティリティ値", fontsize=14)
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
