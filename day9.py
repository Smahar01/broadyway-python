# # # identity operator
# # is 
# # is not

# membership operator
# in

# print(1 is not 2)
# print(1 is not 2)
# print(1!=2)
# print(1==1)

# a = "None"
# if a is None:
#     print("1")
# # 
# print(1 is 1)
# print(1==1)
# ========================================================================

# 22nd October, Friday

# LIST CONCEPT
# list is mutable:you can change the value during runtime
# list are ordered collection of data items, they store multiple items in a single variable, list items are seprated
# commas and enclosed within square brackets [], list are changeable meaning we can alter then after creation
# list and dict: mutable
# set and tuple : immutable

# a = [2,1,"hello",5,6, 5.3, 7]
# pint(a)
# print(type(a))
# print(a[2])


# data items are places in index starts with  positive index 0 at first and negative index -1 at last

# changing the item 
# a = [2,1,"hello",5,6, 5.3, 7]

# a[0] = 10
# print(a)

# negatie index starts from -1 at end
# a = [2,1,"hello",5,6, 5.3, 7]

# print(a[-1])

# length of list

# a = [2,1,"hello",5,6, 5.3, 7]
# print(len(a))  # lenght will count the value starting from 1, it doesn't count index.



# slice according to index number
# a = [2,1,"hello",5,6, 5.3, 7]
# print("slicing value",a[0:4])
# print("slicing value",a[:4])   # if you don't put any index in beginning, it takes as 0.
# print("slicing value",a[1:4])
# print("slicing value",a[1:]) # if you don't put any index after :, it takes up to the last value
# print("slicing value",a[:]) # gives all items from list


''' METHODS OF LIST
1. append
2. insert
3. extend
4. concatenate
'''
# add items in list

# 1. append: it always add an element/item  at the end of existing list
# b = ["cat","dog",1]
# print("before append")
# print(b)
# print("after append")
# b.append("this is test")
# print(b)

# c = []
# c.append("this is an empty list")
# c.append(1)
# print(c)

# Insert: the insert medthod add the element at the specified index position

# c = []
# c.append("this is an empty list")
# c.append(1)
# c. insert(0,"insert")
# c.insert(0,"hello")
# c.insert(25, "sameer")
# print(c)


# # concatenate: 
# b = [1,2,4,"b"]
# c = [2,6,"c"]
# print(c+b)

# extend
# b = [1,2,4,"b"]
# c = [2,6,"c"]

# c.extend(b)
# print(c)


# a = [2,1,"jelly,[1,2,3]]
# print(a)

# d = a[-1]
# print(type(d))
# print(d[-1])

# or

# print(a[-1][-1])
# ====================================================================================
# day 10.py October 24th 2024
# delete items or elements from exisiting list via index
'''
1. delete : delete items or elements from exisiting list via index

2. remove: delete items based on the value
3. pop: delete the last index item.
4. clear: delete all elements or items from the list

'''

# # 
# a = [1,3,4,2]
# print("before delete",a)
# del a[0]
# print("after delete",a)

# a = [1,2,4,5]
# a.remove(5)
# print(a)

# a = [2,5,4,5]
# a.remove(5)    # remove delete only the first elements and then it won't delete duplicate element
# print(a)


# a = [1,4,7,8]
# a.pop()
# print("pop",a)

# a = [1,3,4]
# a.clear()
# print("clear:",a)


#count concept

# a = [1,3,5,6,5]
# data = a.count(5)
# print("count:",data)

# index, sort, reverse

# a = [1,4,6,4,2,7,0]
# a.sort()
# print(a)

# ============================================

# empty_list = []
# user_1 = input("Enter first name:",)
# user_2 = input("Enter second name:",)
# print(user_1)
# print(user_2)
# empty_list.append(user_1)
# empty_list.append(user_2)

# print(empty_list)
# empty_list.sort()
# print(empty_list)

# =====================================================

#above can be done like below:

data = []
a = input("enter first name:",)
b = input("enter second name:",)
data.append(a)
data.append(b)
print("before sort", data)
data.sort()
print("after sort", data)
