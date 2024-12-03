# class UserInfo():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def full_name(self):
#         return self.first_name + " " + self.last_name

# obj = UserInfo("sameer", "maharjan")
# print(obj.full_name())

# November 10th, Sunday ###########################################################
'''
Class
Python is an object oriented programming language
Almost everything in Python is an object , with its properties and methods.
A class is like an object constructor, or a "blueprint"  for creating objects
As we know Python is an Object oriented programming language, to make python OOP, we use class.
we use or create object to call class in python.



# syntax

class <Classname>():
    code_block
    # class properties or class attributes
    a =2

    # method
    def test():
        print("this is class method")

        
a = <Classname>()

'''

# class Broadway():
#     student = 2

# a = Broadway()
# print(a.student)

# class Car():
#     brand = 5

# a = Car()
# print(a.brand)



# Nov 11th, Monday =========================================================

# class Python():
#     a = "hello"
#     b = "hi"

# obj = Python()
# print(obj.a)
# print(obj.b)

# obj.a = "this is changed data"
# print(obj.a)

# obj1 = Python()
# print(obj1.a)


# class Test2():
#     a = 10

#     def hello(self):
#         b = a
#         return b 
    
# obj = Test2()
# print(obj.a)
# print(obj.hello()) 


# class Test2():
#     data = 10

#     def hello(self):
#         b = self.data
#         return b
# obj = Test2()
# print(obj.data)
# print("this is from hello()", obj.hello())

# string retrun function in class: This is used when a developer write a code and he wants to display some messages once
# the code is run or completed.

# class Math():
#     a = 100
#     b = 10

#     def __str__(self):
#         return "Hello is string return function, the code is completed"
    
# obj = Math()
# print(obj)


# CONSTRUCTOR METHOD: capture arguments

# class Subjects():
#     def __init__(self):
#         print("this is init")

# obj = Subjects()

# class Subjects():
#     def __init__(self,a,b):
#         self.c = a
#         self.d = b
#         print("this is init", a,b)

#     def test5(self):
#         print(self.c)

# obj = Subjects(1,2)
# obj.test5()

# class UserInfo():
#     def __init__(self, first_name, last_name):
#         self.first = first_name
#         self.last = last_name


#     def full_name(self):
#         return self.first + " " + self.last
    
# obj = UserInfo("sameer", "maharjan")
# print(obj.full_name())

'''
# INHERITANCE 
# It allows us to define a class that inherits all the methods and properties from another class
# Parent class is the class being inherited from, also called base class
# child class is the class that inherits from another class, also called derived class.

1. singel inheritance: 
2. multi level inheritance
3. multiple inheritance

always create object from a child class


'''

