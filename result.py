from matrix import Matrix


class Solution:
    def __init__(self, x_vector, iterations, error_vector, digits_after_dot=None):
        self.digits_after_dot = digits_after_dot
        self.error_vector = error_vector
        self.iterations = iterations
        self.x_vector = x_vector

    def __str__(self):
        result = 'Vector of unknowns: '
        if self.digits_after_dot:
            formatted_vector = list(map(lambda x: round(x, self.digits_after_dot), self.x_vector))
            result += f'{formatted_vector}\n'
        else:
            result += f'{self.x_vector}\n'

        result += f'Number of iterations: {self.iterations}\n'
        result += f'Error vector: {self.error_vector}\n'
        return result


def solve(matrix: Matrix, precision: str):
    digits_after_dot = len(precision.split('.')[1].rstrip('0'))
    precision = float(precision)
    x_vector = [0] * matrix.size
    # x_vector = matrix.right

    # проверка диагонального преобладания
    if not matrix.diagonally_dominant:
        print('Matrix not diagonally dominant, attempted permutation...')
        if not matrix.make_diagonally_dominant():
            print('Failed to achieve diagonal dominance: Calculation completed.')
            return None
        else:
            print('New matrix: ')
            print(matrix)

    # вычисление матрицы C
    c_matrix = []
    for row in range(matrix.size):
        a_ii = matrix.coefficients[row][row]
        row_vector = []
        for column in range(matrix.size):
            c = -matrix.coefficients[row][column] / a_ii if row != column else 0
            row_vector.append(c)
        c_matrix.append(row_vector)

    # iteration
    iterations = 0
    error_vector = [0] * len(x_vector)

    while True:
        iterations += 1
        for i in range(len(x_vector)):
            a = matrix.coefficients[i][i]
            b = matrix.right[i]
            cx_array_sum = sum(map(lambda c_ij: c_ij * x_vector[i], c_matrix[i]))

            prev = x_vector[i]
            x_vector[i] = cx_array_sum + b / a
            error_vector[i] = abs(x_vector[i] - prev)

        if max(error_vector) <= precision:
            break

    return Solution(x_vector, iterations, error_vector, digits_after_dot)
