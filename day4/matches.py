user_data = {'name':'fed', 'role':'admin', 'age':30}

access = {'admin':{'server':'yes', 'ads':'yes'}}

items = [user_data,access,]

for i in items:

    match i:
        case {'role':'admin',
              'name':name}:
            print(f'{name} is admin')

        case {'admin':{'server':access,'ads':acces}}:
            if acces == access:
                print(f"{name} server access:{access}\nads access:{acces}")
        case _:
            print('no data')
