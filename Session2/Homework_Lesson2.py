# # Bai_1
# for x in range(1,6):
#     print ("*"*x)
# for x in (6,7,8):
#     print ("*"*(10-x))


# # Bai_2
# i = 0
# j = 0
# for x in range (1,10):
#     if not x % 2:
#         i = i+1
#     else:
#         j = j+1
# print ("number of even number",j,"\nnumber of odd number",i)


# # Bai_3
# for x in range (1500,2701):
#     if not x % 35:
#         print (x, end=" ")


# # Bai_4
# import random
# a = random.randint(1,10)
# x = int(input("x = "))
# while x:
#     if not x == a:
#         x = int(input("x = "))
#     else:
#         break
# print ("well guessed!")


# # Bai_6
# i = 0
# print ("0", end=" ")
# for i in range (0,6):
#     i = i+1
#     if not i % 3:
#         continue
#     else:
#         print (i, end=" ")


# # Bai_7
# print ("0", end = " ")
# a, b = 0, 1
# while b < 50:
#     print (b, end=" ")
#     a,b = b, a+b


# # Bai_8
# print ("fizzbuzz")
# for x in range (1,51):
#     if not x % 3 and x % 5:
#         print ("fizz")
#     elif not x % 5 and x % 3:
#         print("buzz")
#     elif not x % 15:
#         print ("fizzbuzz")
#     else:
#         print (x)


# # # Bai_9
# # i = int(input("Input number of rows: "))
# # j = int(input("Input number of columns: "))
# # array = [[0 for col in range(j)] for row in range(i)]
# #
# # for row in range(i):
# #     for col in range(j):
# #         array[row][col]= row*col
#
# print(array)


# # Bai_10
# y = [x for x in input("nhap so nhi phan ").split(",")]
# for i in y:
#     p = int(i,2)
#     if not p % 5:
#         print (i)


# # Bai_11
# a = input("input the string ")
# l = d = 0
# for i in a:
#     if i.isdigit(): d = d+1
#     elif i.isalpha(): l = l+1
# print ("letters ",l,"\ndigits ",d)


# # Bai_12
# a = input("password ")
# l = u = n = c = 0
# for i in a:
#     if i.isdigit(): n = n+1
#     elif i.islower(): l = l+1
#     elif i.isupper(): u = u+1
#     elif not (i.isalnum() or i.isspace()): c = c+1
# if l+u+n+c <6  or l+u+n+c >16 or n==0 or l==0 or u==0 or c==0:
#     print("invalid password")
# else:
#     print("valid password ")




# # Bai_13
# for i in range (1,8):
#     if i == 1:
#         print (" *** ")
#     elif i == 4:
#         print("*****")
#     else:
#         print("*   *")



# # Bai_14
# i = 0
# for x in range (1,10):
#     i = i + 10**(x-1)
#     print(i*x)
