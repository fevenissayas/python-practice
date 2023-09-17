"""simulating movement of an elevator (^ for going up and v for going down)"""

x = "^vvvvv^^v"
def elevator (x):
    floor = 0
    for i in x:
        if i == '^':
            floor += 1
        elif i == 'v':
            if floor > 0:
                floor -= 1

    return floor

print (elevator (x))
