class Matrix:
    def __init__(self, size: int, data: [], right=None):
        self.coefficients = data
        self.size = size
        # optional right side of equation
        self.right = right

    def __str__(self):
        result = []
        for i in range(self.size):
            left = ''
            for j in range(self.size):
                left += f'{self.coefficients[i][j]:7.2f}'
            right = '  |' + f"{self.right[i]:7.2f}" if self.right is not None else ''
            result.append(left + right)
        return '\n'.join(result)