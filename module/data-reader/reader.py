import pandas as pd

data = pd.read_csv('data/taw/posture.csv')
print(data.describe())
data = data.dropna()
print(data.describe())