#Python program to create and manipulate a DataFrame with information about Students using Pandas Library.
import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [20, 22, 21, 23],
    'Grade': ['A', 'B', 'C', 'A']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Basic DataFrame Operations
print("\nBasic DataFrame Operations:")

# Accessing a Column
print("Accessing the 'Name' column:")
print(df['Name'])

# Adding a New Column
df['Gender'] = ['Female', 'Male', 'Male', 'Male']
print("\nAdding a 'Gender' column:")
print(df)

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Filtering Data
print("\nFiltering Data:")
filtered_df = df[df['Age'] > 21]
print(filtered_df)

# Sorting Data
print("\nSorting Data:")
sorted_df = df.sort_values(by='Age')
print(sorted_df)
