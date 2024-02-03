#  Stack and Queue

# stack is a lieaner data structure
# work on lifo(last in first out ) or Filo (first in last out)

# stack operation
# 1.push : append a element in list
# 2.pop : remove last element from list
# 3. pick : display last element
# 4. display :dispaly all list

# queue
# queue in lienear data structure
# it work on FIFO first in first out

# Queue operation
# 1. Enqueue : add a item in queue
# 2.Dequeue : remove an first iten from queue
# 3.front : dispal first item from queue
# 4.Rear :dispaly last item from queue

# Dictionary (key and value pair)

# d = {
#     "name": "Dinesh",
#     "roll": 25
# }

# print(d["roll"]) # 25
# for n in d:
#     print(d[n])


# function in   Dictionary

# get() geting value useing key
# keys()
# values()
# item()

# d = {
#     "name": "Dinesh kumar",
#     "roll": 25
# }

# print(d.get("name"))  # Dinesh kumar
# for n in d.keys():
#     print(n)

# for n in d.values():
#     print(n)

# for n, a in d.items():
#     print(n, a)

# here two method for deleteing item
# del and pop

# del d["roll"]
# print(d)  # {'name': 'Dinesh kumar'}

# print(d.pop("roll")) # 25
# print(d)  # {'name': 'Dinesh kumar'}

# d = dict(id=25, money=420)  # use for creating the new Dictionary
# print(d)

# d.update({"roll": 108, "fname": "Alakh"})  # for updateing the value
# print(d)  # {'name': 'Dinesh kumar', 'roll': 108, 'fname': 'Alakh'}

# d.clear()
# print(d) # {}

# how insert an dict
# d["Nickname"] = "Ganesh"
# print(d)

# nested dict

# course = {
#     "php": {
#         "batch": "march",
#         "fees": 1200,
#         "duration": {
#             "first": "1 years",
#             "second": "2 years"
#         }
#     },
#     "java": {
#         "batch": "march",
#         "fees": 120,
#         "duration": "5 month"
#     },
#     "c": {
#         "batch": "march",
#         "fees": 100,
#         "duration": "60 month"
#     }
# }
# course["php"]["duration"]["first"] = "10 years" # updateing the value
# print(course)

# for a, b in course.items():
#     print(a, b)


# tuple

# tuple (in tuple must have more than one value)
# t = (5, 4)

# min()
# max()
# count()
# sun()
# index()

# t = (9, 8, 7, 5, 6, 4, 2, 3)
# print(t, type(t))  # (9, 8, 7, 5, 6, 4, 2, 3) <class 'tuple'>
# r = len(t)

# for n in range(r):
#     print(t[n])  # 9, 8, 7, 5, 6, 4, 2, 3
# print(min(t))  # 2
# print(max(t))  # 9
# print(t.count(9))  # 1
# print(t.index(3)) # 7
# print(sum(t))  # 44
# print(sum(t, 108))  # initial value (previous value) ot-152


# set in python

# add() s.add(50)
# set() l.set()
# pop() it delete random element s.pop()
# remove() s.remove(value)
# clean() s.clear()
# discard() s.discard()
# update() s.upadte(l)

# s = {2.4, 6, 8}  # set are unique and dont have index

# how to change list into set
# l = [25, 25, 36, 96, 36, 36, 8]
# print(set(l))  # {96, 25, 36, 8}

# l = [9, 8, 5]
# s.update(l)  # {2.4, 5, 6, 8, 9}
# print(s)

# user define function

# def sum(a, b):
#     print(a+b)

# sum(25, 25) # 50

# with return

# def sum(a, b):
#     return a+b, a*b


# ot = sum(25, 35)
# print(ot)

# with multiple return

# model define in basic js

# method first

# import basic

# print(basic.sum(52, 48))
# print(basic.mul(25, 25))

# method 2

# from basic import sum, mul

# print(sum(253, 10))
# print(mul(25, 225))

# method 3 sabse best

# from basic import *

# print(sum(253, 1))
# print(mul(25, 225))

# useing aliyas (it means aapne maan se kuch bhi name de sakte hai)

# import basic as m

# print(m.sum(253, 1))
# print(m.mul(25, 225))

#  functions in math

# import math
# x = 12.1

# print(math.ceil(x)) # 13 it remove decimal by increasing the value but need to import math

# print(math.fabs(-15)) #  ot-15 (it always return positive value according to input)

# print(math.factorial(4))  # ot-24  return factorial of given number

# print(math.floor(10.6))
# ot-10 its use to remove the decimal value by decreasing the original value

# l = [25, 25, 50, 25]

# print(math.fsum(l)) # 125.0 it final sum of array(list) and tupple

# print(math.sqrt(25))  # return squreroot value og given integer in decimal

# import random

# it return random number by includeing start and end value(0,10,5,6)
# print(random.randint(1, 10))

# it return random number by includeing start value only and not return end value(0,10,5,6)
# print(random.randrange(1, 10))

# l = [25, 36, 56, 699]
# print(random.choice(l)) # it any from given list

# print(random.random()) # it return always return decimal value between 0 to 1

# random.shuffle(l)
# print(l)  # ot-[36, 699, 56, 25] it use to change the index of list

# print(random.uniform(5, 10))  # ot- 5.381470568096308 it return decimal value between given number


# datetime fuctions
# import datetime

# d = datetime.datetime.now()

# print(d)  # return current date and time ot-2024-01-30 08:11:50.783009
# print(d.strftime("%Y"))  # 2024 return current year and many value search on google if you wants

# d = datetime.datetime(2003, 2, 20)  # 2003-02-20 00:00:00
# print(d)

# pickle in python

# import json

# d = {
#     "name": "dinesh",
#     "home": "gaya",
#     "dist": "gaya",
#     "state": "bihar"
# }
# f = json.dumps(d)
# print(f, type(f))


# import json
# d = '{"name":"dinesh","city":"kolkata"}'
# s = json.loads(d)
# print(s, type(s))

# how to read  other file data

# import json
# file = open("post.json", "r")
# x = file.read()
# fileData = json.loads(x)
# print(fileData) # unable to open json file

# oops object oriented programming language

# class DemoClass:
#     a = 10

#     def sanvalue(self):
#         print(101+7)


# demoobject = DemoClass()
# print(demoobject.a)  # ot-10
# demoobject.sanvalue()  # ot-108

# method and constructor in oop

# class DemoClass:
#     a = 108

#     def sum(self):
#         b = self.a*self.a
#         print(b) # ot-11664


# obj = DemoClass()
# obj.sum()

# with parameter

# class DemoClass:
#     a = 108

#     def sum(self, d, e):
#         b = self.a*self.a
#         print(b*d*e)  # ot-136048896


# obj = DemoClass()
# obj.sum(108, 108)

# constructer (define with __init__ key it is predefine and it aotomically called)

# class DemoClass:
#     a = 108

#     def sum(self, d, e):
#         b = self.a*self.a
#         print(b*d*e)

#     def __init__(self):
#         print("welcome Dinesh")


# obj = DemoClass()
# obj.sum(108, 108)
# ot- welcome Dinesh
# 136048896

# inheritance in python
# child class can use parent class variable this is called inheritance

# there are three main inheritance
# 1. single inheritance
# 2.multilababel inheritance
# 3.multiple inheritance

# single inheritance

# class A:
#     def displayA(self):
#         print("A.Welcome Dinesh")


# class B(A):  # here class B is inherited the class A (it means b is able to use the class a variables)
#     def displayB(self):
#         print("B.Welcome Ganesh jee")


# obj = B()
# obj.displayA()
# obj.displayB()

# multilable inheritance

# class A:
#     def displayA(self):
#         print("A.Welcome Dinesh")


# class B(A):  # here class B is inherited the class A (it means b is able to use the class a variables)
#     def displayB(self):
#         print("B.Welcome Ganesh jee")


# class C(B): # here class C is inherited the class A and B (it means C is able to use the class a nad b variables)
#     def displayC(self):
#         print("C.Welcome to Donocare.com")


# obj = C()
# obj.displayA()
# obj.displayB()
# obj.displayC()

# multiple inheritance

# class A:
#     def displayA(self):
#         print("A.Welcome Dinesh")


# class B():
#     def displayB(self):
#         print("B.Welcome Ganesh jee")


# class C(A, B):  # here class C is inherited the class A and B (it means C is able to use the class a and b variables)
#     def displayC(self):
#         print("C.Welcome to Donocare.com")


# obj = C()
# obj.displayA()
# obj.displayB()
# obj.displayC()

# Encapsulation :- encapsulation is use for makeing private variable and functin(you can within the function not outside )

# geter and seter in Encapsulation

# class Student:
#     def __init__(self):
#         self.__name = ""

#     def getname(self):
#         return self.__name

#     def setname(self, name):
#         self.__name = name


# obj = Student()
# obj.setname("Donocare.com")
# name = obj.getname()
# print(name) # Donocare

# class Student:
#     __name = "Donocare"

#     def __init__(self):
#         print(self.__name)

#     def __userInfo(self):
#         print("Welcome to Donocare")


# obj = Student()

# ploymorphism

# it same function name but different signature

# l = [21, 25, 36, 85]
# print(len(l))
# s = "welcome Dinesh"
# print(len(s))
# function name len() same but first time returnign the array length and second time returning the word length

# class Do:
#     def Dispaly(self, name=""):
#         print("welcome to Donocare", name)


# obj = Do()
# obj.Dispaly()  # welcome to Donocare
# # example of overloading
# obj.Dispaly("Dinesh")  # welcome to Donocare Dinesh


# example of overridding
# class Du:
#     def DisplayInfo(self):
#         print("Welcome to Goa")


# class IIP(Du):
#     def DisplayInfo(self):
#         # super function is used to call name function those are define in parent
#         super().DisplayInfo()
#         print("welcome to IIp")  # example of overridding


# obj = IIP()
# obj.DisplayInfo()

# exmple of overloading

# class Area:
#     def find_area(self, x=None, y=None):
#         if x != None and y != None:
#             print(x*y)
#         elif x != None:
#             print(x*x)
#         else:
#             print("nothing ")


# obj = Area()
# obj.find_area()  # nothing
# obj.find_area(10, 20)  # nothing
# obj.find_area(50)  # nothing

# overriding

# class A:
#     def showData(self):
#         print("A function called")


# class B(A):
#     def showData(self):
#         print("B function called")


# obj = B()
# obj.showData()

# A Bike Rental System

# error handleing

# 1.syntax error
# 2. logical error

# 1.syntax error

# a=10
# b=20
# if a==b
#     print("true") # SyntaxError: expected ':'
# else
#     print("false")

# 2. logical error

a = 10
b = 0
c = a/b
l = [54, 36, 58]
print(l[4])
print(c)
