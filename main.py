import tkinter
import pandas as pd
import os
import matplotlib as plt
import seaborn as sns
from tkinter import messagebox 
data = pd.read_csv("movies.csv")
# print(data.head())
colunm_name = data.columns
print(len(colunm_name))

def box_plot(dataset,xcol1, ycol2, hueDefault ):
    messagebox.showinfo(title="default", message="genre is set as by default hue parameter")
    plt.ylabel(f'{ycol2}', fontsize=12, color='green')
    plt.xlabel(f'{xcol1}', fontsize=12, color='green')
    x=dataset[xcol1].unique()
    y=dataset[ycol2].unique()
    plt.figure(figsize=(x/2, y/2))
    sns.boxplot(data=dataset, x= xcol1, y= ycol2, hue=hueDefault)
    plt.show()
    
def scatter_plot(dataset,xcol1, ycol2, hueDefault ):
    plt.ylabel(f'{ycol2}', fontsize=12, color='green')
    plt.xlabel(f'{xcol1}', fontsize=12, color='green')
    x=dataset[xcol1].unique()
    y=dataset[ycol2].unique()
    plt.figure(figsize=(x/2, y/2))
    sns.scatterplot(data=dataset, x=xcol1, y=ycol2, hue=hueDefault)
    plt.show()     
    
def bar_plot(dataset, xcol1, ycol2, hueDefault):
    plt.ylabel(f'{ycol2}', fontsize=12, color='green')
    plt.xlabel(f'{xcol1}', fontsize=12, color='green')
    x=dataset[xcol1].unique()
    y=dataset[ycol2].unique()
    plt.figure(figsize=(x/2, y/2))
    sns.barplot(data=dataset, x=xcol1, y=ycol2, hue=hueDefault)
    plt.show()         
    
def swarm_plot(dataset, xcol1, ycol2, hueDefault):
    plt.ylabel(f'{ycol2}', fontsize=12, color='green')
    plt.xlabel(f'{xcol1}', fontsize=12, color='green')
    x=dataset[xcol1].unique()
    y=dataset[ycol2].unique()
    plt.figure(figsize=(x/2, y/2))
    sns.swarmplot(data=dataset, x=xcol1, y=ycol2, hue=hueDefault )
    plt.show()    
    
def strip_plot(dataset, xcol1, ycol2, hueDefault):
    plt.ylabel(f'{ycol2}', fontsize=12, color='green')
    plt.xlabel(f'{xcol1}', fontsize=12, color='green')
    x=dataset[xcol1].unique()
    y=dataset[ycol2].unique()
    plt.figure(figsize=(x/2, y/2))
    sns.stripplot(data=dataset, x=xcol1, y=ycol2, hue=hueDefault)
    plt.show()
    
def violin_plot(dataset, xcol1, ycol2, hueDefault):
    plt.ylabel(f'{ycol2}', fontsize=12, color='green')
    plt.xlabel(f'{xcol1}', fontsize=12, color='green')
    x=dataset[xcol1].unique()
    y=dataset[ycol2].unique()
    plt.figure(figsize=(x/2, y/2))
    sns.catplot(data=dataset, x=xcol1, y=ycol2, hue=hueDefault, kind="violin")
    plt.show()        
    
def count_plot_uni(dataset, col):
    sns.countplot(data=dataset, x=col)
    plt.title(f"count plot : {col}")
    plt.xlabel(col)
    plt.ylabel("count")
    plt.show()
    
def bar_plot_uni(dataset, col):
    sns.barplot(data=dataset, x=col)
    plt.title(f"bar plot : {col}")
    plt.xlabel(col)
    plt.ylabel("count")
    plt.show()
    
def violin_plot_uni(dataset, col):
    sns.violinplot(data=dataset, x=col)
    plt.title(f"violin plot : {col}")
    plt.xlabel(col)
    plt.show()
    
def histogram_uni(dataset, col):
    sns.histplot(data=dataset, x=col)
    plt.title(f"Hist plot : {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()
    
def pie_uni(dataset, col):
    size=dataset[col].values_count()
    label=dataset[col].unique()
    plt.pie(x=size, labels=label,startangle=0, autopct="%1.1f%%")
    plt.title(f"{col}")
    plt.show()    
    
def bi_analysis(dataset):
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

        if choice == '7':
            print("Exiting the program.")
            break

        xcol1 = input("Enter the x-axis column name: ")
        ycol2 = input("Enter the y-axis column name: ")
        hueDefault = input("Enter the hue column name (or press Enter for default): ") or None
        
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
    
    
        