"""
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to
print this list after removing all duplicate 
values with original order reserved.
"""


def original_numbers(*args):
    return list(set(args))[::-1]


print(original_numbers(12, 24, 35, 24, 88, 120, 155, 88, 120, 155))