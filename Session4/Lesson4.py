 #[6]
# x = int(input("So hang: x = "))
# y = int(input("So cot: y = "))
# b = []
# for i in range(x):
#     a = []
#     for j in range(y):
#         a.append(i*j)
#     b.append(a)
# print(b)


# # Example_1
# a = [7, 10, 3, 5]
# b = []
# while len(a) > 0:
#     lowest = a[0]
#     for i in range(len(a)):
#         if lowest > a[i]:
#             lowest = a[i]
#     b.append(lowest)
#     a.remove(lowest)
# print(b)


# # [7]
# a = input("Nhap cac tu ").split(" ")
# b=[]
# while len(a)>0:
#     y = ord(a[0][0])
#     vi_tri_tu = 0
#     for i in range(len(a)):
#         if ord(a[i][0]) < y:
#             y = ord(a[i][0])
#             vi_tri_tu = i
#     b.append(a[vi_tri_tu])
#     a.remove(a[vi_tri_tu])
# print(b)