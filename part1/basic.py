# print("Welcome dinesh")
# python is a case sensetive language
# welcoem Message single line comment
''' 
hi 
i  
Am 
dinesh'''  # miltiline unoffisial comment
#  variable
# in case of boolean variable value start with capital letter (True or False)
# popup = True
# name_ad = "dkp"
# age = 10
# height = 2.5

# String

# name = "dinesh kumar pal"

# print(len(name))  # return length of variable ot-16
# print(name[3])  # return third index value ot-e
# print(name[-2])  # return second value from right side ot-a
# spliceing (cuting in string)
# print(name[0:5])  # start from 2 index and stop to 5 string count ot - dines
# print(name[0:])  # start from 2 index and not  stop ot- dinesh kumar pal
# start from 0 index and not  stop 5 count ot- dines
# print(name[:5])

# operators

# a = 10
# b = 10
# c = "dkp"
# print(a+b)
# print(5**2)  # 5*5
# print(5**4)  # 5*5*5*5
# floor division (return division value in interger ) it remove  decimal digits
# print(11//4)


# logical operator
# and or not (in javascript && || ! )
# a = 10
# b = 20
# print(a >= 10 and b != 20)
# print(a >= 10 or b != 20)
# print(not b != 20)

# membership operators  ##(in javascript arr.include(50))

# name = "Dinesh"

# print('d' in name)  # False because its a case sensetive language
# print('e' in name)  # True
# arr = [25, 5266, 636, 52]
# print(50 not in arr)  # True    ##(in javascript arr.include(50))

# identity operator
# is (==) is not (!=)

# a = 10
# b = 10
# print(a is b, b == a) # True True
# print(a is not b, b != a) # False False

# Bitwise operator

# & if both side true then return True (and)
# | if atleast one true then return True (or)
# ^ if both side same then return Flase else True (xor)

# x = 10
# y = 8

# print(bin(x))  # return binary value 1010
# print(bin(y))  # return binary value 1000

# print(bin(x & y), x & y)  # return 1000 (means 8)
# print(bin(x | y), x | y)  # return 1010 (means 10)
# print(bin(x ^ y), x ^ y)  # return 0010 (means 2)

# DataType
# a = 10  # number
# b=2.5 float
# c=4+5j complex

# print(type(a)) # it return the datatype of a variable

# d = '''
# hello Dinesh
# how are you today
# i can  ...
# '''
# print(d, type(d))  # it work as a pre tag it means preformated text

# list (array)

# l = [25, "dkp", "ak"]
# l[2] = "si"
# print(l, type(l)) #  [25, 'dkp', 'si'] <class 'list'>

# tuple (can not be change and atleast two value in bracket )

# t = (2, 525, "dkp", "si")
# print(t, type(t))  # (2, 525, 'dkp', 'si') <class 'tuple'>


# Dictionary

# Dictionary data type (it accept value in key and pair and we can acces useing its key and we can also update it)

# d = {
#     "name": "dinesh",
#     "sName": "pal"
# }
# print(d)  # "{'name': 'dinesh', 'sName': 'pal'}
# d["name"] = "Ganesh"
# print(d, type(d))  # {'name': 'Ganesh', 'sName': 'pal'} <class 'dict'>

# sets (set can not duplicate and not changeable ) it remove duplicate value

# s = {5, 5, 10, 26, 50, 26}
# print(s, type(s))  # {10, 26, 50, 5} <class 'set'>

# get user input and type casting
#  input  (it take input from user on runtime )
# int() it take only integer value
# float() it take only float value
# Eval() it handle all type value (integer,float,bianary)
# c = eval(input("Enetr First Value:- "))
# a = eval(input("Enter Your First Name:-"))
# d =eval (input("Enter Second Value:-"))
# f = c+d
# print(e, type(e))
# print(f, type(f))


# conditional statement

# if

# a = 20
# if a % 2 == 0:
#     print(a, "Even Number")


# if and else

# a = 20
# if a % 2 == 0:
#     print(a, "Even Number")
# else:
#     print(a, "Odd Number")


# if and elif elif else

# per = 50
# if per >= 60:
#     print("First Div")
# elif per >= 45:
#     print("Second Div")
# elif per >= 30:
#     print("Third Div")
# else:
#     print("Fail")

# basic calculator use if elif and else

# num1 = 505
# num2 = 320
# opt = "5"

# if opt == "+":
#     print(num1+num2)
# elif opt == "-":
#     print(num1-num2)
# elif opt == "/":
#     print(num1/num2)
# elif opt == "*":
#     print(num1*num2)
# else:
#     print("invalid opt")

# for loop

# range

# range(5) # output - 0,1,2,3,4
# it have some defalut value
# default start value 0
# default less than 5 (in this case  range(5) )
# default increment 1


range(1, 6)  # output- 1,2,3,4,5
# first start form
#  less than 6
# increment by 1

range(1, 6, 2)  # output- 1,3,5
# first start form
# second less than
# third increment

# table of 3 useing for loop with range

# x = 3
# for n in range(1, 11, 1):
#     print(x, "*", n, "=", n*x)

# for loop with reverse useing range

# for n in range(10, 0, -1):
#     print(n)

# while loop

# i = 1
# while i <= 10:
#     print(i, "Welcome Dkp")
#     i = i+1
# print(i) #output:- 11
# reversed

# i = 10
# while i >= 1:
#     print(i, "Welcome Dkp")
#     i = i-1
# print(i) # output-0
