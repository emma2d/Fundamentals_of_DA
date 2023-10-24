import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

col_names = ["species", "island", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex"]

missing_values = ["NA", "N/A"]

penguin_data = pd.read_csv(url, names=col_names, na_values=missing_values)
#print(penguin_data.head())
#print(penguin_data)

Adelie = penguin_data[penguin_data['sex'] == "Adelie"]
print(Adelie.describe)



