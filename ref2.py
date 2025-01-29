# second approach

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

def get_non_zero_diagonals(matrix):
    n = len(matrix)
    used_rows = set()

    for i in range(n):
        found = False
        for j in range(n):
            if j not in used_rows and matrix[j][i] != 0:
                if i != j:
                    # Swap rows to bring a non-zero element to the diagonal
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                used_rows.add(j)
                found = True
                break
        
        if not found:
            raise ValueError(f"No non-zero element found for column {i}. Cannot ensure non-zero diagonal.")
    
    return matrix, True

    
def clean_zero_columns(matrix):
    n = len(matrix[0])
    col = 0

    while col < n:
        if all(row[col] == 0 for row in matrix):
            for row in matrix:
                row.pop(col)
            n -= 1
        else:
            col += 1
    return matrix

def ref(matrix):
    matrixSet = set()
    for row in matrix:
        matrixSet.update(row)
    if len(matrixSet) == 1 and 0 in matrixSet:
        print("A = 0")
        return matrix
    
    n, m = len(matrix[0]), len(matrix)
    n_pivots = min(n, m)
    matrix = clean_zero_columns(matrix)
    matrix, swapability = get_non_zero_diagonals(matrix)
    
    if swapability is False:
        raise ValueError("Cannot make a non-zero diagonal")

    for pivot in range(n_pivots):
        if pivot == 0:   
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
    print("Before pivoting:", matrix)
    
    # Base case: If matrix has 1 row and the pivot is zero, return as-is
    if len(matrix) == 1 and matrix[0][0] == 0:
        return matrix
    
    for index, row in enumerate(matrix):
        if index == 0:
            if row[0] == 0:
                raise ValueError("Pivot element is zero. Cannot proceed with pivoting.")
            matrix[index] = [x / row[0] for x in row]
        else:
            factor = row[0]
            if factor != 0:
                subtracted_row = [x * factor for x in matrix[0]]
                matrix[index] = [y - x for x, y in zip(subtracted_row, row)]
    print("After pivoting:", matrix)
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
    matrix = str(input("Enter the matrix like [1 2 3 ; 4 5 6 ; 7 8 9] (considering it is already the augmented matrix): "))
    # matrix = "[1 1 1 ; 7 5 6 ; 10 8 9]" # for test
    matrix : list[list[int]] = parse_matrix(matrix)
    matrix = ref(matrix)
    print_format(matrix)
    

if __name__ == '__main__':
    main()
    