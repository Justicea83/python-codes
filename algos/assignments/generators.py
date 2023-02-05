def create_cubes(n):
    for x in range(n):
        yield x ** 3

create_cubes(10)