import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Car A', 'Car B', 'Car C', 'Car D', 'Car E'],
    'Price': [25000, 30000, 35000, 40000, 45000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Customize the export settings
custom_header = ['Product', 'Price']

df.to_excel('output.xlsx', index=False, na_rep='N/A', header=custom_header, index_label='ID')