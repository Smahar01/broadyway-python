# october 28th 2024, Monday
# october 29th 2024, Tuesday

# system = 8 # suppose this is system generated number
# while True:
#     user = int(input("Enter user's number: "))

#     if system == user:
#         print("Number matched")
#         break
#     print("Guessed number doesn't match")

# =========================================================================

# import random
# system = random.randint(1,10)
# print(system)
# count = 0

# while True:
#     user = int(input("Enter user's number: "))
#     count = count + 1
#     if system == user:
#         print("number matched")
#         print(f'your guess count is {count} ')

#         break
#     print("number didn't match")

# ====================================================================================


# import random
# system = random.randint(1,10)
# print(system)
# count = 0
# user_guess_limit = 2

# while True:
#     user = int(input("enter user's number: "))
#     count = count + 1
#     if system == user:
#         print(f'user guessed number matched in {count} times')
#         break
#     if count == user_guess_limit:
#         print("Guess limit exceed, the system generated number is", system)
#         break

# =======================================================================================

# import random
# system = random.randint(1,10)
# print(system)

# n = "yes"
# count = 0
# user_guess_limit = 3
# while n == "yes":
#     n = int(input("enter a number:"))
#     count = count + 1

#     if system == n:
#         print("guess number match")
#         print(f'(you have guess in {count}th times)')
#         break
#     if count == user_guess_limit:
#         print(f'(your guess limit execeed, system generated number is {system})')
#         break
#     print("guess number not found")

#     n = input("do you wish to continue guessing number?").lower()
#     if n!="yes":
#         print(f'(you give up, system generated number is {system})')

# ===================================================================================================

# scissor/paper/rock game

import random
system = random.randint(1,3)
print(system)

# scissor = 1
# paper = 2
# rock = 3

while True:
    user_guess = input("user guess: ")

    if system == user_guess:
        print(f'(both are same)')
        break

    if user_guess!=system:
        print(f'(different guess)')
        break




