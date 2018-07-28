import numpy as np

def func1(x):
    y = 1/(1+np.exp(-x))
    return y

def func2(x):
    y = x**2
    return y

def func3(x):
    y = np.sin(x)
    return y

import matplotlib.pyplot as plt

# 定義域を設定
xmin = -10.0
xmax = 10.0
num = 100 # xminからxmaxまでをnum個で区切る
x = np.linspace(xmin, xmax, num)

# 関数から値域を取得
#y = func1(x)
#y = func2(x)
y = func3(x)

# 点どうしを直線でつなぐ
plt.plot(x, y)

# 適切な表示範囲を指定
plt.xlim(xmin, xmax)

# グリッド追加
plt.grid(True)

# 表示
plt.show()
