class person:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
  
name=input('Enter your name:')
age=input('Enter your age :') 
p=person(name,age)#p is a class instance 
print(p.name)
print(p.age)#when we call p.age python takes the instance and searches from the class..

# self- self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.       
        
#__init__ :->"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.        