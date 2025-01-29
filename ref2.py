# different approach

def parse_matrix(matrix):
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
    return formatted_matrix

def ref(matrix):
    matrixSet = set()
    for row in matrix:
        matrixSet.update(row)
    if len(matrixSet) == 1 and 0 in matrixSet:
        print("A = 0")
        return matrix
    
    n, m = len(matrix[0]), len(matrix)
    startpoint = 0
    for i in range(n):
        if any(row[i] != 0 for row in matrix):
            startpoint = i
            break
        # delete row
        for i in range(len(matrix)):
            matrix[i].pop(0)

    n_pivots = min(n, m)
    for pivot in range(n_pivots):
        if pivot < startpoint:
            continue
        elif pivot == startpoint:   
            matrix = make_pivot(matrix)
        else:
            submatrix = get_submatrix(matrix, pivot)
            newSubmatrix = make_pivot(submatrix)
            matrix = insert_submatrix(matrix, newSubmatrix)
    return matrix

def insert_submatrix(matrix, submatrix):
    n = len(submatrix[0])
    m = len(submatrix)
    n_startpoint = len(matrix[0]) - n
    m_startpoint = len(matrix) - m
    for idx, row in enumerate(submatrix, start=0):
        for index, element in enumerate(row, start=0):
            matrix[idx+m_startpoint][index+n_startpoint] = element
    return matrix

def make_pivot(matrix):
    print(matrix)
    for index, row in enumerate(matrix, start=0):
        if index == 0:
            # make first element 1
            newRow = [x/row[0] for x in row]
            matrix[index] = newRow
        else:
            # make first element 0
            for_subtract = row[0]
            substracting_row = [x*for_subtract for x in matrix[0]]
            newRow = [x-y for x, y, in zip(substracting_row, row)]
            matrix[index] = newRow
    print(matrix)
    return matrix
        
def get_submatrix(matrix, level):
    # Create a new submatrix instead of modifying the original
    submatrix = []
    for i in range(level, len(matrix)):
        new_row = matrix[i][level:]
        submatrix.append(new_row)
    return submatrix
            

def print_format(matrix):
    print("\n \t BEHOLD!\n")
    for row in matrix:
        text = "[ "
        for element in row:
            text += " " + str(element) + " "
        text += " ]"
        print(text)
    return 

def main():
    # p.d actually better to store groups as columns because of check need to go through all, but operations only need one loop
        # matrix = str(input("Enter the matrix like [1 2 3 ; 4 5 6 ; 7 8 9] (considering it is already the augmented matrix): "))
    # matrix = "[1 2 3 ; 4 5 6 ; 7 8 9]"
    matrix = "[3 3 3 ; 7 5 6 ; 10 8 9]"
    # matrix = "[0 0 0 ; 0 0 0]"
    matrix : list[list[int]] = parse_matrix(matrix)
    matrix = ref(matrix)
    print_format(matrix)
    

if __name__ == '__main__':
    main()
    