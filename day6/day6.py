#!/usr/bin/env python3

with open("./input", "r") as stuff:
    list1337 = []
    for item in stuff:
        list1337.append((item.strip()))

class answerInfo():
    def __init__(self,list1337):
        self.yesses = []
        self.matching = []
        self.list1337= list1337
        self.list1337.append('')

    def reset(self):
        self.letters = []
        self.uniqueLetters = []
        self.group = []

    def calc(self):
        self.reset()
        for line in self.list1337:
            if len(line) > 0:
                self.letters += set(line)
                self.group.append(line)
            elif len(line) == 0:
                self.uniqueLetters += set(self.letters)
                self.yesses.append(len(self.uniqueLetters))
                for char in set(self.letters):
                    for groupLine in self.group:
                        if char not in groupLine and char in self.uniqueLetters:
                            self.uniqueLetters.remove(char)
                self.matching.append(len(self.uniqueLetters))
                self.reset()
        return self
    def __repr__(self):
        return f'Part 1 answer: {sum(self.yesses)} and Part 2 answer: {sum(self.matching)}'

answer = answerInfo(list1337)
answer.calc()