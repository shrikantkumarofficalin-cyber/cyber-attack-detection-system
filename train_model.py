import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("dataset.csv", header=None)

X = data.iloc[:, [0,4,5]]
y = data.iloc[:, 41]

y = y.apply(lambda x: 0 if x == "normal" else 1)

model = DecisionTreeClassifier()
model.fit(X,y)

pickle.dump(model, open("model.pkl","wb"))

print("Model trained successfully")