# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

# import pandas as pd
# import numpy as np

# data = pd.read_csv("10000 Sales Records.csv")

# print(data.columns)

# region = data["Region"].unique()
# country = data["Country"].unique()
# item = data["Item Type"].unique()
# sales = data["Sales Channel"].unique()

# print(region)
# print(country)
# print(item)
# print(sales)

# # Function to assign a number to each item type
# def assign_item_type_number(item_type):
#     if item_type == 'Office Supplies':
#         return 0
#     elif item_type == 'Beverages':
#         return 1
#     elif item_type == 'Vegetables':
#         return 2
#     elif item_type == 'Household':
#         return 3
#     elif item_type == 'Baby Food':
#         return 4
#     elif item_type == 'Meat':
#         return 5
#     elif item_type == 'Cereal':
#         return 6
#     elif item_type == 'Clothes':
#         return 7
#     elif item_type == 'Snacks':
#         return 8
#     elif item_type == 'Personal Care':
#         return 9
#     elif item_type == 'Cosmetics':
#         return 10
#     elif item_type == 'Fruits':
#         return 11
#     else:
#         return -1  # Return -1 for any item type not listed

# # Function to assign a number to each sales channel
# def assign_sales_channel_number(sales_channel):
#     if sales_channel == 'Online':
#         return 0
#     elif sales_channel == 'Offline':
#         return 1
#     else:
#         return -1  # Return -1 for any sales channel not listed

# # Example usage with a sample dataframe
# import pandas as pd

# # Apply the functions to the relevant columns
# data['Item_Type_Number'] = data['Item Type'].apply(assign_item_type_number)
# data['Sales_Channel_Number'] = data['Sales Channel'].apply(assign_sales_channel_number)

# # Display the updated DataFrame
# print(data)


# x=data.drop(columns=["Region","Country","Order Priority","Order Date","Order ID","Ship Date"])
# y=data["Total Cost"]


# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=42)

# model = LinearRegression()
# model.fit(x_train,y_train)

# print(model.intercept_)
# print(model.coef_)

# y_pred = model.predict(x_test)
# print(y_pred)

# rmse = np.sqrt(mean_squared_error(y_test,y_pred))
# r2 = r2_score(y_test,y_pred)

# print(rmse)
# print(r2)\\
    
    
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("10000 Sales Records.csv")

# Display the columns in the dataset
print(data.columns)

# Get unique values for exploration
region = data["Region"].unique()
country = data["Country"].unique()
item_types = data["Item Type"].unique()
sales_channels = data["Sales Channel"].unique()

# Print unique values for each category
print("Regions:", region)
print("Countries:", country)
print("Item Types:", item_types)
print("Sales Channels:", sales_channels)

# Function to assign a number to each item type
def assign_item_type_number(item_type):
    item_type_mapping = {
        'Office Supplies': 0,
        'Beverages': 1,
        'Vegetables': 2,
        'Household': 3,
        'Baby Food': 4,
        'Meat': 5,
        'Cereal': 6,
        'Clothes': 7,
        'Snacks': 8,
        'Personal Care': 9,
        'Cosmetics': 10,
        'Fruits': 11
    }
    return item_type_mapping.get(item_type, -1)  # Default to -1 if not found

# Function to assign a number to each sales channel
def assign_sales_channel_number(sales_channel):
    sales_channel_mapping = {
        'Online': 0,
        'Offline': 1
    }
    return sales_channel_mapping.get(sales_channel, -1)  # Default to -1 if not found

# Apply the functions to the relevant columns
data['Item_Type_Number'] = data['Item Type'].apply(assign_item_type_number)
data['Sales_Channel_Number'] = data['Sales Channel'].apply(assign_sales_channel_number)

# Display the updated DataFrame
print(data)

# Drop unnecessary columns and select features for the model
x = data.drop(columns=["Region", "Country", "Order Priority", "Order Date", "Order ID", "Ship Date", "Total Cost"])
y = data["Total Cost"]

# Check for missing values and handle them if necessary
if x.isnull().values.any() or y.isnull().values.any():
    print("Missing values detected. Dropping missing values...")
    x.dropna(inplace=True)
    y = y[x.index]  # Align y with x after dropping

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(x_train, y_train)

# Print the intercept and coefficients
print("Model Intercept:", model.intercept_)
print("Model Coefficients:", model.coef_)

# Make predictions on the test set
y_pred = model.predict(x_test)

# Calculate RMSE and R² score
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print("Root Mean Squared Error (RMSE):", rmse)
print("R² Score:", r2)
    