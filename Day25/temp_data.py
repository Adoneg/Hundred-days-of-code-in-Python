# with open("./temp_data.csv") as temp_data:
#     data = temp_data.readlines()
#     print(data)

# 0R

import csv
with open("./temp_data.csv") as temp_data:
    data = csv.reader(temp_data) # creates an object that can be looped thru
    temp_list = []
    for row in data:
        if row[1] != "temp":
            temp_list.append(int(row[1]))
    print(temp_list)


