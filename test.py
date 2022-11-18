a = int(input())
d = int(input())
count = 0
caunt = 0
while a != 0 and d != 0:
    if d > a:
        count += 1
    else:
        caunt += 1
    a = int(input())
    d = int(input())
if count > caunt:
    print(count)
else:
    print(caunt)