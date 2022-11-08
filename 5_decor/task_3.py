import os
import datetime


def logger(old_function):
    time_now = str(datetime.datetime.now())
    def new_function(*args, **kwargs):
        # данные по функции
        data = locals()
        # print(data)
        result_fun = old_function(*args, **kwargs)
        with open('task_3.log', 'w+', encoding='utf8') as f:
            f.write(f'the function used at: {time_now} \n')
            f.write(f'name of function is: {old_function.__name__}')
            f.write(f"\n*args are: {data['args']}")
            f.write(f"\n*kwargs are: {data['kwargs']}")
            f.write(f"\nresult of function is: {result_fun} \n 'Конец записи' \n")
            f.close()
        return result_fun
    return new_function


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



def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    list_of_lists_1 = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]

    # Cheking work of __unzip__
    new_item = FlatIterator(list_of_lists_1)
    FlatIterator.__unzip__(new_item)

    # checking work of iteration

    @logger
    def list_check(list_of_lists_1):
        all_items = []
        for item in FlatIterator(list_of_list=list_of_lists_1):
            all_items.append(item)
        return all_items

    list_check(list_of_lists_1)


if __name__ == '__main__':
    test_1()