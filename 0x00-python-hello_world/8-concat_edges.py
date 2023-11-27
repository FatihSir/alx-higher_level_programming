#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split(", ")[2].split()[0] + str.split(", ")[2][67:73] + str[:6]
print(str)
