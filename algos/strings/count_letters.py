def count_letters(sentence: str):
    upper_case_count = 0
    lower_case_count = 0
    for word in sentence:
        if word.isupper():
            upper_case_count += 1
            continue
        if word.islower():
            lower_case_count += 1
    return upper_case_count, lower_case_count


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    ucc, lcc = count_letters(input('Enter the sentence: ').strip())
    print(f'No. of Upper case characters is  {ucc}')
    print(f'No. of Lower case characters is  {lcc}')
