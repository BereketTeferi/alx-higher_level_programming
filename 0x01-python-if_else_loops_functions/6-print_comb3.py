#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        print(f"{min(i, j)}{max(i, j)}", end=", ")

print()