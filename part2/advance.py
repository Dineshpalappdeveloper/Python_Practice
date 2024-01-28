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

def sum(a, b):
    return a+b, a*b


ot = sum(25, 35)
print(ot)
