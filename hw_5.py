﻿"""
Write a program to read last n lines of a file.
"""


def read_last_lines(n):
    with open('examples/history EETS .txt', 'r') as f:
        return f.readlines()[-n:]


print(read_last_lines(10))
