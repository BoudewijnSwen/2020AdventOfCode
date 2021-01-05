#!/usr/bin/env python3\
import re

with open("./input", "r") as stuff:
    list1337 = []
    for item in stuff:
        list1337.append((item.strip()))

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

validPassportP1 = 0
validPassportP2 = 0
validFieldsP1 = 0
validFieldsP2 = 0

for row in list1337:
    # Part 1
    if len(row) == 0 or validFieldsP1 == 7:
        validFieldsP1 = 0
    for rowPart in re.split(" ",row):
        if rowPart[0:3] in fields:
            validFieldsP1 += 1
    if validFieldsP1 == 7:
        validPassportP1 += 1
    # Part 2
    if row == "" or validFieldsP2 == 7:
        validFieldsP2 = 0
    for rowPart in row.split(" "):
        if rowPart.split(":")[0] == "byr":
            if 1920 <= int(rowPart.split(":")[1]) <= 2002:
                validFieldsP2 += 1
        elif rowPart.split(":")[0] == "iyr":
            if 2010 <= int(rowPart.split(":")[1]) <= 2020:
                validFieldsP2 += 1
        elif rowPart.split(":")[0] == "eyr":
            if 2020 <= int(rowPart.split(":")[1]) <= 2030:
                validFieldsP2 += 1
        elif rowPart.split(":")[0] == "hgt":
            if rowPart.split(":")[1][-2:] == "in":
                if 59 <= int(rowPart.split(":")[1][:-2]) <= 76:
                    validFieldsP2 += 1
            elif rowPart.split(":")[1][-2:] == "cm":
                if 150 <= int(rowPart.split(":")[1][:-2]) <= 193:
                    validFieldsP2 += 1
        elif rowPart.split(":")[0] == "hcl":
            if (len(rowPart.split(":")[1]) == 7) and re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', rowPart.split(":")[1]):
                validFieldsP2 += 1
        elif rowPart.split(":")[0] == "ecl":
            if rowPart.split(":")[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                validFieldsP2 += 1
        elif rowPart.split(":")[0] == "pid":
            if len(rowPart.split(":")[1]) == 9:
                try:
                    int(rowPart.split(":")[1])
                    validFieldsP2 += 1
                except:
                    pass
    if validFieldsP2 == 7:
        validPassportP2 += 1
print("part 1 result = {} and the answer for part 2 = {}".format(validPassportP1,validPassportP2))