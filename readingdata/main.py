import pandas

squirrel_dataset = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
squirrel_colors = squirrel_dataset["Primary Fur Color"]
print(squirrel_dataset[squirrel_dataset.X == -73.9561344937861]["Primary Fur Color"])

squirrel_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [0, 0, 0]
}

for color in squirrel_colors:

    if color == squirrel_data["Fur Color"][0]:
        squirrel_data["count"][0] += 1
    elif color == squirrel_data["Fur Color"][1]:
        squirrel_data["count"][1] += 1
    elif color == squirrel_data["Fur Color"][2]:
        squirrel_data["count"][2] += 1

squirrel_census_frame = pandas.DataFrame(squirrel_data)
squirrel_census_frame.to_csv("2018_count_squirrels_centralpark_bycolor.csv")
