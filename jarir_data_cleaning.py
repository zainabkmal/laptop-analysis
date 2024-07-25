import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel( '/Users/zainab/Desktop/jarir_data.xlsx' , sheet_name='Sheet1')

# Function to split the specs into columns
def split_specs(specs):
    specs_list = specs.split('\n')
    unique_specs_list = list(dict.fromkeys(specs_list))
    return pd.Series(unique_specs_list)

# Apply the function to the 'product_specs' column
specs_df = df['product_specs'].apply(split_specs)
# Rename columns
specs_df.columns = ['Screen Size', 'CPU', 'RAM', 'Storage', 'OS', 'Graphics']
# Concatenate the original DataFrame with the new specs columns
df = pd.concat([df, specs_df], axis=1)
# Optionally, save the result to a new CSV file
df.to_csv('jarir_updated.csv', index=False)


