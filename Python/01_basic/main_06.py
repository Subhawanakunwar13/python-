# def hello():
#     print("hello world ")
# hello()
# hello()
# hello()

def printName(name):
    print(f"hello world{name}")
    printName("Ram")
    printName("Sita")
# printName("name") 
# printName("name")

# print(getinfo())
# return(f"hello world{name}")
#no parameter ,no return ->hello
# no parameter ,no return->printname(name)
# no parameter ,return->getinfo()
# parameter,return->add(a,b)

#parameter type in python fun
def defaultParameters (a=0,b=20):
    print(a+b)
   
defaultParameters()
defaultParameters(10)
defaultParameters(40,20)
    
    #wap to print the power of two numbers using default pparameter
def power(a=2,b=4):
    print(a**b)  
power()

def normalFun(name,age):
    print(f"name is {name} and age is{age}")
normalFun(age= 25,name= "Sub")
   

def abc(*args,**kwargs):
    print(args)
    print(kwargs)
abc("ktm","dcl","palpa",name="Sub",age=25)

#wap to use the parameter type in a single function
def parametertype(a,b,c=20,*args,**kwargs):
  
  print(f"a:{a},b:{b},c{c}")
  print("additional args:",args)
  print("keyword kwargs:",kwargs)
parametertype(1,44,56,7,6,7,8,6,9,6,9,6,6,9,6,name="Sayuri",town="darchula",gender="female") 


# def-> lambda fun -> ananymous fun()
x= lambda :20
print(x())
adds= lambda a,b:a+b
print(adds(10,20))

#wap to print the given value is even or odd using lambda function

result= lambda a,b:a+b
print(result(4,5))
res=lambda a:f"{a} is even" if a%2==0 else f"{a} is odd"
print(res(5))

def rec(n):
    if n==0:
        return 0
    else:
        print(n)
        return n + rec (n-1)
print(rec(10))    
    



