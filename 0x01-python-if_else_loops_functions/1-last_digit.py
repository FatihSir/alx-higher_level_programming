#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    digit = int(str(number)[-1])
elif number < 0:
    digit = int("-" + str(number)[-1])
if digit > 5:
    status = "and is greater than 5"
elif digit == 0:
    status = "and is 0"
elif digit < 6 and digit != 0:
    status = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, digit, status))
