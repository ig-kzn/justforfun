a = int(input())
b = int(input())
c = 0
# while a != 0 and b != 0:
#     if a >= 1:
#         c += 1
#         break
#     a = int(input())
#     b = int(input())
# if c >= 1:
#     print('ДА')
# else:
#     print('НЕТ')
while not(a == 0 and b == 0): # a != 0 and b != 0:
    if a > 0:
        c += 1
    a = int(input())
    b = int(input())
if c > 0:
    print('ДА')
else:
    print('НЕТ')