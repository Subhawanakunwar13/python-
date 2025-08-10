# #oop-. object oriented programming
# #programming paradigm based on the concept of program
# #class, object,mathods,attributes, decorators,magic/dundermethods
# #4 pillars -> inheritance ,encapsulation,polymorphism abtraction

# class Abc:
# #class attributes/properties /variables ,methods, and constructor
#     name = "Subhawana"
#     age =44
#     gender = "female"

# def printDetails(self):
#     print(f"name: {self.name},age: {self.age}, gender: {self.gender} ")
# #object -> instance of a class containts attributes and methods
# one =Abc()
# print(one.name)
# one.name = "sub"
# print(one.name)
# print(one.age)
# print(one.gender)
  
#   #wap to create a class for with attributes like name,model,year and methods like start stop and display

# class Abc:
#   name = "suzuki"
#   model = "der"
#   year = 2022
  
#   def start(self):
#      print(f"name:{self.name},model :{self.model},year :{self.year}")
# obj=Abc()
# obj.start()
# obj.stop()
# obj.display()

# ##wap to create a class for with attributes like name,model,year and methods like start
# #  stop and display info using constructor
# class Student:
#   def _init_(self,name,age,year,):
#      self.name = name
#      self.age = age
#      self.year = year
  
#   class Ones:
#      two ="this is a class variable"

#   def one(self):
#     print(f"This is mathod one {self.two}")
#   def twos(clas):
#     print(f"class methods:{clas.method}")    
#   def three (clas):
#      print("class method")
#   def four(a,b):
#      print(f"sum::{a+b}")
#      one.twos()
#      one.threes(10,20) 


#      #wap 

def add_five (func):
    def wrapper(*args,**kwargs):
      result = func(*args,**kwargs)
      return result +5
    return wrapper
@add_five
def add_numbers(a):
    return a 
print(add_numbers(10))


