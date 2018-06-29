# a = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# c = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# b = []
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] == a[j]:
#             b.append(a[i])
# for m in c:
#     for n in b:
#             if m == n:
#                 a.remove(m)
#                 b.remove(n)
# print(a)

# # Cach_2
# a = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# for i in range(len(a)):
#     for j in a[i+1:]:
#         if a[i] == j:
#             a.remove(a[i])
#             a.remove(j)
# print(a)

