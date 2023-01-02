import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:,1:-1].values
Y=dataset.iloc[:,-1].values
Y=Y.reshape(len(Y),1)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X=sc.fit_transform(X)
scY=StandardScaler()
Y=scY.fit_transform(Y)
from sklearn.svm import SVR
regressor=SVR(kernel='rbf')
regressor.fit(X,Y)
print(scY.inverse_transform(regressor.predict(sc.transform([[6.5]])).reshape(-1,1)))
plt.scatter(sc.inverse_transform(X),scY.inverse_transform(Y),color='red')
plt.plot(sc.inverse_transform(X),scY.inverse_transform(regressor.predict(X).reshape(-1,1)),color='blue')
plt.title('Truth or Bluff SVR')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
