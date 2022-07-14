class Cell:
    def __init__(self, cells):
        if type(cells) != int and cells <= 0:
            print('Неправильный ввод данных')
        else:
            self.cells = cells

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        sub = self.cells - other.cells
        if sub <= 0:
            sub = 'При вычитание получилось отрицательное число'
        return sub

    def __mul__(self, other):
        return self.cells * other.cells

    def __truediv__(self, other):
        return self.cells // other.cells if self.cells // other.cells != 0 else 'Получился 0'

    def make_order(self, row):
        structure = ''
        for i in range(self.cells):
            if (i + 1) % row != 0:
                structure += '*'
            else:
                structure += '*\n'
        return structure


if __name__ == "__main__":
    cell1 = Cell(12)
    cell2 = Cell(15)

    print('Проверка вывода клетки:')
    print(cell1.make_order(5))
    print(cell2.make_order(6))

    print('Проверка вычитания:')
    print(cell2 - cell1)
    print(cell1 - cell2)

    print('Проверка сложения:')
    print(cell1 + cell2)

    print('Проверка умножения:')
    print(cell1 * cell2)

    print('Проверка деления:')
    print(cell1 / cell2)
    print(cell2 / cell1)
