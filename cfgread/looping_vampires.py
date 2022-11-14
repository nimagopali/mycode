#!/usr/bin/env python3
count = 0

with open("./dracula.txt", "r") as draculafile:
    with open("vampytimex.txt", "w") as fang:
        for line in draculafile:
            if "vampire" in  line.lower():
                print(line)
                count +=1
                fang.write(line)

print(count)

