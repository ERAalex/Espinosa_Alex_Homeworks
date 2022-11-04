import types


def flat_generator(list_of_lists):
    for items in list_of_lists:
        for item in items:
            yield item


#check generator
# list_of_lists_1 = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
# test_result = flat_generator(list_of_lists_1)
# type(test_result)
# for x in test_result:
#     print(x)
#


def test():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test()