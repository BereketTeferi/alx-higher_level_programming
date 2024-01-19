#!/usr/bin/python3
def multiple_returns(sentence):
    first = ''
    length = 0
    for i in sentence:
        first = i
        break
    for i in sentence:
        length += 1

    return length, first
