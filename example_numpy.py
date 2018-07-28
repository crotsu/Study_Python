# 連立1次方程式 Ax = bをやってみる

# numpyをインポートして名前をnpにする．numpyのメソッドは，np.***で使える．
import numpy as np

# 行列
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A)

# ベクトル
x = np.array([[1],[2],[3]])
print(x)

# 行列とベクトルの演算
b = np.dot(A, x)
print(b)

# こちらは違う
A * x

# わかりやすく実行すると
x = np.array([[10],[100],[1000]])
A * x

#  定数倍
A * 2
