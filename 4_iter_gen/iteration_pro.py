class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.size_of_list = len(list_of_list)
        self.list_of_result = []


    def __unzip__(self):
        our_list = self.list_of_list
        our_elements = []
        while our_list:
            elem = our_list.pop(-1)
            # если элемент список, кидаем в конец, если нет, берем к себе в our_elements
            # алгоритм методом перебора и скидывания в конец
            if isinstance(elem, list):
                our_list.extend(elem)
            else:
                our_elements.append(elem)
        # придется вернуть таким, образом, чтобы сохранить порядок, мы ведь все перекидывали в конец
        self.size_of_list = len(our_elements)
        self.list_of_result = our_elements[::-1]
        return our_elements[::-1]



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





# list_of_lists_2 = [[['a'], ['b', 'c']], ['d', 'e', [['f'], 'h'], False], [1, 2, None, [[[[['!']]]]], []]]

# Cheking work of __unzip__
# new_item = FlatIterator(list_of_lists_2)
# print(list(FlatIterator(list_of_lists_2)))
# print(FlatIterator.__unzip__(new_item))



def test():

    list_of_lists_2 = [[['a'], ['b', 'c']], ['d', 'e', [['f'], 'h'], False], [1, 2, None, [[[[['!']]]]], []]]
    list_of_lists_3 = [[['a'], ['b', 'c']], ['d', 'e', [['f'], 'h'], False], [1, 2, None, [[[[['!']]]]], []]]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_2), ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_3)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test()