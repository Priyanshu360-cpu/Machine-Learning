import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
dataset=pd.read_csv('my_years_location.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values
le=LabelEncoder()
Y=le.fit_transform(Y)
ct=ColumnTransformer([('encoder',OneHotEncoder(),[1])],remainder='passthrough')
X=np.array(ct.fit_transform(X))
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=1)
regressor=LinearRegression()
regressor.fit(X_train,Y_train)
n=int(input('Enter the year: '))
l=input('Enter the location: ')
if l=='Durgapur':
    l=[1.0,0.0]
elif l=='Kolkata':
    l=[0.0,1.0]
y_pred=regressor.predict(np.array([l+[n]]))
print(y_pred)