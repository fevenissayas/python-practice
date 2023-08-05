import math # To use math.sqrt when solving the area. We could have used a different technique like ' **0.5 '.

def calc_area (): # Defining a function

    print ("Input the sides of the triangles :") # User input for each sides

    s1 = float (input ('a = '))
    s2 = float (input ('b = '))
    s3 = float (input ('c = '))

# Introducing the formulars to the code
    S = (s1 + s2 + s3)/2
    Area = math.sqrt (S * (S - s1) * (S - s2) * (S -s3))
    
    print ("Area of the triangle = ", Area)  # Displaying the calculated final amount.

    return Area # Returning the calculated final amount. However, removing this would not affect the code  unless we plan to use the calculated area elsewhere in this program

calc_area () # Calling the function to execute the code.


# The code would have still worked fine if we hadn't written the defined, returning, and calling parts at the beginning and end.
