#!/usr/bin/python3
import hidden_4

if _name_ == "_main_":
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
