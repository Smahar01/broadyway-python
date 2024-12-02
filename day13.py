# Nov 6 2024, Wednesday
''' Function concept
A function is a block of code which only runds when it is called. 
You can pass data, known as parameters, into a function.
A function can return data as a result.
In Python a function is define using the "def" keyword.


'''
# def test():
#     print("this is function")
#     return "ok"

# a = test()
# print(a)

# def hello():
#     print(1)
#     print("hello")

# hello()
# hello()

# def hello():
#     print(2)
#     print("hello")
# for i in range(1,10):
#     hello()

# arguement/ parameter concept

# def addition():
#     x = 2 + 2
#     return x
# print(addition())

# 1. positional arugment or parameter

# def adds(a,b):
#     c = a+b
#     return c

# print(adds(1,2))
# print(adds(2,2))
# print(adds(5,5))

# def multiplication(a,b):
#     c = a*b
#     return c

# print(multiplication(2,2))
# print(multiplication(3,5))

# def my_function(fname):
#     print(fname + " maharjan")

# my_function("email")
# my_function("address")

# def my_function(fname, lname):
#     print(f'{fname} {lname}')

# my_function("sameer", "maharjan")
# my_function("sarad", "hamal")

# 2.default argument
# def default(a=10):
#     return a

# print(default())
# print(default(50))

# def default(x,a=10):
#     return a,x
# #print(default())   this will give an error, 1 missing required positional argument

# print(default(60))

# def math(pie=3.14):
#     print("value of pie is", pie)

# math()
# math(5)


# 3. keyword argument (kwargs) or **kwargs

# def test2(a,v,c):
#     print(a,v,c)

# test2(v=10, a=1, c=4)

# 4. arbitary positional arguments
# def arbitary_function(*a):     # this will give output in tuples
#     print("arbitary", a)

# arbitary_function(1)
# arbitary_function(1,2,4,5,5)


# def test(*broadway):
#     print(broadway)

# test(1,2,3,4,4,5,6)

# def test(*broadway):
#     sum = 0
#     for i in broadway:
#         sum =  sum + i
#     print(sum)

# test(1,2,3,4,4,5,6)

# 5. Arbitary keyword arguement

# def kw(**sameer):  # provide outputs in dictionary
#     print(sameer)

# kw(name="ram", test=1)

# def my_function(**test):
#     print(test)

# my_function(name="sameer", address="charlotte")

# def my_function(**arb_keyword):
#     print(arb_keyword)

# my_function(name="ram", grade=10)


# def my_function(*args, **kwargs):
#     print("this is positional args value", args)
#     print("this is kwargs value", kwargs)

# my_function(1,2,4)
# my_function(1,2,3,name="hello", 1,2)   # positional arg always comes first and then only keyword arg, after keyword arg, you cannot add positional arg.

# def multiplication(*args,**kwargs):
#     print("my name is", kwargs['name'])
#     data = set(args)
#     print(data)
#     for i in data:
#         for j in range(1,3):
#             print(f'{i} x {j} = {i*j}')
        

# multiplication(1,2, name="sameer")

