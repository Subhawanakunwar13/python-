# list1={1,2,4,5,6,7}
# for i in list1:
#     print (1*2)

# output1 =[i*2 for i in list1 if i % 2==0]
# print(output1)

# #wap to print the square of even number from 1 to 100

# res=[i**2 for i in range(1,101) if i % 2==0]
# print(res)

# res=[i*7 for i in range(1,11)]
# print(res)
# [print (f"7 * {i} = {7*i}") for i in range(1,11)]

# calculator app using fun->add sub div mul ** // % exit and ask the  input for the user
#  2 will be numbers and will be option and recursion to call the function again and again 
#until the user wants to exit

def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 / num2
def expo(num1,num2):
    return num1 ** num2
def calculator():
    print("welcome to calculator app")
    print("1.Add")
    print("2.subtract")
    print("three.multiplication")
    print("4.division")
    print("5.eponentiaton")
    print("6.exit")
    options= int(input("select your options:"))
    list_of_options = [1,2,3,4,5]
    if options in list_of_options:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if options == 1:
            print(f"Result: {add(num1, num2)}")
            return calculator()
        elif options == 2:
            print(f"Result: {sub(num1, num2)}")
            return calculator()
        elif options == 3:
            print(f"Result: {div(num1, num2)}")
            return calculator()
        elif options == 4:
                print(f"Result: {mul(num1, num2)}")
                return calculator()
        elif options == 5:
            print(f"Result: {expo(num1, num2)}")
            return calculator()
        else:
            print("Exiting the calculator app")
            return
    
calculator()


# global and local variable in python
abc= 19
def name():
    bcd=20
    print("this is a name function ")
    return abc+bcd
    print(bcd)

    print(name())
    print(abc)

    #print(bcd)
    #wap to print factorial of a number using recursion.

def factorial(num):
    if num==0:
        return
    else
        return num*factorial(num-1)
    

