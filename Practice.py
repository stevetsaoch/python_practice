# practice for loop

# for item in [1,2,3,4,5]:
#     print(item)

# user = {
#     'name' :'Steve',
#     'age' : 10,
#     'Height' : 100
# }

# for key, value in user.items():
#     print(key, value)

# for item in user.values():
#     print(item)

# counter
# sumup = [1,2,3,4,5,6,7,8,9,10]
# counter = 0
# for num in sumup:
#     counter = counter + num

# print(counter)

# range
# for item in range(1,101,1):
#     print(item)

# enumerate
# for i, char in enumerate(list(range(10))):
#   if char == 5:
#       print(i)

# #while
# i= 0
# while i<51:
#     i = i+1
#     print(i)

# picturing a image with pixel
# picture = [
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
# ]

# i = 0
# while i <= 3:
#     for row in picture:
#         for col in row:
#             if (col == 0):
#                 print(' ',end ='')
#             else:
#                 print('*',end ='')
#         print('',)
#     i += 1

# #Find duplicate
# test_list = ['a','b','c','b','d','m','n','n']
# result_list=[]

# for item in test_list:
#     if test_list.count(item) > 1:
#         # if item not in result_list:
#         if result_list.count(item) == 0:
#             result_list.append(item)
#             print(item)

# # print(result_list)
# def sum(n1=1,n2=2):
#     def sum2(n1,n2):
#         return n1 + n2
#     return sum2

# print(sum()(1,2))

# #Tesla function
# def checkage(age):
#     if int(age) < 18:
#         print("sorry, you are too old to drive this car. Powering off.")
#     elif int(age) > 18:
#         print("Powering on. Enjoy your ride.")
#     elif int(age) == 18:
#         print("Congratlation on your first year of driving.")

# checkage(18)

# def is_primenumber(num):
#     i = 2
#     if num == 2:
#         print(True)
#     else:
#         while i < num:
#             if num % i == 0 :
#                 print(False)
#                 break
#             else:
#                 if i == num - 1:
#                     print(True)
#             i += 1


# is_primenumber(2447)

# out put a highest even from a list or a number series you input
# testlist = [2,3,5,12000,19,33000,48,17,10,1000,15,12]
# def heighest_even(*inputlist):
#     temp_list = list(inputlist)
#     temp_value = 0
#     temp_highest_even = 2
#     for item in temp_list:
#         while item % 2 == 0:
#             temp_value = item
#             if temp_value <= temp_highest_even:
#                 temp_highest_even = temp_highest_even
#                 break
#             else:
#                 temp_highest_even = item
#                 break
#     return temp_highest_even

# print(heighest_even(10000,20,1,3,5,100000,100))


# class Cat:
#     fat = 100

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         return self.name

# class User():
#     def __init__(self, username='steve', password='abc'):
#         self.username = username
#         self.password = password

#     def username_and_password(self):
#         return f'you username is {self.username} and you password is {self.password}'


# class Worrior(User):
#     def __init__(self, charater_name, charater_hight, charater_power):
#         super().__init__()
#         self.charater_name = charater_name
#         self.charater_hight = charater_hight
#         self.charater_power = charater_power

#     def slower(self):
#         return "123"


# class Mach():
#     def __init__(self, charater_name, charater_hight, charater_power):
#         self.charater_name = charater_name
#         self.charater_hight = charater_hight
#         self.charater_power = charater_power

#     def faster(self):
#         return "456"


# class DoubleChar(Worrior, Mach, object):
#     def __init__(self, charater_name, charater_power, charater_hight):
#         super().__init__(charater_name, charater_hight, charater_power)
#         self.charater_name = charater_name
#         self.charater_power = charater_power

#     def test(self):
#         return super().faster()


# dou1 = DoubleChar("test1", 100, 1000)
# print(dou1.test())
# print(dou1.username)
# # wor1 = Worrior("test", 100, 1000)
# # print(wor1.username)

# from functools import reduce
# my_pets = ['sisi', 'bibi', 'titi', 'carla']


# def Cap(item):
#     return item.capitalize()


# print(list(map(Cap, my_pets)))

# scores = [73, 20, 65, 19, 76, 100, 88]


# def larger50(item1):
#     return item1 > 50


# my_numbers = [5, 4, 3, 2, 1]


# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item


# # print([1,3]+[2,4])

# my_dict = {num: num/2 for num in [1, 2, 3]}

# print(my_dict)

# some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']

# duplicate = list(set([dup for dup in some_list if some_list.count(
#     dup) > 1]))

# print(duplicate)

# valuedict = {
#     'I': 1,
#     'IV': 4,
#     'IX': 9,
#     'V': 5,
#     'X': 10,
#     'XL': 40,
#     'XC': 90,
#     'L': 50,
#     'C': 100,
#     'CD': 400,
#     'CM': 900,
#     'D': 500,
#     'M': 1000
# }

# i = 0
# output = 0


# def romantonub(s):
#     i = 0
#     output = 0
#     while i < len(s):
#         print(i)
#         if s[i:i+2] not in valuedict.keys() and valuedict[s[i]] <= valuedict[s[i+1]]:
#             output += valuedict[s[i]]
#             i += 1
#         else:
#             output += valuedict[s[i:i+2]]
#             i += 2

#     return output


# testroman = 'III'
# print(romantonub(testroman))

# Create an @authenticated decorator that only
# allows the function to run is user1 has 'valid' set to True:

# user1 = {
#     'name': 'Sorna',
#     'valid': False
# }


# def authenticated(fn):
#     def wrap_function(*args, **kwargs):
#         if args[0]['valid'] == True:
#             fn(kwargs)
#         else:
#             return 'not valid'

#     return wrap_function


# @authenticated
# def message_friends(user):
#     print('message has been sent')


# print(message_friends(user1))

# def fib(number):
#     a = 0
#     b = 1
#     for i in range(number):
#         yield a
#         temp = a
#         a = b
#         b = temp + b


# for x in fib(10):
#     print(x, end=',')

# a = fib(5)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

with open('sad.txt', mode='w') as myfile:
    text = myfile.write(":)")
    print(text)
