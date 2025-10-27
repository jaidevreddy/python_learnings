print("")
print("Right angle triangle with numbers")
print("")

row = 5

for i in range(1,row+1):

    for j in range(1,i+1):
        print(j,end=' ')
    
    print("")


print("")
print("right angle with '*'")
print('')

row = 5

for i in range (1,row+1):

    for j in range(1,i+1):
        print('*',end=' ')
    
    print("")


print("")
print("reverse right angle triangle with numbers")
print('')

n =5 
k =5

for i in range(0,n+1):

    for j in range(k-i,0,-1):
        print(j,end=' ')
    
    print("")