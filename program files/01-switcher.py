# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:42:31 2022

@author: mmacarty
"""

x = 5
y = 10

print(f"The value of x is {x}")
print(f"The value of y is {y}")

_x = 5
x = y
y = _x

print(f"The value of x is {x}")
print(f"The value of y is {y}")

x, y = y, x

print(f"The value of x is {x}")
print(f"The value of y is {y}")
