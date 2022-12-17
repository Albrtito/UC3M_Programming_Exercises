import random

int_A = int(input("Enter first integer: (A): "))
int_B = int(input("""Enter second integer (B) sucha as:
 A + 5 < B :  """))
count = 0

while int_A + 5 >= int_B:
    int_B = int(input("""Enter again second integer (B) sucha as:
     A + 5 < B 
     The first try didn`t comply with the rule: """))

even_and_odd = []

for i in range(5):
    i = random.randint(int_A,int_B)
    #print(i)
    if count % 2 == 0:
        #print("odd")
        while i % 2 != 0:
            i = random.randint(int_A,int_B)
            #print(i)

    else:
        print("even")
        while i % 2 == 0:
            i = random.randint(int_A, int_B)
            #print(i)


    even_and_odd += [i]
    count += 1

print(even_and_odd)