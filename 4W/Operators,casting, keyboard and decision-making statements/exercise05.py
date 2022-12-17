name_1 = str(input("Introduce first name: "))
age_1 = int(input("Introduce " + name_1 + "´s age: "))

name_2 = str(input("Introduce second name: "))
age_2 = int(input("Introduce " + name_2 + "`s age: "))

if age_1 > age_2:
    print(name_1, "is older than", name_2)

elif age_2 > age_1:
    print(name_2, "is older than", name_1)

else:
    print(name_2, "and", name_1,"are the same age")
