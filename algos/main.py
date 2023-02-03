from data_structures.linked_list import LinkedList, is_palindrome

def test_is_palindrome(item: str):
    linked_list = LinkedList()
    for i in item:
        linked_list.add(i)

    print(f'Is it palindrome: {is_palindrome.is_palindrome(linked_list.head)}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_is_palindrome('kayak')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
