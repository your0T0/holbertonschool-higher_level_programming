#!/usr/bin/python3
def uppercase(str):
    out = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            out += chr(ord(c) - 32)
        else:
            out += c
    print("{}".format(out))
