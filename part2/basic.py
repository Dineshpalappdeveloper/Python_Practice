
# String indexing

# s = "dinesh kumar pal"

# print(s[0])  # output:- d (left to right indexing start from 0 )
# print(s[-2])  # output:- a (right to left  indexing start from -1)

# sliceing in string
# print(s[0:10])  # start from 0 index and end to 10 index
# print(s[0::3])  # start from 0 index and end last with increment 3
# print(s[-1::-1])  # reverse
# print(s[-1::-2])  # reverse with 2 increment

# string iteration

# w = "welcome Bhai"

# t = len(w)
# for n in range(t):
#     print(w[n])
# for a in w:
#     print(a)

# reverse
# for n in range(t-1, -1, -1):
#     print(w[n])


# python string function


# lower() # for lower case
# captilize()  # for captilizetion
# upper()  #  for  uppercase
# title() # har work ka pahla letter capital

# w = "welocme to bihar"
# a = w.title() # Welocme To Bihar
# b = w.upper() # WELOCME TO BIHAR
# c = w.lower() # Welocme to bihar
# d = w.capitalize() # Welocme to bihar
# print(a)
# print(b)
# print(c)
# print(d)

# w = "welcome"
# print(w.find("e"))  # it return the index of first march e
# print(w.find("e", 3))  # it return the index of  e but start finding from 3 index
# print(w.index("l"))  # it return index same as find

# if find function dont mathch any value then return -10 but index function give an value error

# output:- True   (if in this string all value is alphabet or not return True of False)
# print(w.isalpha())
# output:- Flase   (if in this string all value is digit or not return True of False)

# print(w.isdigit())
# output:- True   (if in this string all value is (alphabet or  digit both case return true  ) or not return True of False)
# print(w.isalnum())

# chr() and ord()

# print(chr(65))  # it accept charater and return ascci value integer output-A
# print(ord("A"))  # it accept ascci value integer and return character outPut-65

# format( ) in string

# w = "Your Fname {} and LastName {} ".format("Dinesh", "pal")
# print(w)
# w = "Your Fname {1} and LastName {0} ".format("Dinesh", "pal")
# print(w)

# w = "Your Fname {name} and LastName {tital} ".format(
#     name="Dinesh", tital="pal")
# print(w)

# list in python

# l = [2, 5, 7, [8, 9, 3], "hello"]


# print(l[0:2])  # slice from 0 to  2 ot [2, 5]
# l2 = [5, 2, 4, 6, 9, 8]
# print(l2[0::2])  # [5, 4, 9]
# print(l2[-1::-1])  # [8, 9, 6, 4, 2, 5]

# list iteration

# l2 = [5, 2, 4, 6, 9, 8]
# t = len(l2)
# for n in range(t):
#     print(l2[n])
# second method (easy method)
# for n in l2:
#     print(n)

# for n in range(t-1, -1, -1):
#     print(l2[n])

# my logic

# for n in range(-1, -t-1, -1):
#     print(l2[n])

# List Comprehension

# l = []

# for n in range(1, 109):
#     l.append("Um Namah Shivaye")

# print(l)

# l = [n for n in range(1, 109)]
# print(l)

# finter in list

# l = [n for n in range(1, 216) if n % 2 == 0]
# print(l)

# change string into list

# w = "welcome"
# l = [n for n in w]
# print(l)


# Function for Delete Element from List

# del
# pop()
# remove()
# clear()

# l = [25, 36, 69, 665, 655]

# del l[2] # for deleteing useing index
# print(l) # [25, 36, 665, 655]

# print(l.pop(3))  # for deleteing useing index and also return deleteing value
# print(l)  # for deleteing useing index [25, 36, 69, 655]

# l.remove(69)  # for deleteing useing value
# print(l)  # [25, 36, 665, 655]

# l.clear()  # delete all elements
# print(l)  # []

# l = [25, 36, 69, 665, 655]

# # update list
# l[2] = 108
# print(l)  # [25, 36, 108, 665, 655]

# insert()
# append()
# extends()

# first index and second value and 0 index value move to 1 index and so on
# l.insert(0, 108)
# print(l) # [108, 25, 36, 69, 665, 655]

# l.append(101)  # it last index of an array
# print(l)  # [25, 36, 69, 665, 655, 101]

# p = [25, 50, 75, 100]
# l.append(p)  # it add with datatype not value
# print(l)  # [25, 36, 69, 665, 655, [25, 50, 75, 100]]

# l.extend(p)  # it work on value
# print(l)  # [25, 36, 69, 665, 655, 25, 50, 75, 100]

# function in list

# count() # how many time element present in a list
# max() # highest value in list(integer) if charecter then z in higher
# min() # minimum value in list(integer) if charecter then z in higher
# sort() # shorting in acs order
# reverse() # reverse the list
# index() # for finding the index useing list element value
l = [25, 36, 5, 69, 665, 655, 25, 50, 75, 100]

# print(l.count(50))  # 2
# print(max(l)) #665
# print(min(l)) # 5

# l.sort()
# print(l) #[5, 25, 25, 36, 50, 69, 75, 100, 655, 665]

# l.reverse()
# print(l)  # [100, 75, 50, 25, 655, 665, 69, 5, 36, 25]

# sort with reverse

# l.sort()
# l.reverse()
# print(l)  # [665, 655, 100, 75, 69, 50, 36, 25, 25, 5]

# print(l.index(75)) # 8

# how to iterate dubble list

# zip( ) in python

# l = [10, 20, 30, 40]
# m = [1, 2, 3, 4]
# n = [11, 21, 31, 41]
# for a, b in zip(l, m):
#     print(a, b)

# t = len(l)

# for h in range(t):
#     print(l[h], m[h], n[h])

# convert string to list

# s = "welcome- to mypustak"
# l = s.split("-") #['welcome', ' to mypustak']
# l = s.split()  # ['welcomme', 'to', 'mypustak']

# p = []
# for n in s:
#     p.append(n)


# print(p) # ['w', 'e', 'l', 'c', 'o', 'm', 'e', '-', ' ', 't', 'o', ' ', 'm', 'y', 'p', 'u', 's', 't', 'a', 'k']

# model for  advance  js

def sum(a, b):
    return a+b


def mul(a, b):
    return a*b
