import math

x1,y1 = eval(input("x1: ")), eval(input("y1: "))
x2,y2 = eval(input("x2: ")), eval(input("y2: "))

def distance (x1,y1,x2,y2):
    D = math.sqrt(((x2-x1)**2 + (y2-y1)**2))
    return D

print(distance(x1,y1,x2,y2))

