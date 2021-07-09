a = int(input("Ввод a: "))
b = int(input("Ввод b: "))
if a<b:
    for i in range(a, b + 1):
        print(i)
else :
    for i in range(a, b-1, -1):
        print(i)


