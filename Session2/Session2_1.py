# # Enter year of birth
#
# yob = input("year of birth")
# age = 2018 - int (yob)
#
# if age < 14:
#     print ("baby")
# elif age < 18:
#     print ("teenager")
# else:
#     print ("adult")


# import math
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))
#
# if a==0:
#     print ("khong phai phuong trinh bac 2")
# else:
#     delta = b*b - 4*a*c
#     if delta < 0:
#         print ("vo nghiem")
#     if delta == 0:
#         temp = math.sqrt(delta)
#         x1 = -b/(2*a)
#         print("pt co nghiem kep x1 = x2 =", x1)
#
#     else:
#         x1 = (-b+math.sqrt(delta))/(2*a)
#         x2 = (-b-math.sqrt(delta)/(2*a)
#         print ("pt co 2 nghiem x1 = ",x1," x2 = ", x2)



# khai bao array

# a = [5,2,3,4]
# sum = 0
# for i in range(len(a)):
#     sum = sum + a[i]
# print('sum of a: ', sum)

# import random
# # tao mang a
# a = []
# for i in range (100):
#     a.append(random.randint(1,20))
# # hien thi
# for i in range (100):
#     print (a[i], end= " ")


# import random
# # tao mang a
# a = []
# for i in range (20):
#     a.append(random.randint(1,1000))
# # hien thi
# for i in range (20):
#     print (a[i], end= " ")
# max = a[0]
# for i in range (20):
#     if a[i] > max:
#         max = a[i]
# print ("max", max)

# a = [1,"xinchao", {2,3}]
# b = [[1,4],[2,3,4],1]
# c = [(1,2,3,4),(8,7,9,19)]
# for x,y,z,t in c:
#     print (x,y,z,t)

# a= [4,5,6,7]
# print(a[2:4])

# a= ["sad","happy"]
# n= '''_♥__♥_____♥__♥___ Put This
# _♥_____♥_♥_____♥__ Heart
# _♥______♥______♥__ On Your
# __♥_____/______♥__ Page If
# ___♥____\_____♥___ You Had
# ____♥___/___♥_____ Your Heart
# ______♥_\_♥_______ Broken
# ________♥_________…………….'''
# print (n)

# # khai bao ham con
#
# import sub_function as sf
#
# b = [2,3,7]
# sum = sf.tinh_tong_mang (b)
# print (sum)
