import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset with exception handling
try:
    data = pd.read_csv("10000 Sales Records.csv")
except FileNotFoundError:
    print("Error: '10000 Sales Records.csv' file not found. Please check the file path.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: No data found in '10000 Sales Records.csv'.")
    exit()
except pd.errors.ParserError:
    print("Error: Parsing '10000 Sales Records.csv' failed. Please check the file format.")
    exit()

# Define the column to plot
col = "Country"

# Get the top N categories to reduce clutter
top_categories = data[col].value_counts().nlargest(10).index  # Show only top 10 categories
filtered_data = data[data[col].isin(top_categories)]

# Plot
plt.figure(figsize=(10, 6))  # Adjust figure size
sns.histplot(data=filtered_data, x=col, shrink=0.8, palette="viridis")  # Shrink bars to avoid overlap
plt.title(f"Histogram of Top 10 {col}")
plt.xlabel(col)
plt.ylabel("Frequency")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Ensure everything fits properly
plt.show()
