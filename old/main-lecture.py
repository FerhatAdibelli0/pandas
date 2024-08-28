# with open("industry.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("ferhat.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)

import pandas

# data["Fullname"] This is Data Series
# data This is Data Frame

# data = pandas.read_csv("ferhat.csv")
# print(type(data.columns))
# print(sum(data[data.columns[1]])/len(data.columns[1]))
# print(data.to_dict())
# print(data[data.columns[1]].mean())
# print(data[data.columns[1]].max())

# Get the related row
# print(data[data.Identifier == data["Identifier"].max()])
# ferhat = data[data.Username == "ferhat"]
# number = ferhat.Identifier.iloc[0]
# print(number)
# print((number * 9/5) + 32)

# data_docs = {
#     "names": ["Ferhat", "libelled", "Charm"],
#     "numbers": [12, 45, 90]
# }
#
# data_frame = pandas.DataFrame(data_docs)
# data_frame.to_csv("ferhat-new.csv")
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240820.csv")
park_squirrel_gray = len(data[data["Primary Fur Color"] == "Gray"])
park_squirrel_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
park_squirrel_black = len(data[data["Primary Fur Color"] == "Black"])


print(park_squirrel_gray)
print(park_squirrel_cinnamon)
print(park_squirrel_black)

new_data = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "counts": [park_squirrel_gray, park_squirrel_cinnamon, park_squirrel_black]
}

squirrel_count = pandas.DataFrame(new_data)
squirrel_count.to_csv("squirrel_color_count")


