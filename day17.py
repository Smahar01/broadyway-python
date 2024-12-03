### November 14th 2024, Thursday

# Multiple level inheritance

# class Parent():
#     a = 100
#     def parent_metho(self):
#         self.b = self.a
#         return self.b

# class Child1(Parent):
#     c = 70
#     def child1_method(self):
#         return self.c

# class Child2(Child1):
#     def child2_method(self):
#         self.d = 90
#         return self.d  + self.a + self.c
    
# obj = Child2()
# print(obj.child2_method())

# OR you can do as below by calling the function in line 40, #         self.child1_method()


# class Parent():
#     a = 100
#     def parent_metho(self):
#         self.b = self.a
#         return self.b

# class Child1(Parent):
#     def child1_method(self):
#         self.c = self.a - 40
#         return self.c

# class Child2(Child1):
#     def child2_method(self):
#         self.child1_method()
#         self.d = 90
#         return self.d  + self.a + self.c
    
# obj = Child2()
# print(obj.child2_method())


              
# class Parent():
#     a = 100

#     def parent_metho(self):
#         self.b = self.a
#         return self.b

# class Child1(Parent):
#     def __init__(self):
#         print("I am a constructor-1")

#     def child1(self):
#         self.c = self.a - 50
#         return self.b
    

# class Child2(Child1):
#     def __init__(self):
#         Child1. __init__(self)
#         print("I am a constructor-2")

#     def child2(self):
#         self.child1()
#         self.parent_method()
#         self.d = 10
#         return self.d + self.a + self.c
    
# obj = Child2()
# print(obj.child2())


# CONSTRUCTOR EXMAPLE==============

# class Parent():
#     def __init__(self):
#         self.a = 10
#         self.b = 100

# class Child(Parent):
#     def __init__(self):
#         Parent.__init__(self)   #you are manually calling parent class or you can use super().__init__()
#         # or  super().__init__() above
#         self.d = self.a + self.b
#         print("value of d", self.d)

# obj = Child()


# class Person():
#     name = "sameer"

#     def name_method(self):
#         print("Person name is", self.name)

# class Employee():
#     employee_id = 10

#     def employee_method(self):
#         print("employee id is", self.employee_id)

# class Manager(Person, Employee):
#     def manager_class(self):
#         print(f'{self.name} has employee id, {self.employee_id}')
        


# obj = Manager()
# print(obj.manager_class())



# POLYMORPHISM CONCEPT =====================================

