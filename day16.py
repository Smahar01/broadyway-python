# nov 13 2024 Wednesday=====================================

# Inheritance
# single inheritance

# class Parent():  # parent class or super class 
#     a = 10
#     b = 99

# class Child(Parent):  # child class or sub class
#     c = 18
#     d = 11

#  # always use child class for object

# obj = Child()
# print(obj.a)

# class Parent1():
#     first_name = "sameer"

# class Child(Parent1):
#     last_name = "maharjan"

# obj = Child()
# print("full name is",obj.first_name, obj.last_name)


# class Parent():
#     a = 100

#     def test1(self):
#         return self.a
    
# class Child(Parent):
#     b = 12

#     def test2(self):
#         return self.a * self.b
    
# obj = Child()
# print(obj.test2())



# class Parent():
#     a = 100

#     def test1(self):
#         return self.a
    
# class Child(Parent):
#     b = 12

#     def test2(self):
#         return self.a * self.b
    
# obj = Child()
# print(obj.test2(), obj.test1())



# class Parent():
#     first_name = "sameer"

#     def first(self):
#         return self.first_name
    
# class Child(Parent):
#     last_name = "maharjan"

#     def second(self):
#         return self.first_name + " " + self.last_name
    
# obj = Child()
# print(obj.second())


# single Inheritance with constructor 

# class Parent():
#     def __init__(self):
#         print("Hi I am a constructor")
#         self.a = 10
#         return None
    
# class Child(Parent):
#     pass

# obj = Child()



# class Parent():
#     def __init__(self):
#         print("Hi I am a constructor")
#         self.a = 10
#         return None
    
# class Child(Parent):
#     pass

# obj = Child()
# print(obj.a)


# class Parent():
#     def __init__(self):
#         print("hi, I am a constructor-1")
#         self.a = 10

# class Child(Parent):
#     def __init__(self):
#         print("hi, I am a constructor-2")
#         self.b = self.a * 100

# obj = Child()
# print(obj.b)

# you get an error, Child object has no attribute 'a', as constructor-2 will run and a won't be called from Parent.
# you need to manualy call constructor-1 using Parent.__init__(self)

# class Parent():
#     def __init__(self):
#         print("hi, I am a constructor-1")
#         self.a = 10

# class Child(Parent): 
#        def __init__(self):
#           Parent.__init__(self) # manual calling constructor from Parent class, or you can use  super().__init__()
#           print("hi, I am a constructor-2")
#           self.b = self.a * 100

# obj = Child()
# print(obj.b)

# or you can simply use super().__init__(), to call the parent constructor class


# class Parent():

#     def __init__(self):
#         print("Hi, I am a constructor-1")
#         self.a = 30

#     def test1(self):
#         return 2
    
# class Child(Parent):

#     def __init__(self):
#         Parent.__init__(self)
#         print("Hi, I am a constructor-2")
#         self.b = self.a * 100

#     def test2(self):
#         return self.test1() * 25
    
# obj = Child()
# print(obj.test2())
              