import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
x_np = np.array(x)

################################## clark_double gpt4o & gpt4omini ##################################
gpt0 = [11270.31, 9833.447, 1356.603, 4724.519, 8681.835, 10620.87, 3154.278, 3318.797, 1570.107, 726.1754]
gpt0_np = np.array(gpt0)
mask = ~np.isnan(gpt0_np)
gpt1 = [float('nan'), 8829.539, 3798.369, 11261.56, 11370.09, 11292.73, float('nan'), 3099.919, 1848.063, 4072.018]
gpt1_np = np.array(gpt1)
mask = ~np.isnan(gpt1_np)
gpt2 = [8817.801, 1583.5, float('nan'), 1237.166, 1636.557, 10213.17, 9055.404, 4523.515, 4563.984, 8221.0]
gpt2_np = np.array(gpt2)
mask = ~np.isnan(gpt2_np)
gpt3 = [5000.02, 11132.56, 9791.152, float('nan'), 2857.058, 11145.56, 4485.816, 10632.83, 11128.56, 11216.09]
gpt3_np = np.array(gpt3)
mask = ~np.isnan(gpt3_np)
gpt4 = [11473.8, 2459.899, 11412.55, 10568.25, 11440.02, 10062.31, float('nan'), 6954.716, 11138.29, float('nan')]
gpt4_np = np.array(gpt4)
mask = ~np.isnan(gpt4_np)

################################## clark_double gpt4o & gpt4omini ##################################

################################## clark_double gpt4o ##################################
pgpt0 = [9691.462, 6870.079, 5133.205, float('nan'), float('nan'), float('nan'), float('nan'), float('nan'), float('nan'), float('nan')]
pgpt0_np = np.array(pgpt0)
mask = ~np.isnan(pgpt0_np)
pgpt1 = [8965.698, float('nan'), 1144.35, 8271.0, 8264.0, 9365.0, 9105.0, 9627.0, 9301.345, float('nan')]
pgpt1_np = np.array(pgpt1)
mask = ~np.isnan(pgpt1_np)
pgpt2 = [11443.02, 10964.01, 1708.343, float('nan'), 3516.403, 7142.622, float('nan'), 4404.705, 9963.673, 11169.32]
pgpt2_np = np.array(pgpt2)
mask = ~np.isnan(pgpt2_np)
pgpt3 = [8818.998, 8259.0, 3440.669, 306.7621, 9365.732, 711.7011, 9529.52, float('nan'), 7915.299, 9470.283]
pgpt3_np = np.array(pgpt3)
mask = ~np.isnan(gpt3_np)
pgpt4 = [9170.534, 3474.16, float('nan'), 7652.312, 7028.946, float('nan'), 6276.582, 7152.644, 8697.637, 1669.82]
pgpt4_np = np.array(pgpt4)
mask = ~np.isnan(pgpt4_np)

################################## clark_double gpt4o ##################################
fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot(111)

ax.plot(x, gpt0, color = 'r', alpha=0.3, marker="o", linestyle='None')
ax.plot(x, gpt1, color = 'r', alpha=0.3, marker="o", linestyle='None')
ax.plot(x, gpt2, color = 'r', alpha=0.3, marker="o", linestyle='None')
ax.plot(x, gpt3, color = 'r', alpha=0.3, marker="o", linestyle='None')
ax.plot(x, gpt4, color = 'r', alpha=0.3, marker="o", linestyle='None')

ax.plot(x, pgpt0, color = 'b', alpha=0.3, marker="o", linestyle='None')
ax.plot(x, pgpt1, color = 'b', alpha=0.3, marker="o", linestyle='None')
ax.plot(x, pgpt2, color = 'b', alpha=0.3, marker="o", linestyle='None')
ax.plot(x, pgpt3, color = 'b', alpha=0.3, marker="o", linestyle='None')
ax.plot(x, pgpt4, color = 'b', alpha=0.3, marker="o", linestyle='None')



data = np.array([gpt0,gpt1,gpt2,gpt3,gpt4])
means = np.nanmean(data, axis=0)
stds = np.nanstd(data, axis=0)

#pdata = np.array([pgpt0,pgpt1,pgpt2,pgpt3])
pdata = np.array([pgpt0,pgpt1,pgpt2,pgpt3,pgpt4])
pmeans = np.nanmean(pdata, axis=0)
pstds = np.nanstd(pdata, axis=0)

# 90パーセント信頼区間の計算
confidence_interval = 1.645 * (stds / np.sqrt(data.shape[0]))
pconfidence_interval = 1.645 * (pstds / np.sqrt(pdata.shape[0]))

# 平均値と信頼区間のプロット
ax.plot(x_np, means, color='red', label='Mean Utility(4o, 4o-mini)')
ax.fill_between(x, means - confidence_interval, means + confidence_interval, color='red', alpha=0.2, label='90% Confidence Interval(4o, 4o-mini)')
ax.fill_between(x, pmeans - pconfidence_interval, pmeans + pconfidence_interval, color='b', alpha=0.2, label='90% Confidence Interval(4o)')

# 平均値と信頼区間のプロット
ax.plot(x_np, pmeans, color='b', label='Mean Utility(4o)')

# 一次の線形回帰を計算
slope, intercept = np.polyfit(x_np, means, 1)
regression_line = slope * x_np + intercept
print("Slope of the regression line:", slope)
slope, intercept = np.polyfit(x_np, pmeans, 1)
pregression_line = slope * x_np + intercept



# 回帰線のプロット
ax.plot(x, regression_line, color='darkgreen', linestyle='--', linewidth=2, label='Linear Regression(4o, 4o-mini)')
ax.plot(x, pregression_line, color='orange', linestyle='--', linewidth=2, label='Linear Regression(4o)')

# タイトルとラベルの設定
ax.set_title("Utility Values over Iterations", fontsize=14)
ax.set_xlabel("Iteration", fontsize=12)
ax.set_ylabel("Utility", fontsize=12)

# グリッドの追加
ax.grid(True, linestyle='--', alpha=0.6)

# 凡例の表示
ax.legend(fontsize=10)

# グラフの表示
plt.tight_layout()
plt.show()

# 回帰直線の傾きを表示
print("Slope of the regression line:", slope)