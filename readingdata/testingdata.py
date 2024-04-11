# with open("./weather_data.csv", mode="r") as weather_data:
#     list_weather = weather_data.readlines()
#     data = list_weather[1:]
#
# print(data)

# import csv
# with open("./weather_data.csv", mode="r") as weather_data:
#     temperature = []
#     data = csv.reader(weather_data)
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
#     print(temperature)
import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
#print(data["temp"])
#print(data_dict)

#turning data to list
temp_list = data["temp"].to_list()
# print(temp_list)
#
# #printing avg
# print(f"Avg: {sum(temp_list)/len(temp_list)}")
# #using pandas to print average
# print(f"Average temp is: {data['temp'].mean()}")
#
# print(f"Max temp of the week is {data['temp'].max()}")
#
# #getting columns in 2 ways
# print(data["condition"])
# print(data.condition)

# #get data in a row
# print(data[data.day == 'Monday'] )

#getting row for max temp
# print(data[data.temp == data.temp.max()])

# print(data[data.condition=='Sunny'])

monday_temp = data[data.day =='Monday'].temp.to_list()
print(f"Mondays temperature is {monday_temp[0]} C which is {float(monday_temp[0]) * (9/5) + 32} F")


#creating own data frame

data_dict = {
    "students": ["Lily","Peter","Sam"],
    "scores": [23,45,55]
}
mydata = pandas.DataFrame(data_dict)
print(mydata)

#can turn this data frame to csv as well
mydata.to_csv("newdata.csv")