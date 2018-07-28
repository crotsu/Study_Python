import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data.csv', names=('A', 'B'))
plt.scatter(df.A, df.B)
plt.grid(True)
plt.show()
