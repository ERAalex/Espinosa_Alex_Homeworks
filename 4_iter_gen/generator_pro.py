import types



def flat_generator(list_of_list):
    our_list = list_of_list
    our_elements = []
    while our_list:
        elem = our_list.pop(-1)
        # если элемент список, кидаем в конец, если нет, берем к себе в our_elements
        # алгоритм методом перебора и скидывания в конец
        if isinstance(elem, list):
            our_list.extend(elem)
        else:
            our_elements.append(elem)
    our_elements_final = our_elements[::-1]
    for items in our_elements_final:
        yield items


## check generator

# list_of_lists_2 = [[['a'], ['b', 'c']], ['d', 'e', [['f'], 'h'], False], [1, 2, None, [[[[['!']]]]], []]]
# test_result = flat_generator(list_of_lists_2)
# type(test_result)
# for x in test_result:
#     print(x)


def test():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    list_of_lists_3 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_3)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test()
