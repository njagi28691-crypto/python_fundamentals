import os

#friends = 10
#friends = friends +1
#friends += 1
#friends = friends - 2
#friends -= 2
#friends = friends * 3
#friends *= 3
#friends = friends / 2 
#friends /= 2
#friends = friends ** 2
#friends **= 2
#remainder = friends % 3


# round() ; rounding a number
# abs() : absolute number
#pow() : power fxn
#max() : max value btwn numbers

#x = 3.14
#y = 4
#z = 5
#result = round(x)
#result = abs(y)
#result = pow(y,3)
#result = min(x,y,z)
#math.ceil() :rounds upwards
#math.floor() :rounds downwards

import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

c = math.sqrt(a**2 + b**2)
print(f"side c = {c}")