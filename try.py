from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import pandas as pd
import numpy as np

data = pd.read_csv("movies.csv")
print(data)

data.dropna(inplace=True)
print(data.columns)

x = data.drop(columns=['name', 'rating', 'genre', 'company', 'released', 'director', 'writer', 'star', 'country', 'votes'])
y= data['votes']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(x_train,y_train)

print(model.intercept_)
print(model.coef_)

y_pred = model.predict(x_test)
print(y_pred)

rmse = np.sqrt(mean_squared_error(y_test,y_pred))
r2 = r2_score(y_test,y_pred)

print(rmse)
print(r2)