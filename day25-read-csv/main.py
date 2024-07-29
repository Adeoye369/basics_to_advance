# import csv

# data_row =[]
# with open('day25-read-csv/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)
#         data_row.append(row)


# # method 1: extract all second column
# print ([temp_data[1] for temp_data in data_row[1:]])

# # method 2: much longer but easier to understand
# temperatures = []
# for temp in data_row[1:]:
#     temperatures.append(temp[1])

# print(temperatures)


import pandas as pd

# data = pd.read_csv("day25-read-csv/weather_data.csv")

# monday = data[data.day == "Monday"]
# monday_temperature  = monday['temp']
# print(monday_temperature)
# temp_in_celsius = round((monday_temperature.loc[0] - 32) * (5/9), 2)
# print(temp_in_celsius)

# creating DataFrame from scratch

movie_dict = {
    'movie': ["A to Z", "Movers ", "Born to Live", 'omolope'],
    'release_date': [1997, 2012, 2023, 2020],
    'rating' : [9.5, 1.4, 8.8, 0.96]
}

# create data from movie dictionary
movie_data = pd.DataFrame(movie_dict)

# Display movie data
# print(movie_data)
# print(movie_data["rating"].loc[2])
# convert it to csv and save in directory
# movie_data.to_csv('day25-read-csv/movie_data.csv')

# Testing 1
print(movie_data[movie_data.rating >= 1.4])




