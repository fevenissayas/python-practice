def str_palio (x):
    if len (x) < 2:
        return True

    if x[0] != x[-1]:
        return False

    return (str_palio (x [1:-1]))


if __name__ == "__main__":

    x = "racecar"
    if str_palio (x) is True:
        print ("is palio")
    else:
        print ("not palio")