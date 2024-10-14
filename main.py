import tkinter
import pandas as pd
import os
import matplotlib.pyplot as plt  # Corrected the import statement
import seaborn as sns
from tkinter import messagebox 
from data import bivariate_analysis, bivariate_pairs

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

# Print the number of columns
column_name = data.columns
print(len(column_name))

def box_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        
        plt.ylabel(f'{ycol2}', fontsize=12, color='green')
        plt.xlabel(f'{xcol1}', fontsize=12, color='green')
        x = dataset[xcol1].unique()
        y = dataset[ycol2].unique()
        plt.figure(figsize=(len(x)/2, len(y)/2))  # Fixed figure size logic
        sns.boxplot(data=dataset, x=xcol1, y=ycol2, hue=hueDefault)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred in box_plot: {e}")

def scatter_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        plt.ylabel(f'{ycol2}', fontsize=12, color='green')
        plt.xlabel(f'{xcol1}', fontsize=12, color='green')
        plt.figure(figsize=(10, 6))  # Fixed figure size
        sns.scatterplot(data=dataset, x=xcol1, y=ycol2, hue=hueDefault)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred in scatter_plot: {e}")

def bar_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        plt.ylabel(f'{ycol2}', fontsize=12, color='green')
        plt.xlabel(f'{xcol1}', fontsize=12, color='green')
        plt.figure(figsize=(10, 6))  # Fixed figure size
        sns.barplot(data=dataset, x=xcol1, y=ycol2, hue=hueDefault)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred in bar_plot: {e}")

def swarm_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        plt.ylabel(f'{ycol2}', fontsize=12, color='green')
        plt.xlabel(f'{xcol1}', fontsize=12, color='green')
        plt.figure(figsize=(10, 6))  # Fixed figure size
        sns.swarmplot(data=dataset, x=xcol1, y=ycol2, hue=hueDefault)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred in swarm_plot: {e}")

def strip_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        plt.ylabel(f'{ycol2}', fontsize=12, color='green')
        plt.xlabel(f'{xcol1}', fontsize=12, color='green')
        plt.figure(figsize=(10, 6))  # Fixed figure size
        sns.stripplot(data=dataset, x=xcol1, y=ycol2, hue=hueDefault)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred in strip_plot: {e}")

def violin_plot(dataset, xcol1, ycol2, hueDefault):
    try:
        plt.ylabel(f'{ycol2}', fontsize=12, color='green')
        plt.xlabel(f'{xcol1}', fontsize=12, color='green')
        plt.figure(figsize=(10, 6))  # Fixed figure size
        sns.violinplot(data=dataset, x=xcol1, y=ycol2, hue=hueDefault)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred in violin_plot: {e}")

def count_plot_uni(dataset, col):
    try:
        sns.countplot(data=dataset, x=col)
        plt.title(f"Count plot: {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred in count_plot_uni: {e}")

def bar_plot_uni(dataset, col):
    try:
        sns.barplot(data=dataset, x=col)
        plt.title(f"Bar plot: {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred in bar_plot_uni: {e}")

def violin_plot_uni(dataset, col):
    try:
        sns.violinplot(data=dataset, x=col)
        plt.title(f"Violin plot: {col}")
        plt.xlabel(col)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred in violin_plot_uni: {e}")

def histogram_uni(dataset, col):
    try:
        sns.histplot(data=dataset, x=col)
        plt.title(f"Hist plot: {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred in histogram_uni: {e}")

def pie_uni(dataset, col):
    try:
        size = dataset[col].value_counts()  # Corrected method call
        labels = dataset[col].unique()
        plt.pie(x=size, labels=labels, startangle=0, autopct="%1.1f%%")
        plt.title(f"{col}")
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred in pie_uni: {e}")

def bi_analysis(dataset):
    hueDefault="genre"
    hue_columns = [    "rating",    "genre",    "director",    "writer",    "star",    "country",    "company"]

    while True:
        print("\nMenu:")
        print("1. Box Plot")
        print("2. Scatter Plot")
        print("3. Bar Plot")
        print("4. Swarm Plot")
        print("5. Strip Plot")
        print("6. Violin Plot")
        print("7. Exit")
        
        choice = input("Select an option (1-7): ")

        if choice == '8':
            print("Exiting the program.")
            break
        
        print(f"Possible Bivariate Pair's : {bivariate_pairs}")    
        xcol1 = input("Enter the x-axis column name: ")
        ycol2 = input("Enter the y-axis column name: ")
        messagebox.showinfo(title="Default", message="Genre is set as the default hue parameter")
        print(hue_columns)
        hueDefault = input("\nEnter the hue column name (or press Enter for default): ") or None
        
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
        else:
            print("Invalid choice, please select a valid option.")

def uni_analysis(dataset):
    while True:
        print("\nMenu:")
        print("1. Count Plot")
        print("2. Bar Plot")
        print("3. Violin Plot")
        print("4. Histogram")
        print("5. Pie Chart")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")

        if choice == '6':
            print("Exiting the program.")
            break

        col = input("Enter the column name for plotting: ")
        
        if choice == '1':
            count_plot_uni(dataset, col)
        elif choice == '2':
            bar_plot_uni(dataset, col)
        elif choice == '3':
            violin_plot_uni(dataset, col)
        elif choice == '4':
            histogram_uni(dataset, col)
        elif choice == '5':
            pie_uni(dataset, col)
        else:
            print("Invalid choice, please select a valid option.")    

def choose_analysis(data):
    try:
        print("\nEnter 1. to do Univariate graph Plotting \nEnter 2. to do Bivariate graph Plotting:")
        choice = int(input())
        if choice == 1:
            uni_analysis(data)
        elif choice == 2:
            bi_analysis(data)
        else:
            print("Invalid choice. Please enter either 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def cleaning_dataset(data):
    """Here you are passing the dataset which you want to analyze."""
    dataset = data
    dataset.info()
    print("\nEnter 1. to remove null \nEnter 2. to replace Na values \nEnter 3. to use up to certain quarters of data \nEnter 4. to drop duplicates \nEnter 5. to check for duplicates, Na values \nEnter 6. to exit \n")
    
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 6:
            break
        
        col_name = input("Enter the name of the column: ")
        reference_data_in_use = dataset.copy()  

        if choice == 1:
            reference_data_in_use.dropna(inplace=True)
        
        elif choice == 2:
            print("Do you want to replace it with a certain value? \nEnter Yes or No")
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
