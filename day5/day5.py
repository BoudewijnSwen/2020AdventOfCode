#!/usr/bin/env python3

with open("./input", "r") as stuff:
    list1337 = []
    for item in stuff:
        list1337.append((item.strip()))

def calculator(num,indicator):
    diff = num[1] - num [0] + 1
    if num[1] - num [0] == 1:
        newNum = num[0] if indicator == "F" or indicator == "L" else num[1]
    elif indicator == "F" or indicator == "L":
        newNum = (num[0],int(num[1] - diff/2))
    elif indicator == "B" or indicator == "R":
        newNum = (int(num[0] + diff/2),num[1])
    return newNum

seatList = []
for line in list1337:
    start = (0,127)
    position = (0,7)
    for lineSegment in line[0:7]:
        start = calculator(start,lineSegment)
    finalRow = start
    for lineSegment in line[7:10]:
        position = calculator(position,lineSegment)
    finalPosition = position
    seatList.append(finalRow * 8 + finalPosition)

print("part 1 result = {} and the answer for part 2 = {}".format(max(seatList),[seat for seat in [ele for ele in range(max(seatList)+1) if ele not in seatList] if seat > min(seatList) and seat < max(seatList)]))