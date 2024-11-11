'''
for this project we wiil be analysising a data-set of movies and use python libraries to predict number of votes and score on the basis random parameters we will be passing to our model. Before prediction we would also analysis the graph which would make more sense with our data for analysing the correlation ship between columns of score, votes, director.
Here we will be only using director , votes, genre, score which are at the top to remove clustering of data.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from tkinter import messagebox
import data as col_data
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import joblib
# Load the dataset with exception handling
try:
    data = pd.read_csv("movies.csv")
except FileNotFoundError:
    print("Error: 'movies.csv' file not found. Please check the file path.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: No data found in 'movies.csv'.")
    exit()
except pd.errors.ParserError:
    print("Error: Parsing 'movies.csv' failed. Please check the file format.")
    exit()

# Univariate plotting functions
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Univariate plotting functions with adjusted figure size for top 20 largest values

def count_plot_uni(dataset, col):
    
    # Keep only top 20 categories
    top_categories = dataset[col].value_counts().nlargest(30)
    filtered_data = dataset[dataset[col].isin(top_categories.index)]
    
    try:
        plt.figure(figsize=(18, 6))
        sns.countplot(data=filtered_data, x=col, order=top_categories.index)
        plt.title(f"Top 30 Count plot: {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred in count_plot_uni: {e}")

def bar_plot_uni(dataset, col):
    # Keep only top 20 categories
    top_categories = dataset[col].value_counts().nlargest(20)
    filtered_data = dataset[dataset[col].isin(top_categories.index)]
    
    try:
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_categories.index, y=top_categories.values, palette="viridis")
        plt.title(f"Top 20 Bar plot: {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred in bar_plot_uni: {e}")

def violin_plot_uni(dataset, col):
    # Filter top 20 categories
    top_categories = dataset[col].value_counts().nlargest(20)
    filtered_data = dataset[dataset[col].isin(top_categories.index)]
    
    try:
        plt.figure(figsize=(10, 6))
        sns.violinplot(data=filtered_data, x=col, order=top_categories.index)
        plt.title(f"Top 20 Violin plot: {col}")
        plt.xlabel(col)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred in violin_plot_uni: {e}")

def histogram_uni(dataset, col):
    # Filter top 20 categories
    top_categories = dataset[col].value_counts().nlargest(20)
    filtered_data = dataset[dataset[col].isin(top_categories.index)]
    
    try:
        plt.figure(figsize=(10, 6))
        sns.histplot(data=filtered_data, x=col)
        plt.title(f"Top 20 Hist plot: {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred in histogram_uni: {e}")

def pie_uni(dataset, col):
    # Filter top 20 categories
    top_categories = dataset[col].value_counts().nlargest(10)
    
    try:
        plt.figure(figsize=(8, 8))
        plt.pie(x=top_categories.values, labels=top_categories.index, startangle=90, autopct="%1.1f%%")
        plt.title(f"Top 10 {col}")
        plt.tight_layout()
        plt.show()
        plt.legend()
    except Exception as e:
        print(f"An error occurred in pie_uni: {e}")

# Bivariate plotting functions
import seaborn as sns
import matplotlib.pyplot as plt

# Updated plotting functions to show only the top 10 values

def box_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        # Filter to top 10 values in xcol1
        top_categories = dataset[xcol1].value_counts().nlargest(20).index
        filtered_data = dataset[dataset[xcol1].isin(top_categories)]
        
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=filtered_data, x=xcol1, y=ycol2, hue=hueDefault)
        plt.title(f"Top 20 Box plot: {xcol1} vs {ycol2}")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred in box_plot: {e}")

def scatter_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        top_categories = dataset[xcol1].value_counts().nlargest(20).index
        filtered_data = dataset[dataset[xcol1].isin(top_categories)]
        
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=filtered_data, x=xcol1, y=ycol2, hue=hueDefault)
        plt.title(f"Top 20 Scatter plot: {xcol1} vs {ycol2}")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred in scatter_plot: {e}")

def bar_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        top_categories = dataset[xcol1].value_counts().nlargest(20).index
        filtered_data = dataset[dataset[xcol1].isin(top_categories)]
        
        plt.figure(figsize=(10, 6))
        sns.barplot(data=filtered_data, x=xcol1, y=ycol2, hue=hueDefault)
        plt.title(f"Top 20 Bar plot: {xcol1} vs {ycol2}")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred in bar_plot: {e}")

def swarm_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        top_categories = dataset[xcol1].value_counts().nlargest(20).index
        filtered_data = dataset[dataset[xcol1].isin(top_categories)]
        
        plt.figure(figsize=(10, 6))
        sns.swarmplot(data=filtered_data, x=xcol1, y=ycol2, hue=hueDefault)
        plt.title(f"Top 20 Swarm plot: {xcol1} vs {ycol2}")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred in swarm_plot: {e}")

def strip_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        top_categories = dataset[xcol1].value_counts().nlargest(20).index
        filtered_data = dataset[dataset[xcol1].isin(top_categories)]
        
        plt.figure(figsize=(10, 6))
        sns.stripplot(data=filtered_data, x=xcol1, y=ycol2, hue=hueDefault)
        plt.title(f"Top 20 Strip plot: {xcol1} vs {ycol2}")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred in strip_plot: {e}")

def violin_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        top_categories = dataset[xcol1].value_counts().nlargest(10).index
        filtered_data = dataset[dataset[xcol1].isin(top_categories)]
        
        plt.figure(figsize=(10, 6))
        sns.violinplot(data=filtered_data, x=xcol1, y=ycol2, hue=hueDefault)
        plt.title(f"Top 10 Violin plot: {xcol1} vs {ycol2}")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred in violin_plot: {e}")

def line_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        # Get top 20 categories of the xcol1 column
        top_categories = dataset[xcol1].value_counts().nlargest(20).index
        
        # Filter the dataset for only those top categories
        filtered_data = dataset[dataset[xcol1].isin(top_categories)]
        
        # Create a line plot with Seaborn
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=filtered_data, x=xcol1, y=ycol2, hue=hueDefault, marker='o')
        
        # Set title and rotate x-ticks for better readability
        plt.title(f"Top 20 Line Plot: {xcol1} vs {ycol2}")
        plt.xticks(rotation=45, ha='right')
        
        # Adjust layout for tight fit
        plt.tight_layout()
        
        # Show the plot
        plt.show()
    except Exception as e:
        print(f"An error occurred in line_plot: {e}")

# Data cleaning function
def cleaning_dataset(data):
    print("Inside Cleaning Section.")
    """Here you are passing the dataset which you want to analyze."""
    dataset = data
    dataset.info()
    
    while True:
        print("\nEnter 1. to remove null \nEnter 2. to replace Na values \nEnter 3. to use up to certain quarters of data \nEnter 4. to drop duplicates \nEnter 5. to check for duplicates, Na values \nEnter 6. to exit \n")
    
        choice = int(input("Enter your choice: "))
        if choice == 6:
            break
        

        reference_data_in_use = dataset.copy()

        if choice == 1:
            reference_data_in_use.dropna(inplace=True)
        
        elif choice == 2:
            print("Do you want to replace it with a certain value? \nEnter Yes or No")
            col_name = input("Enter the name of the column: ")
            choice2 = input().capitalize()
            if choice2 == "Yes":
                value = input("Enter the value: ")
            else:
                print("Enter 1 to replace with mean \nEnter 2 to replace with median \nEnter 3 to replace with mode \n")
                choice3 = int(input())
                if choice3 == 1:
                    value = reference_data_in_use[col_name].mean() 
                elif choice3 == 2:
                    value = reference_data_in_use[col_name].median() 
                elif choice3 == 3:
                    value = reference_data_in_use[col_name].mode()[0]
                else:
                    print("Invalid choice for replacing Na values.")
                    continue
            
            reference_data_in_use[col_name].fillna(value, inplace=True)
        
        elif choice == 3:
            print("Enter the number of rows you want to use:")
            row_num1 = int(input("Enter start: "))
            row_num2 = int(input("Enter end: "))
            reference_data_in_use = reference_data_in_use.loc[row_num1: row_num2]
        
        elif choice == 4:
            reference_data_in_use.drop_duplicates(inplace=True)
        
        elif choice == 5:
            duplicates = reference_data_in_use.duplicated()
            print("Duplicate Rows:\n", reference_data_in_use[duplicates])
            print(f"\nNumber of duplicate rows: {duplicates.sum()}")
            nan_count = reference_data_in_use.isna().sum()
            print("\nNumber of NaN values in each column:\n", nan_count)
        
        else:
            print("Invalid choice. Please try again.")
            continue
        
        choose_analysis(reference_data_in_use)

# Analysis functions
def uni_analysis(dataset):
    print("Inside Uni_varaite analysis section")
    while True:
        print("\nMenu:")
        print("1. Count Plot")
        print("2. Bar Plot")
        print("3. Histogram")
        print("4. Pie Chart")
        print("5. Exit")
        
        choice = input("Select an option (1-6): ")

        if choice == '5':
            print("Exiting the program.")
            break

        col = input("Enter the column name for plotting: ")
        
        if choice == '1':
            count_plot_uni(dataset, col)
        elif choice == '2':
            bar_plot_uni(dataset, col)
        elif choice == '3':
            histogram_uni(dataset, col)
        elif choice == '4':
            pie_uni(dataset, col)
        else:
            print("Invalid choice, please select a valid option.")    

def bi_analysis(dataset):
    print("Inside Bivariate analysis Section.")
    hueDefault="genre"
    hue_columns = ["rating", "genre", "director", "writer", "star", "country", "company"]
    print(f"Possible Bivariate Pair's : {col_data.bivariate_analysis}")
    while True:
        print("\nMenu:")
        print("1. Box Plot")
        print("2. Scatter Plot")
        print("3. Bar Plot")
        print("4. Swarm Plot")
        print("5. Strip Plot")
        print("6. Violin Plot")
        print("7. line plot")
        print("8. Exit")
        
        choice = input("Select an option (1-7): ")

        if choice == '8':
            print("Exiting the program.")
            break
        
        xcol1 = input("Enter the x-axis column name: ")
        ycol2 = input("Enter the y-axis column name: ")
        # messagebox.showinfo(title="Default", message="Genre is set as the default hue parameter")

        print(hue_columns)
        hueDefault = input("\nEnter the hue column name (or press Enter for default): ")
        if hueDefault == "":
            hueDefault = None

        if choice == '1':
            box_plot(dataset, xcol1, ycol2, hueDefault)
        elif choice == '2':
            scatter_plot(dataset, xcol1, ycol2, hueDefault)
        elif choice == '3':
            bar_plot(dataset, xcol1, ycol2, hueDefault)
        elif choice == '4':
            swarm_plot(dataset, xcol1, ycol2, hueDefault)
        elif choice == '5':
            strip_plot(dataset, xcol1, ycol2, hueDefault)
        elif choice == '6':
            violin_plot(dataset, xcol1, ycol2, hueDefault)
        elif choice == '7':
            line_plot(dataset, xcol1, ycol2, hueDefault)
        else:
            print("Invalid choice, please select a valid option.")

def choose_analysis(dataset):
    print("Inside choose analysis section.")
    print("\n1. Univariate Analysis")
    print("2. Bivariate Analysis")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        uni_analysis(dataset)
    elif choice == 2:
        bi_analysis(dataset)
    else:
        print("Invalid choice, please try again.")

# Initial call to clean and analyze the dataset
cleaning_dataset(data)

# prediction model test and training

# Load the dataset
df = pd.read_csv('movies.csv')

# Fill missing values with the mean (for numerical columns only)
# df.fillna(df.mean(), inplace=True)
df.dropna(inplace=True)
# Step 1: Prepare your features (X) and target variable (y)
# Assuming 'gross' is the target variable you want to predict
# X = df.drop('gross', axis=1)  # Features (remove target column 'gross')
X= df.drop(columns=['name', 'rating', 'genre', 'company', 'released', 'director', 'writer', 'star', 'country','gross'])
print(X)
y = df['gross']  # Target variable (the 'gross' column)

# Step 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Initialize and train the regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Step 4: Make predictions
y_pred = regressor.predict(X_test)

# Step 5: Evaluate the model
# Calculate RMSE (Root Mean Squared Error)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Calculate R² (Coefficient of Determination)
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse}")
print(f"R²: {r2}")

# Step 6: Visualize the predictions vs actual values (for the test set)
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', edgecolors='k', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Values')
plt.show()

# Step 7: Save the model for future use (optional)
joblib.dump(regressor, 'linear_regression_model.pkl')
