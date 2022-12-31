import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
dataset=pd.read_csv('my_years.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values
le=LabelEncoder()
Y=le.fit_transform(Y)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=1)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)
n=int(input('Enter the year: '))
y_pred=regressor.predict(np.array([[n]]))
plt.scatter(np.array([[n]]),y_pred,color='green')
plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('{} Prediction: '.format(n)+('Good' if round(y_pred[0])==1 else 'Bad'))
plt.xlabel('Years')
plt.ylabel('Good/Bad')
plt.show()
