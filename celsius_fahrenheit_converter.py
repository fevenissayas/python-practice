# First, we start with the main function.

def main ():
    c = float (input ("Enter the temprature in celcius: ")) # This is a user input. And the reason why we used 'float' instead of 'int' is for precision of the result.

# We used the while loop to add restrictions since the minimum temperature is zero kelvin. So, if we use '-300', per se, the code will take you back to rewrite a number above zero kelvin.
    while c < -273.15:
        print ("Error. Contradicts with Absolute Zero. Please try again.")
        c = float (input ("Enter the temprature in celcius: "))

    f = celc_to_farh (c)
    print ("The temprature in Fahrenheit is: ", f) #The degree in F will now be printed (with the use of the function we defined at the bottom).

def celc_to_farh (d): # "d" is the parameter we used to represent the Celsius degree. If we had used another letter, it wouldn't have mattered since it corresponds to that one letter 'c' in function 'f = celc_to_farh (c).'
    F = (1.8 * d) + 32
    return F # Returning the function.

main () # This calls the main function and starts the execution.
