#!/usr/bin/python3
import sys

if _name_ == "_main_":
    total = 0
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print(total)
