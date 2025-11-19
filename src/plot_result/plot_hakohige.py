import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# Macの場合
font_path = '/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc'
# フォントを適用
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

log_value   = [4, 3.5, 3, 3.75, 3.5, 4, 3.25, 3.5, 3.25, 3.25] #大規模言語モデルの分析は価値ある試行錯誤をしているか
log_use     = [3, 3, 2.5, 3.25, 2.5, 3.25, 2, 2.75, 2.75, 2.5] #自分が設計者になった時にこの分析を使いたいと思うか

#value = np.array(log_value)

points = [np.array(log_value), np.array(log_use)]

fig, ax = plt.subplots()

bp = ax.boxplot(points, showmeans=True)
# ラベルとタイトルの設定
ax.set_title('大規模言語モデル分析に対する主観評価', fontsize=14)
ax.set_xticklabels(['分析の価値', '利用意向'], fontsize=12)
ax.set_ylabel('評価スコア (1～5)', fontsize=12)



# 平均値のポイントをカスタマイズ
for mean in bp['means']:
    mean.set(color='red', linewidth=1.5)

# グリッドを追加
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 表示
plt.tight_layout()
plt.show()