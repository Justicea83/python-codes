from math import pi


def vol(r):
    return 4 * pi * (r ** 3) / 3


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    rad = float(input('Enter the radius of the circle: ').strip())
    print(f'The volume of the circle is: {vol(rad)}')
