"""
Template for the COMP1730/6730 project assignment, S2 2020.
The assignment specification is available on the course web site:
https://cs.anu.edu.au/courses/comp1730/assessment/project/

The assignment is due 25/10/2020 at 11.55 pm, Canberra time.

Collaborators: <list the UIDs of ALL members of your project group here>
"""

import csv
'''
This function is to decompose elements in list which contains day, month, and year to only contain year.
The year is an int.
'''
def improve_content(seq):
    i = 0
    l = []
    while i < len(seq):
        l.append(int(seq[i][-4:]))  #The year is consist with 4 numbers.
        i = i + 1
    return l

with open(r"C:\Users\53598\PycharmProjects\pythonProject2\aqi_data_civic.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    data = [row for row in reader]
    list1 = []
    for row in data:
        if row[-4] == '':  # Because the null str cannot be change to an int, the null str is ignored.
            pass
        else:
            if int(row[-4]) >100:  #Create a list that contains two row including pm2.5 AQI and datetime
                list1.append(row)

    list2 = [row[-2] for row in list1]  # Selecting the element's date which pm2.5 AQI > 100.
    list3 = list(set(list2))  # Delete overlap about same date in different time.
    list_final = improve_content(list3)
    list_final.sort()

print(list_final.count(2016))
print(list_final.count(2017))
print(list_final.count(2018))
print(list_final.count(2019))
print(list_final.count(2020))

