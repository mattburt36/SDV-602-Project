import pandas as pd
import matplotlib.pyplot as plt

# Store CSV file in pandas dataframe 
df = pd.read_csv('wfp_food_prices_ukr.csv')

# .to_string() will display more than the first 5 rows and last 5 rows 
# .info() will display the information about the rows, entries and data columns
# .dropna(inplace = True) removes empty rows 
# .dropna(subset=['x'], inplace = True) removes empty rows with data under x column 
# .fillna(x, inplace = True) fills empty cells with value of x
# [y].fillna(x, inplace = True) fills empty cells with x at y columns 
# print(df)

# plot as graph, not working yet as needs numeric values 
df.plot()

plt.show()