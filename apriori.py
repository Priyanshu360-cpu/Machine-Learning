import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv('Market_Basket_Optimisation.csv',header=None)
transactions=[]
for i in range(0,len(dataset)):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
from apyori import apriori
rules=apriori(transactions=transactions,min_support=21/7501,min_confidence=0.2,min_lift=3,min_length=2,max_length=10)
results=list(rules)
def inspect(results):
    lhs=[tuple(result[2][0][0])[0] for result in results]
    rhs=[tuple(result[2][0][1])[0] for result in results]
    supports=[result[1] for result in results]
    confidence=[result[2][0][2] for result in results]
    lift=[result[2][0][3] for result in results]
    return list(zip(lhs,rhs,supports,confidence,lift))
resultsinDataFrame=pd.DataFrame(inspect(results),columns=['Left Hand Side','Right Hand Side','Support','Confidence','Lift'])
print(resultsinDataFrame.nlargest(n=10,columns='Lift'))