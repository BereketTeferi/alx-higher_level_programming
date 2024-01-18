#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    lists = dir(hidden_4)
    for list in lists:
        if list[:2] != "__":
            print(list)
