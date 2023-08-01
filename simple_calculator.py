# SECTION 13

# 1. ENATFANTA ZERIHUN GETACHEW	(UGR/6344/15)
# 2. ERMIAS MEQUANINT MINTESNOT	(UGR/6851/15)
# 3. EYERUSALEM TEKLEBRHAN GEBREMARIAM	(UGR/6149/15)
# 4. EYOB ASSEFA SHIKUR	(UGR/9773/15)
# 5. FEVEN ISSAYAS MULUGETA   (UGR/9815/15)


def calculator ():

    print ("Enter two numbers you want to calculate\n") # User input of the two numbers.
    a = float (input ("The first number: "))
    b = float (input ("The second number: ")) # 'int' instead of 'float' would have worked too, but it would exclude numbers with decimal points.

    print ("Addition: ", a + b) # Operation of the two numbers.
    print ("Substraction: ", a - b)
    print ("Multiplication: ", a * b)

# Below, we tried to add restrictions for division so that the code doesn't stop functioning when 0 is used as a denominator.

    if b == 0:
        print ("Division: Zero Division Error!")
    elif b==0:
        print ("Division", a / b)

calculator () # Calling the function to proceed and display the code.
