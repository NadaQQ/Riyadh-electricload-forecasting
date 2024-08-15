import pandas as pd

# Step 1: Read your dataset into a DataFrame
df = pd.read_csv('data/merged_train_data.csv')

# Step 2: Reorder columns to make 'electric_load' the last column
columns = [col for col in df.columns if col != 'electric_load'] + ['electric_load']
df = df[columns]

# Step 3: Save the modified DataFrame back to a CSV file
df.to_csv('data/merged_train_data.csv', index=False)
