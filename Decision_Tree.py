import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:,1:-1].values
Y=dataset.iloc[:,-1].values
from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(X,Y)
print(regressor.predict([[6.5]]))
X_grid=np.arange(min(X),max(X),0.01)
X_grid=X_grid.reshape(len(X_grid),1)
plt.scatter(X,Y,color='red')
plt.plot(X_grid,regressor.predict(X_grid),color='blue')
plt.title('Truth or Bluff Decision Tree Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()