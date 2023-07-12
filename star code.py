x = 6

#i = 0, 1, 2, 3, 4, 5

def right_angled ():
    
    for i in range (x):
        for j in range (i):
            print ('*', end = ' ')
        print ()
    for i in range (x-2, 0, -1):
        for j in range (i):
            print ('*', end = ' ')
        print ()


def triangle ():

    for i in range (x-1,0, -1):
        for j in range (i):
            print ('*', end = ' ')
        print ()
        print (end = ' '* (x-i))


def pyramid ():
          
    for i in range (x):
        print (end = ' '* (x-i))
        for j in range (i):
            print ('*', end = ' ')
        print ()
    for i in range (x-2,0, -1):
        print (end = ' '* (x-i))
        for j in range (i):
            print ('*', end = ' ')
        print ()


for i in range (x):
    for j in range (x-i,0, -1):
        print (' ', end = ' ')
    for k in range (i):
        print ('*', end = ' ')
    print ()


























        
    
