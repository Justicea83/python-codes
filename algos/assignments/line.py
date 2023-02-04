from math import sqrt


class Line:
    def __init__(self, coor1: tuple[int, int], coor2: tuple[int, int]):
        self.coor1 = coor1
        self.coor2 = coor2

    def slope(self):
        return self.y_diff() / self.x_diff()

    def distance(self):
        return sqrt(self.x_diff() ** 2 + self.y_diff() ** 2)

    def y_diff(self):
        return self.coor2[1] - self.coor1[1]

    def x_diff(self):
        return self.coor2[0] - self.coor1[0]


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    coordinate1 = (3, 2)
    coordinate2 = (8, 10)
    li = Line(coordinate1, coordinate2)
    print(f'This distance is {li.distance()}')
    print(f'This slope is {li.slope()}')
