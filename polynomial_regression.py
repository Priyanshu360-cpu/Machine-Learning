import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:,1:-1].values
Y=dataset.iloc[:,-1].values
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,Y)
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)
regressor2=LinearRegression()
regressor2.fit(X_poly,Y)
print(regressor.predict([[6.5]]))
print(regressor2.predict(poly_reg.fit_transform([[6.5]])))
plt.scatter(X,Y,color='red')
plt.plot(X,regressor2.predict(X_poly),color='blue')
plt.title('Truth or Bluff Linear Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
