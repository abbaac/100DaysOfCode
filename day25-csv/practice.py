# with open("weather_data.csv", "r") as data_files:
#     data = data_files.readlines()
#     print(data)

import csv
import pandas as pd

# Open csv file with csv module
with open("weather_data.csv", "r") as data_files:
    data = csv.reader(data_files)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    # print(temperatures)

    
## Open csv file with pandas
data = pd.read_csv("weather_data.csv")

## Access column
# print(data["temp"])

## Calculations
# average = data["temp"].mean()

# max_temp = data[data.temp == data.temp.max()]
# print(max_temp)


## Filter column with queries
# monday = data[data.day == "Monday"]

# monday.temp[0] = monday.temp[0] * 1.8 + 32
# print(monday)


## Dictionary to DataFrame

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("student_data.csv")



