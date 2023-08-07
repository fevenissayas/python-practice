def calulate_mount (): # Defining the function and using indention after.

    t = float (input ("Enter the number of years: ")) # User input for the number of years

    while t < 0: # A 'while' loop to exclude non-existing negative numbers in time.
        print ("Error. Please try using a non-negative number.")
        t = float (input ("Enter the number of years: ")) # Re-inquiring user input until a non-negative value is provided.

# Introducing the foluma given by substituting the values in the variables.
    A = 10000 * (1 + (0.8/12))**(12 * t) 

    print ("The final amount after", t, "years is: ", A) # We used comma, then t, then comma because t is interchangeable and in order for the code to reflect this modification.

    return A # Returning the calculated amount.

calculate_mount () # Calling the function to execute the calculation.
