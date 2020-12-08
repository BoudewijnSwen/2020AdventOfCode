#!/usr/bin/env python3
with open("./day1_list", "r") as stuff:
    list1337 = []
    for item in stuff:
        list1337.append(int(item.strip()))
    for x in list1337:
        for y in list1337:  
            if x + y == 2020:
                print(x * y)
