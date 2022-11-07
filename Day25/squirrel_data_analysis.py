import pandas
# Goal === to extract the number of colors for the squirels present in the squirel dataset
squirel_dataframe = pandas.read_csv("Squirrel_Data.csv")

#Method 1
# squirel_colors_list = squirel_dataframe["Primary Fur Color"].to_list()
# gray_count = 0
# cinnamon_count = 0
# black_count = 0
#
# for color in squirel_colors_list:
#     if color == "Gray":
#         gray_count += 1
#     if color == "Cinnamon":
#         cinnamon_count += 1
#     if color == "Black":
#         black_count += 1
#
# squirel_count = {
#         'Fur Color' : ["red", "black", "gray"],
#         'count': [cinnamon_count, black_count, gray_count]
#     }
#
# data = pandas.DataFrame(squirel_count)
# data.to_csv("squirel_count.csv")

# OR

gray_count = len(squirel_dataframe[squirel_dataframe["Primary Fur Color"] == "Gray"])
red_count = len(squirel_dataframe[squirel_dataframe["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirel_dataframe[squirel_dataframe["Primary Fur Color"] == "Black"])

squirel_count = {
    'Fur Color': ["red", "black", "gray"],
    'color_count': [red_count,black_count,gray_count]
}

df = pandas.DataFrame(squirel_count)
df.to_csv("squirel_count version1.1")