import pandas as pd
import matplotlib.pyplot as plt

# 創建示例玩家統計數據
data = {
    'player': ['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10'],
    'score': [1625, 1000, 1200, 1100, 1000, 975, 1350, 855, 1400, 1450]
}

# 創建DataFrame
df = pd.DataFrame(data)

# 設定圖表尺寸
plt.figure(figsize=(9, 4))  # 調整寬度和高度來改變整個圖表的大小

# 計算得分的平均值和標準差
mean_value = df['score'].mean()
std_value = df['score'].std()

# 創建柱狀圖
plt.bar(df['player'], df['score'], width = 0.5)
plt.xlabel('player')
plt.ylabel('score')
plt.title('player score statistics')

# 添加得分平均值和標準差的文本注釋
plt.text(len(df) + 0.7, mean_value, f'mean: {mean_value:.2f}', ha='center', va='bottom')
plt.text(len(df) + 0.5, mean_value - std_value, f'std: {std_value:.2f}', ha='center', va='top')

# 調整y軸上限值
plt.ylim(0, 2000)  # 設置y軸的上限值為2000

plt.tight_layout()  # 調整圖表布局，確保注釋不超出範圍

plt.show()