# data type
# a = 10 ===>integer, it is a whole number which can be negative or positive
# a = 4.3 ===> float, it is a decimal number
# a = "hello" ====> string
# a = 2+3j ===>complex

a = '1'
print("1" + "1")
print("1"*3)

a = "10"
b = "2"

print("before type casting:", a + b )

print("after type casting:", int(a) + int(b))

a = "5"
print(isinstance(a, int))

a = "5"
print(isinstance(a, str))

test = "hello"
test2 = "from broadway"
test3 = 2222

# print(str(test) + " " + str(test2) + " "  + str(test3))
print(test, test2, test3)

# formatted string
print(f'{test} {test2} {test3}')