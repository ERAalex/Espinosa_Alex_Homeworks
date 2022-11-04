
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.size_of_list = len(list_of_list)
        self.list_of_result = []

    def __unzip__(self):
        for items in self.list_of_list:
            for item in items:
                self.list_of_result.append(item)
        self.size_of_list = len(self.list_of_result)
        return self.list_of_result

    def __iter__(self):
        self.__unzip__()
        self.counter = 0
        return self

    def __next__(self):
        if self.counter >= self.size_of_list:
            raise StopIteration
        result = self.list_of_result[self.counter]
        self.counter += 1
        return result


# list_of_lists_1 = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]

# Cheking work of __unzip__
# new_item = FlatIterator(list_of_lists_1)
# FlatIterator.__unzip__(new_item)

#checking work of iteration
# for item in FlatIterator(list_of_list=list_of_lists_1):
#     print(item)


def test():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1), ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test()