import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('bc2.csv')
dataset = pd.DataFrame(data)
dataset.columns
dataset.describe().transpose()
