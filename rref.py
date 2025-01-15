# give a matrix and be returned a rref matrix

matrix = str(input("Enter the matrix like [1 2 3 ; 4 5 6 ; 7 8 9] (considering it is already the augmented matrix): "))
# parsed into nested lists
matrix = matrix[1:-1]
print(matrix)
matrix : list[str] = matrix.split(" ")
print(matrix)
formatted_matrix = [[]]
count : int = 0
for x in matrix:
    if x == ";":
        formatted_matrix.append([])
        count += 1
    else:
        formatted_matrix[count].append(int(x))
print(formatted_matrix)
# actually transform to rref

