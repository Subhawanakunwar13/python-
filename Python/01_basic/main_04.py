# #string manipulation 
 
# name ="Subhawana\Kunwar "
# print("hi\'s my name is Subhawana")
# print(name)
# print(name[0])
# print(name[-6:-1])
# print(name[::-1])


# one ="hello world"
# two="hello world"
# three ="hello world"
# four="22244"
# print(one.upper())
# print(one.capitalize())
# print(one.split())
# print(one.strip())
# print(one.replace("world","python"))
# print(one.find("world"))
# print(three.isupper())
# print(three.islower())
# print(two.istitle())
# print(two.isalpha())
# print(four.isdigit())
# print(four.isalnum())

# #wap to print if the given value is palindrome or not 121-121


# a="121"
# b=a[::-1]
# if (a==b):
#     print("the number is palindrome")
# else:
#     print("the number is not palindrome")

#     #list in python
# list1=[1,2,4,5,6,7]
# print(list1)
# print(list1.index(5))
# list1.append(6)
# print(list1)
# list1.insert(0,7)
# print(list1)
# list1.remove(7)
# print(list1)
# list1.reverse()
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)


# tupl=(1,2,4,5,6,7,8)
# list2=(1,2,4,5,6,7)
# print(tupl)
# list2[9]=10
# print(list2)

# print(tupl.count(1))
# print(tupl.count(4))
    

# tup1=(1,2, 4,5,6,7)
# list2=list(tup1)
# list2.append("Subhawana")
# tup2=tuple(list2)
# print(tup2)

# #for loop
# for i in tup2:
#     print(i)
#     for i in list2:

        #set
set1={1,4,5,6,8,9,56,4,1,57,9,97}
print(set1)
set1.add(11)
print(set1)
set1.remove(1)
print(set1)
set2={5,6,7,8,5,9,}
print(set2)
set4=set1.union(set2)
print(set4)
set5=set1.intersection(set4)
print(set5)
set5.clear()
list1=[1,2,4,5,6,7,8,9]
for i in set1:
   print(i)
   
