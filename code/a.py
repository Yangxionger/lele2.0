import matplotlib.pyplot as plt

# 示例数据（替换成你的数据）
x = [1, 2, 3, 4, 5]  # X轴数据
y = [10, 15, 7, 20, 12]  # Y轴数据

# 创建折线图
plt.figure(figsize=(8, 5))  # 设置图像大小
plt.plot(x, y, marker='o', color='blue', linestyle='-', linewidth=2, label='数据趋势')

# 添加标题和标签
plt.title("示例折线图", fontsize=14)
plt.xlabel("X轴标签", fontsize=12)
plt.ylabel("Y轴标签", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)  # 网格线
plt.legend()  # 显示图例

# 显示图表
plt.show()
system("pause")