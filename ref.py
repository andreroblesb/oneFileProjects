# provide a matrix and get a rref matrix
# outdated: see "ref2"
from fractions import Fraction

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

def rref(matrix):
    m: int = len(matrix)
    for row in range(m):
        pivot = matrix[row][row]
        if pivot == 1:
            make_pivot_unique(matrix, row, m)
        elif pivot == 0:
            matrix[row][row] += 1
            matrix[row][-1] += 1
        else:
            matrix[row] = [Fraction(element, pivot) for element in matrix[row]]
    return matrix
                
def make_pivot_unique(matrix, current_pivot_row, m):
    pivotRow = matrix[current_pivot_row]
    for row in range(m):
        if row == current_pivot_row:
            continue
        scaling_factor = matrix[row][current_pivot_row]
        temp = list(map(lambda x : x * scaling_factor, pivotRow))
        # substract
        matrix[row] = [a - b for a, b in zip(matrix[row], temp)]
    return 

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
    # matrix = str(input("Enter the matrix like [1 2 3 ; 4 5 6 ; 7 8 9] (considering it is already the augmented matrix): "))
    matrix = "[1 2 3 ; 4 5 6 ; 7 8 9]"
    matrix = parse_matrix(matrix)
    print_format(rref(matrix))
    

if __name__ == '__main__':
    main()
