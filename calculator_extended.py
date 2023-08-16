# We made an effort to write code that can handle both real and complex number arithmetic.


print ("What kind of arithmetic are you solving: ")
print ("1. Complex number arithmetic")
print ("2. Real number arithmetic")

choice = eval (input ("Your choice? ")) #User input

if choice == 1: #this is for the complex number arithmetic.
 
    def complex_arithmetic (a, b):
        print ("Addition:" , a + b)
        print ("Substraction:" , a - b)
        print ("Multiplication:" , a * b)

        # Below, we tried to add restrictions for division so that the code doesn't stop functioning when 0 is used as a denominator.
        if b == 0:
            print("Division: Undefined (Zero division error!)")
        else:
            print("Division:", a / b)

    # This is also a user input. But here, 'complex_a' is written as (a, ia). The same is true for b.
            
    real_a = float(input("Enter the real value of 'a': "))
    img_a = float(input("Enter the imaginary value of 'a': "))
 
    complex_a = complex (real_a, img_a)
 
    real_b = float(input("Enter the real value of 'b': "))
    img_b = float(input("Enter the imaginary value of 'b': "))
 
    complex_b = complex (real_b, img_b) # (b, ib)

    complex_arithmetic (complex_a, complex_b) # Calling the complex number arithmetic function. 

elif choice == 2: #this is for the real number arithmetic.
 
    def real_arithmetic ():

        print ("How do you want your results to be written: ")
        print ("1. in Integer")
        print ("2. in Float")
        
        option = int (input ("Your option? ")) # User input
        a = float(input("Enter the value of 'a': "))
        b = float(input("Enter the value of 'b': "))
   
        if option == 1: #This yields an integer value in the end.
            
            print ("Addition:" , int(a + b))
            print ("Substraction:" , int(a - b))
            print ("Multiplication:" , int(a * b))
            
            if b == 0: #We also added restrictions here.
                print("Division: Undefined (Zero division error!)")
            else:
                print("Division:", int (a / b))

        elif option == 2: # Float operation.
            print ("Addition:" , a + b)
            print ("Substraction:" , a - b)
            print ("Multiplication:" , a * b)
            
            if b == 0: # Restriction similar to the two mentioned above.
                print("Division: Undefined (Zero division error!)")
            else:
                print("Division:", a / b)

    real_arithmetic () # Calling the real number arithmetic function.

