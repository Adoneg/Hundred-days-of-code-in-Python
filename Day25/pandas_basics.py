import pandas
data = pandas.read_csv("temp_data.csv")
# data --- is call a dataframe or simple excel spreadsheet where we can get data from

# temp_list = data["temp"].to_list()
# # data["temp"] or in general data["column"] is a series and can be use to access data in a particular column specified
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())

# Accessing row data
day2 = data[data.day == "Tuesday"]  # or data[data["day"] == "Tuesday"]
# getting the row with the max temp
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_farh = (9/5 * monday_temp) + 32
print(monday_temp_farh)

# create a dataframe from scratch
student_score = {
    'student': ["Lyonnie", "Afeh", "Junior", "Miriam"],
    'score':[12,32,12,34]
}

data = pandas.DataFrame(student_score)
data.to_csv("student_score")
