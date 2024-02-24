print("Задание№18")
for i in range(3, 11, 4):
	print(i)

print("Задание№19")
lst = [2, 6, 43, 1, 66]
s = 0
for item in lst:
    if item % 2 == 0:
        s += 1
    else:
        continue

print("Задание№20")
x = float(input())
sum = x
j= 1
for i in range(j+i):
    a = x**i/i
    sum =sum +(a)
    if(a <= 10**-6):
        break
print(sum)



