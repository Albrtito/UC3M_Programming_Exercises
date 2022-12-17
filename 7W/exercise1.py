import random
n = int(input("Enter number of columns/rows: "))

matrix = []

for x in range(n):
    for y in range(n):
        if y != n:
            matrix.insert((x,y),random.randint)
            print(matrix[x,1],"+",matrix[x,2],"+",matrix[x,3],"=", matrix[x,4])
        else:
            matrix[x,y] = sum.matrix[1]




