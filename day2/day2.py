#!/usr/bin/env python3
import re

list1337 = []
with open("./day2_list", "r") as stuff:
    for item in stuff:
        list1337.append((item.strip()))

splittedList = []
for line in list1337:
    splittedList.append(re.split('-| |: ',line))

part1 = []
part2 = []
for row in splittedList:
    if (row[2] in row[3]) and int(row[0]) <= row[3].count(row[2]) <= int(row[1]):
        part1.append(row)
    if (row[3][int(row[0])-1] == row[2]) != (row[3][int(row[1])-1] == row[2]):
        part2.append(row)
print(len(part1),len(part2))