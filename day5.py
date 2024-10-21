'''
if (1==2):
    print("this is 1==1")
else:
    print("this is a false condition")

    day = "SUNday"
    day = day.lower()
    if (day=="sunday"):
        print("Its a sunny day")

day = "Tuesday"
day = day.lower()

if (day == "sunday"):
    print("sunny day")

elif (day == "monday"):
    print("workday")
elif (day == "tuesday"):
    print("Today is tuesday")

else:
    print("boring day")


# singeline if condition
# nested if condition

a = input("Enter a number: ")
print("enter word is" , a)
print(type(a))


day = input("Enter a day: ")
day = day.lower()

if (day == "sunday"):
    print("sunnday day")

elif (day == "monday"):
    print("workday")
elif (day == "tuesday"):
    print("today is tuesday")
else:
    print("boring day")


day = input("Enter today's day: ")
day = day.lower()

if (day=="monday"):
    print("It's a work day")

elif(day=="tuesday"):
    print("It's a meeting day")
else:
    print("It's a relax day")

'''
'''


if (1==1):
    print("this is true condition")
else:
    print("this is false condition")

n = 10
if (n%2==0):
    print("this is even number")
else:
    print("this is odd number")

'''
# per = input("enter your per: ")

# if (per>=80 and per<=100):
#     print("you got distinction")

# elif(per<=80 and per>=60):
#     print("you got first division")

# else:
#     print("you got second division")



# GPA = 3.00
# if (GPA>=3.25 and GPA<=4.0):
#     print ("this is distinction")
# elif (GPA>=3.25 and GPA<=4.0):
#     print ("this is pass")
# else:
#     print ("this is fail")

gpa=3.5
if (gpa>3.6 and gpa<=4):
 print("A+")
elif (gpa>3.2 and gpa<=3.6):
 print("A")
else:
 print("B+")