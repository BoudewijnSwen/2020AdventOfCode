#!/usr/bin/env python3
import re

with open("./input", "r") as stuff:
    list1337 = []
    for item in stuff:
        list1337.append((item.strip()))

class rulert():
    def __init__(self,line):
        self.outer = {}
        self.inner = {}
        bla = (re.split(' bags contain ',line))
        self.outer['shade'] = (re.split(' ',bla[0]))[0]
        self.outer['color'] = (re.split(' ',bla[0]))[1]
        if ',' in bla[1]:
            innersList = (re.split(', ',bla[1]))
            counter = 1
            for container in innersList:
                containerParts = re.split(' ',container)
                self.inner["container{0}".format(counter)] = {}
                self.inner["container{0}".format(counter)]["amount"] = int(containerParts[0])
                self.inner["container{0}".format(counter)]["shade"] = containerParts[1]
                self.inner["container{0}".format(counter)]["color"] = containerParts[2]
                counter += 1
        else:
            try:
                inner1Temp = (re.split(' ',bla[1]))
                self.inner['container1'] = {}
                self.inner['container1']['amount'] = int(inner1Temp[0])
                self.inner['container1']['shade'] = inner1Temp[1]
                self.inner['container1']['color'] = inner1Temp[2]
            except:
                self.inner = {}
                pass
    def __repr__(self):
        return f"Rule contains: \nOuter container: {self.outer} \nCan contain {len(self.inner)} different containers"

def zoek(shade,color,ruleList):
    canContain = []
    for rule in ruleList:
        if len(rule.inner) != 0:
            for container in rule.inner:
                if rule.inner[container]['shade'] == shade and rule.inner[container]['color'] == color:
                    canContain.append(rule.outer['shade'] + rule.outer['color'])
                    subContain = zoek(rule.outer['shade'],rule.outer['color'],ruleList)
                    canContain.extend(subContain)
    return canContain

def zoek_amount(shade,color,ruleList):
    amount = 0
    for rule in ruleList:
        if rule.outer['shade'] == shade and rule.outer['color'] == color:
            if len(rule.inner) != 0:
                for container in rule.inner:
                    amount += rule.inner[container]['amount']
                    amount += (rule.inner[container]['amount'] * zoek_amount(rule.inner[container]['shade'],rule.inner[container]['color'],ruleList))
    return amount

ruleList = []
for line in list1337:
    ruleList.append(rulert(line))

answerP1 = zoek('shiny','gold',ruleList)
answerP2 = zoek_amount('shiny','gold',ruleList)
print(f'Answer to part 1: {len(set(answerP1))} and the answer to part 2: {answerP2}')