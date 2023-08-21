def find (lst, targ):
    i = 0
    while i < len (lst):
        if lst [i] == targ:
            return i
        i +=1
    return -1

print (find ([1,2,15,4],4))
    
    
