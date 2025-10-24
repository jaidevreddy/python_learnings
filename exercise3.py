def exercise3(*args):

    current_num = None

    for i in args:

        if current_num == 0 and i == 0:
            return True
        
        current_num = i
    
    return False


print(exercise3(1,2,3,4,4,0))

