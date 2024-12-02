# # ============    october 28th 2024    =======
# # print a multiplication table

# n = int(input("enter a number: "))

# for i in range(1,11,1):
#     print(f'{n} x {i} = {n*i}')

# ==============================================================

# BREAK CONCEPT

# for i in range(1,5):
#     print(i)
#     if i == 3:
#         break
#     print(f'{i} is not equal to 3')

# print(f'{i} is equal to 3')

# ==================================================================

# for i in ["sameer", "ram", "hari"]:
#     print(i)
#     if i == "ram":
#         break
#     print(f'break not applied as {i} is not ram')

# print(f'{i} is equal to ram')

# ===============================================================================
# CONTINUE CONCEPT


# for i in ["ram", "sam", "hari"]:
#     print(i)
#     if i == "sam":
#         continue
#     print("Hello I am", i)

# for i in range(1,5):
#     print(i)
#     if i == 3:
#         continue
#     print("continue will escape")

# ====================================================================

# NESTED LOOP CONCEPT===============

# for i in range(1,6):
#     for j in range(2,10,2):
#         print(i,j)


# for first_name in ["ram","sameer","hari"]:
#     print(first_name)
#     for last_name in ["maharjan", "shrestha"]:
#         print(first_name,last_name)


# for first_name in ["ram", "sameer","hari"]:
#     print(first_name)
#     if first_name == "sameer":
#         for last_name in ["sharma", "shrestha"]:
#             print(first_name,last_name)

# for i in range(1,7):
#     if (i%2!=0):
#         continue       # here only 2, 4, 6 will have modulus 0, therefore, continue will escape other numbers
#     for j in range(1,7):
#         print(i,j)