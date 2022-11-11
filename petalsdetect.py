import pandas as pd;
from matplotlib import pyplot as plt;
from sklearn.datasets import load_iris;
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_blobs
iris=load_iris()
print(dir(iris))
print(iris.feature_names)
print(iris.feature_names[0])
print(iris.data)
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df["target"]=iris.target
print(df[df.target==1].head())
df0=df[df.target==0]
df1=df[df.target==1]
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.scatter(df0["sepal length (cm)"],df0["sepal width (cm)"],color="green",marker="+")
plt.scatter(df1["sepal length (cm)"],df1["sepal width (cm)"],color="blue",marker=".")
