import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("\file_path")

x = df.iloc[:,1:-1].values
y = df.iloc[:,-1].values

dt = DecisionTreeRegressor(random_state = 0)

dt.fit(x,y)

x_grid = np.arrange(min(x),max(x),0.1)
x_grid = x_grid.reshape(len(x_grid),1)

plt.scatter(x,y,color='red')
plt.plot(x_grid,dt.predict(x_grid))
