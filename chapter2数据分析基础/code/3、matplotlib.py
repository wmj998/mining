import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决plt中文显示的问题
plt.rcParams['axes.unicode_minus'] = False  # 解决plt负号显示的问题

x = np.linspace(0, 2)
y = (np.sin(x - 2)) ** 2 * (np.exp(-x ** 2))

plt.title("$y = sin(x-2)^2e^{-x^2}$")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()

x = np.linspace(0, 6)
y = np.cos(x)
plt.title("Example")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y, label='cos(x)', color='g')
plt.legend()
plt.show()

x = [0.15, 0.3, 0.45, 0.1]
explode = [0, 0, 0, 0]
labels = ['apples', 'oranges', 'bananas', 'pears']
colors = ['r', 'y', 'g', 'b']
plt.pie(x, explode, labels, colors, autopct='%.1f%%')
plt.show()
