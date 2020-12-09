#!/usr/bin/env python3
with open("./input", "r") as stuff:
    list1337 = []
    for item in stuff:
        list1337.append((item.strip()))

def treeHugger(list1337,right,down):
    pos = 0
    line = 0
    tree = 0
    while line < len(list1337):
        if list1337[line][pos] == '#':
            tree += 1
        pos += right
        if pos > len(list1337[line])-1:
            pos -= len(list1337[line])
        line += down
    return tree

part1 = treeHugger(list1337,3,1)
part2 = treeHugger(list1337,1,1) * part1 * treeHugger(list1337,5,1) * treeHugger(list1337,7,1) * treeHugger(list1337,1,2)

print("part 1 result = {} and the answer for part 2 = {}".format(part1,part2))