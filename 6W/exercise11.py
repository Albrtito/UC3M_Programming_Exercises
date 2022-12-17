import random
list = []

for i in range(0,100):
    list += [random.randint(1,1000)]

print(len(list))
print(list)
for i in range(0,100):
    if list[99-i] % 2 == 0:
        del(list[99-i])

print(list)





















