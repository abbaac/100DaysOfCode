import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(squirrel_data.columns)

fur_colour = squirrel_data["Primary Fur Color"].value_counts()

gray = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_color_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray, cinnamon, black]
}

squirrel_color_df = pd.DataFrame(squirrel_color_dict)
squirrel_color_df.to_csv("squirel_count.csv")
