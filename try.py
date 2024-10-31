from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import pandas as pd
import numpy as np


Genre=['Drama', 'Adventure' ,'Action', 'Comedy' ,'Horror', 'Biography', 'Crime', 'Fantasy', 'Animation', 'Family', 'Western', 'Sci-Fi', 'Romance', 'Thriller','Mystery']
Rate= ['R', 'PG', 'G', 'NC-17', 'Approved', 'Not Rated', 'PG-13','Unrated', 'X', 'TV-MA']
data = pd.read_csv("movies.csv")
print(data)


genre = []
rating = []

data.dropna(inplace=True)
print(data.columns)

def assign_rate_number(rate):
    if rate == 'R':
        return 0
    elif rate == 'PG':
        return 1
    elif rate == 'G':
        return 2
    elif rate == 'NC-17':
        return 3
    elif rate == 'Approved':
        return 4
    elif rate == 'Not Rated':
        return 5
    elif rate == 'PG-13':
        return 6
    elif rate == 'Unrated':
        return 7
    elif rate == 'X':
        return 8
    elif rate == 'TV-MA':
        return 9
    else:
        return -1  # Return -1 for any rate not listed

# Apply the function to the 'Rate' column
data['Rate_Number'] = data['rating'].apply(assign_rate_number)


def assign_genre_number(genre):
    if genre == 'Drama':
        return 0
    elif genre == 'Adventure':
        return 1
    elif genre == 'Action':
        return 2
    elif genre == 'Comedy':
        return 3
    elif genre == 'Horror':
        return 4
    elif genre == 'Biography':
        return 5
    elif genre == 'Crime':
        return 6
    elif genre == 'Fantasy':
        return 7
    elif genre == 'Animation':
        return 8
    elif genre == 'Family':
        return 9
    elif genre == 'Western':
        return 10
    elif genre == 'Sci-Fi':
        return 11
    elif genre == 'Romance':
        return 12
    elif genre == 'Thriller':
        return 13
    elif genre == 'Mystery':
        return 14
    else:
        return -1  # Return -1 for any genre not listed

# Apply the function to the 'Genre' column
data['Genre_Number'] = data['genre'].apply(assign_genre_number)

print(data.columns)

print(data['Genre_Number'])
print(data["rating"].unique())



x = data.drop(columns=['name', 'rating', 'genre', 'company', 'released', 'director', 'writer', 'star', 'country', 'votes'])
x = data[["budget"]]
y= data[['gross']]

print(data.drop(columns=['name', 'rating', 'genre', 'company', 'released', 'director', 'writer', 'star', 'country']).corr())

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