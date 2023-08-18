G = 6.674 * (10 **(-11)) # Putting in the given value.

def Gravitational_Force(): # Defining the function. The reason we didn't put in parameters is because everything is included inside the function. If, let's say, m1, m2, and r were outside the function, we would have written the parameter as (m1, m2, r).

    # Using indentation to determine the scope of the code it blocks.
    print ("Enter the values of each :")
    m1 = float (input ('mass 1 (in kg)= '))    
    m2 = float (input ('mass 2 (in kg)= '))
    r = float (input ('radius (in m)= '))
    
    Force = (G * m1 * m2)/(r * r) # Using the BODMAS. We could also write "r  * r" as "r ** 2".
    
    print ("Gravitational Force =", Force, "N") # Printing the code and adding its SI unit.

Gravitational_Force () # Calling the function to start execution.
