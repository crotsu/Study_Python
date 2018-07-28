import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 関数を作成
def sigmoid(x):
    return 1/(1+np.exp(-x)) # math.exp(x)だとスカラーしか受け付けない．np.exp(x)としてリスト全体を受けて，リストを返すのがコツ．

# 定義域を設定
xmin = -5.0
xmax = 5.0
num = 100 # xminからxmaxまでをnum個で区切る

x = np.linspace(xmin, xmax, num)
y = sigmoid(x)+np.random.normal(0, 0.08, len(x))

df = pd.DataFrame()
df.to_csv("data.csv", header=None, index=False)
