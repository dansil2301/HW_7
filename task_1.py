class Matrix:
    def __init__(self, ls_of_ls):
        self.ls_of_ls = ls_of_ls

    def __str__(self):
        output = ''
        for i in range(len(self.ls_of_ls)):
            for j in range(len(self.ls_of_ls[i])):
                output += str(self.ls_of_ls[i][j]) + (' ' if j != len(self.ls_of_ls[i]) - 1 else '\n')
        return output

    def __add__(self, other):
        line_matrix = []
        new_matrix = []

        for i in range(len(self.ls_of_ls)):
            for j in range(len(self.ls_of_ls[i])):
                line_matrix.append(self.ls_of_ls[i][j] + other.ls_of_ls[i][j])
            new_matrix.append(line_matrix)
            line_matrix = []

        return Matrix(new_matrix)


if __name__ == "__main__":
    m1 = Matrix([[1, 2], [1, 2], [3, 2]])
    m2 = Matrix([[2, 1], [2, 1], [3, 2]])

    print(m1)
    print(m1 + m2 + m1)
