def exponents(func):
    def wrapper (*args,**kwargs):
        results=func(*args,**kwargs)
        return results**2
    return wrapper

@exponents 
def calculate(a,b):
    return(a+b)

print(calculate(10,40))

# class Person:
#     def _init_(self,firstname,lastname):
#         self.firstname=firstname
#         self.lastname=lastname
#         @property 
#         def fullname(self):
#             return f"{self.firstname},{self.lastname}"
# obj1=Person("sub" ,"Kunwar")
# print(obj1.firstname)
# print(obj1.lastname)
# print(obj1.fullname)

#inheritance

# 


class Parent:
    def __init__(self,lastname):
        self.lastname=lastname
    def hello(self):
        print("hello from child class",)
class Child(Parent):
    def _init_(self,firstname,lastname):
        self.firstname=firstname
        super()._init_(lastname)

    def hi(self):
       print(f'{self.firstname}{self.lastname}')
obj2=Child("fdjfhgf","dfgdfgd")
obj2.hello()
obj2.hi()
         
                

