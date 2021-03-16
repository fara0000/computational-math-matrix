from matrix import Matrix
from result import solve


def create_filled_matrix(size: int, get_line) -> Matrix:
    data = []
    right = []
    for line in range(0, size):
        equation = list(map(float, get_line().split()))
        right.append(equation.pop())
        data.append(equation)
    return Matrix(size, data, right)


def size_validation(size: int):
    if not 0 < size <= 20:
        print('The matrix must have a size from 1 to 20 inclusive.')
        exit(-1)
    return size


while True:
    filename = input('Enter the file name to load the matrix or an empty line to enter manually: ')

    if filename == '':
        precision = input('Accuracy: ')
        size = size_validation(int(input('Matrix size: ')))
        print('Matrix coefficients: ')
        matrix = create_filled_matrix(size, input)
    else:
        try:
            file = open(filename, 'r')
            precision = file.readline()
            size = size_validation(int(file.readline()))
            matrix = create_filled_matrix(size, file.readline)
            file.close()
        except FileNotFoundError:
            print('File not found.')
            continue

    print('Source matrix: ')
    print(matrix)

    solution = solve(matrix, precision)

    if solution:
        print('\nSolution:')
        print(solution)

    if input('Again? [y/n] ') != 'y':
        break
