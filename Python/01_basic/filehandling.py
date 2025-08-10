# #read
# # fs=open("hello.txt",mode="r+")
# # print(fs.read())
# # print(fs.readline())
# # fs.close()
 
#  #write
# fs1=open("hello.txt", mode="w" )
# fs1.write("hello world")
# fs1.close()

# fs1=open("hello.text",mode="w+")
# fs1.write("hi Subhawana")
# fs1.seek(0)
# one=fs1.read()
# print(one)
# fs1.close()
# #append
# fs4=open("hello.txt",mode="a+")
# fs4.write(fs4 )

#wap to print the table of 7 using file hndling
with open("01_basic/text/hello.txt","w+")as fs:
    for i in range(1,11):
        fs.write(f"7*{1}={7*i}\n")
        print(fs.read()) 

for i in range(1,11):
    with open(f"01_basic/table/multiply{i}.txt","w+") as fs: 
        for j in range(1,11):
            fs.write(f"{i}*{j}={j*i}\n")
            print(fs.read())

# make a program using oop concpt by create a class name Student and make a constructor
#  and function base also need to ask input from the user with options like add new student,
# ( update student and delete student ) using roll no, show all students and exit, also make 
# a menu for the user and use while loop to call the function again and again until the user 
# wants to exit need to record file in txt format and also need to save the data in the file 
# and load the data from the file.

import os
class Student:
    def __init__(self,name, rollno, age, course, marks):
        self.name = name
        self.rollno =rollno
        self.age =age
        self.course =course
        self.mark=marks

    def _str_(self):
        return f"Name: {self.name}, Rollno:{self.rllno},Age:{self.age}, Course:{self.course}, MArks:{self.marks}"
    def printDetails(self):
        print(f"Name: {self.name}, Rollno:{self.rllno},Age:{self.age}, Course:{self.course}, MArks:{self.marks}")
   
   
    def addStudent():
        try:
            with open("students.txt","a") as f:
                name = input("enter name:")
                rollno =input("enter rollno:")
                age = input("enter age:")
                course = input("enter course:")
                marks = input("enter marks:")

    def searchStudent():
        pass
    def updateStudent():
        pass
    def deleteDtudent():
        pass
    def shoeAllStudents():
        try:
            with open("students.txt","r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No records found.")        

    def menu():
        print("welcome")
        print("1.Add Student")
        print("2. Search Student")
        print("4. Update Student")
        print("5.Delete Stuent")
        print("6. Show All Students")
