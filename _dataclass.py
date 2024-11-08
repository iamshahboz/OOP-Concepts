# # standart example

# class Person():
#     def __init__(self, name, age, height, email):
#         self.name = name 
#         self.age = age
#         self.height = height
#         self.email = email 
        
        
# using dataclass
'''
while using @dataclass decorator, we no longer need to write __init__ function
'''
from dataclasses import dataclass 
from typing import Tuple

@dataclass
class Person():
    name: str 
    age: int
    height: float 
    email: str 
    house_coordinates: Tuple
    
Person1 = Person(name='Jack', age='13', height=2.10, email='jack@jones.com', house_coordinates=(40.748441, -73.985664))
print(Person1.house_coordinates)

    
'''
We could also set a default value
'''