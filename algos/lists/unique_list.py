def unique_list(lst: list) -> list:
    return list(set(lst))


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    sample = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3,4,5]
    res = unique_list(sample)
    print(f'The unique is:  {res}')
