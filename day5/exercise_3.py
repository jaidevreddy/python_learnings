def consecutive_zero(*args):

    for i in range(len(args)):
        if args[i] == 0 and args[i-1]==0:
            return True

    return False


print(consecutive_zero(1,2,3,4,3,6,8,4,6,3,53,5,3,5,3,5,3,2,6,8,9,6,5,5,000,6,5,57,0,2,5,0,8,4,3,53))

            

