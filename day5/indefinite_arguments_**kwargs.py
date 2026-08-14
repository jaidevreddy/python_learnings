def number_attributes(**kwargs):
    return len(kwargs)


def list_attributes(**kwargs):
    
    return list(kwargs.values())



def describe_person(name,**kwargs):
    
    print(f"Characteristics of {name}:")
    
    for key,value in kwargs.items():
        
        print(f"{key}: {value}")