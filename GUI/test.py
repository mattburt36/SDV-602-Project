import pandas as pd

# Read the data from the CSV folder of "Ukrainian_food" and store in a variable that will not be altered 
food_data_frame = pd.read_csv('Ukrainian_food.csv', low_memory=False)
food_data_frame.drop(0, axis=0, inplace=True)

food_data_frame['date'] = pd.to_datetime(food_data_frame['date'])
food_data_frame['year'] = food_data_frame['date'].dt.year

district_list = food_data_frame['market'].tolist()
commodity_list = food_data_frame['commodity'].tolist()
year_list = food_data_frame['year'].to_list()

df=food_data_frame.loc[food_data_frame['commodity'] == "cereals and tubers", 'price'].item()

print(df)
