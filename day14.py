# NOV 8TH 2024, FRIDAY
''' python data types
# tuples
it stores multiple data
it stores data in index
it is immutable (does not  change during runtime using append, extends, concatenate)
opens and closes in small bracket or parenthesis
can add data after type casting to list



# set
 use curly bracket
 data are unordered
 duplicate data cannot be printed
can add data after type casting to list

'''
# RECRUSION CONCEPT

# def sudan():
#     print("sudan")
#     if 1==1:
#         return
#     sudan()

# sudan()

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
    
print(factorial(5))




