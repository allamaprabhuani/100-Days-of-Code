# import csv
#
# with open('weather-data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(row[1])
#     print(temperatures)
#

import pandas

data = pandas.read_csv('weather-data.csv')

data_dict = data.to_dict()
data_list = data['temp'].to_list()
# print(data_list)
# print(data_dict)

print(sum(data['temp']) / len(data['temp']))

## or
print(data['temp'].mean())

print(data['temp'].max())

### to column:

print(data['condition'])

print(data.condition)

## from rows:

print(data[data.day == 'Monday'])

print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)
print((monday.temp * 9 / 5) + 32)

# Create dataframe

data_dic = {
    'students': ['Amy', 'James', 'Amanda'],
    'scores'  : [76, 55, 92]
}

data = pandas.DataFrame(data_dic)
data.to_csv('new_data.csv')

