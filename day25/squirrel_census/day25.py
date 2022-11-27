# with open('weather_data.csv') as f:
#     data = f.readlines()
#     print(data)

'''
import csv

with open('weather_data.csv') as f:
    data = csv.reader(f)
    temperatures = []
    for row in data:
        temp = row[1]
        if temp != 'temp':
            temperatures.append(int(temp))
    print(temperatures)
'''

import pandas as pd

# df = pd.read_csv('weather_data.csv')
# df_dict = df.to_dict()
# print(df_dict)

# temp_list = df['temp'].to_list()
# print(temp_list)

# avg_temp = df['temp'].agg('average')
# print(avg_temp)

# max_temp = df['temp'].max()
# print(max_temp)

# #can also refer to column name with dot notation.. df['temp'] is same as df.temp
# maxx_temp = df.temp.max()
# print(maxx_temp)

# #get a row, get the row df[df['temp'] where the max temp is]
# row = df[df['temp'] == df['temp'].max()]
# print(row)

# monday = df[df['day'] == 'Monday']
# monday = int(monday['temp']) * 9/5 + 32
# print(monday)

# #create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 77]
#     }

# data = pd.DataFrame(data_dict)
# data.to_csv('new_data.csv')

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray = len(df[df['Primary Fur Color'] == 'Gray'])
cinnamon = len(df[df['Primary Fur Color'] == 'Cinnamon'])
black = len(df[df['Primary Fur Color'] == 'Black'])

data_dict = {
    'fur_color': ['gray', 'cinnamon', 'black'],
    'count': [gray, cinnamon, black]
    }

squirrels = pd.DataFrame(data_dict)
squirrels.to_csv('squirrels.csv')