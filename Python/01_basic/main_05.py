# dict1={
#     "name":"Subhawana Kunwar",
#     "age":25,
#     "city":"New York"

# }
# print(dict1)
# print(dict1["name"])
# dict1["name"]="Sayuri"
# print(dict1["name"])
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# print(dict1.get("age"))
# dict1.pop("age")
# print(dict1)
# dict1.update({"name":"Ram","age":56,"city":"New"})
# print(dict1)

# #loop in python 
# #for lop ,while loo,nested loop
# #break,continue,pass

# for i in range(0,11):
#      print(i)

#      print("hello world",0)
#      print("hello world",100)

#      for i in range(0,101):
#         print("hello world",i)
         
         
#         i=0
#         while i<101:
#            print("hello world",i)
#            i+=1


#            #wap to print mul table of 7
#         for i in range(0,11):
#             print(f"7*{i}={i*7}")

#         for i in range(0,11):
#             print(f"the table if {i} is:")
#         for j in range(0,11):
#             print(f"{i}*{j}={i*j}")

# for i in range(1,100):
#     if(i%2==0):
#       print(i)  

# a=0
# b=1
# i=0
# print(a,b)
# while i<100:
#    c=a+b
#    print(c)
#    a=b


for i in range(0,6):
    print("*"*i)



sum=0
for i in range(0,100):
    sum+=1
    print(sum)


for i in range(0,101):
    if(i%5==0 and i%7==0):
        print("fizzbuzz")
    elif(i%5==0):
       print("fizz")
    elif(i%7==0):
       print("buzz")
    

for i in range (0,11):
    if (i==5):
        break
    print(i)

for i in range(0,11):
    if(i==5):
        continue
    print(i)
               
                

