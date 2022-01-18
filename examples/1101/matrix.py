class Matrix:
    size_cols: int
    size_rows: int

    def __init__(self, _size_cols=4, _size_rows=4, auto_generate: bool = True) -> None:
        self.size_cols = _size_cols
        self.size_rows = _size_rows
        if auto_generate:
            self.my_matrix = self.generate_matrix()

    def generate_matrix(self) -> list:
        return [[0 for _ in range(self.size_cols)] for _ in range(self.size_rows)]

    # print matrix
    def print_matrix(self):
        for line in self.my_matrix:
            print(line)
        print()

    def main_diagonal(self):
        for x in range(min(self.size_rows, self.size_cols)):
            self.my_matrix[x][x] = 1

    def foo(self):
        for x in range(self.size_rows):
            for y in range(self.size_cols):
                if y < x:
                    self.my_matrix[x][y] = 9
                elif x == y:
                    break


sizes = [(3, 10), (10, 3), (10, 10)]

for s in sizes:
    m2 = Matrix(*s)
    m2.main_diagonal()
    m2.foo()
    m2.print_matrix()

