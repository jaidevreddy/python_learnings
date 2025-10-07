pet = (input("enter your pet: ")).lower()

if pet == 'cat':
    print("you have a cat")
elif pet == 'dog':
    print("you have a dog")
elif pet == 'fish':
    print('you have a fish')
else:
    print("i dont know what animal that is")


age = int (input("enter your age: "))

if age < 18:
    school_grade = int(input("enter your grade: "))
    print("you are a minor")
    if school_grade >= 7:
        print("passed")
    else: 
        print("failed")
else:
    print("your an adult")