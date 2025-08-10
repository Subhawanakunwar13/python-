# operation nd operators
print(5+5)
#operand number 5,5
# operator +
#python 7
#Arithmetic operators
print("add",5+5)
print("sub",5-5)
print ("div",5/5)
print("mul",5*5)
print("rem",5%5)
print("power",5**2)
print("//",5//5)

#print(f"the sum of 2 number is{5+6}")

#assignment aperators 
#,=,+=,/=,//=,%=,*=
a=10
print(a)
a+=10
print(a)
a-=2
print(a)
a*=10
print(a)
a**=4
print(a)
a/=2
print(a)
a%=2
print(a)
a//=2
print(a)


#comparison operators -> boolen
# ==,>,<,!=,<=,>=
print(5==5)
print(5>5)
print(5<=5)
print(5>=5)
print(5!=4)

#logical operators -> and or not

print(True and True)
print(True and False)
print(False and True)
print(False and False)
 
print(True or True)
print(True or False)
print(False or True)
print(False or False)
 
print( not True)
print( not False)


#identify operators

a=20
b=20
print(a is b)
a=20
b=40
print (a is not b)



# membership operators in and not in-> bool

list1=[1,2,4,5]
print(4 in list1)
print(6 not in list1)


#bitwisse operators ->,|,% ,^
print(5&5)
print(5&4)


# ternary operator

age=20
print("above 18" if (age>20) else "below 18")

#wap to print the number is odd or not by asking from the user 

num=int(input("enter number"))
print("odd num" if num %2!=0 else "even num")

age=21
print ("driver" if age>21 else "below age")


#conditionsin python 
# if else elif,match
value= 50
if(value %2!=0):
     print("the given value is odd")
elif(value==0):
     print("it is 0")
elif(value>94):
     print("the given value is above 94")
else :
     print ("the given value is even")


#num= int(input("enter the number"))
#if (num=="buzz"):
     #num1=num/7
     #print(f'the number is divide by seven{num}')


     #match statement

     day= "tuesday"
     match(day):
        case"sunday":
               print("its sunday")
               case"monday":
               print("its monday")
               case "tueday":
               pritnt("its tueday")
       




