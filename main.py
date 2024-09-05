import pandas as pd

# Load Coffee Data
coffee_data = pd.read_csv('psd_coffee.csv', encoding='latin1')

# Load World Population Data
# population_data = pd.read_csv('path_to_population_data.csv', skiprows=4)

# Load Country Codes Data
#country_codes_data = pd.read_csv('countries-codes.csv')

print(coffee_data.shape)
print(coffee_data.info())
print(coffee_data.head())