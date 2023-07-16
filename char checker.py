def char_checker(s1, s2): 
    flag = True 
    for char in s1: 
        if char in s2: 
            continue
        else: 
            flag = False 
    print (flag) 
char_checker('na', 'PYnative')
