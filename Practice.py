##practice for loop

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

##counter
# sumup = [1,2,3,4,5,6,7,8,9,10]
# counter = 0
# for num in sumup:
#     counter = counter + num

# print(counter)

##range
# for item in range(1,101,1):
#     print(item)

##enumerate
# for i, char in enumerate(list(range(10))):
#   if char == 5:
#       print(i)

# #while
# i= 0
# while i<51:
#     i = i+1
#     print(i)

#picturing a image with pixel
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

##out put a highest even from a list or a number series you input
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

total = 0 

def count(total):
    total += 1
    return total

print(count(3))

x = 'hello'
y = "Hello"[0]
print(y)