
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]



def only_russia(geo_logs):
    for x in range(len(geo_logs)):
        for items in geo_logs:
            for key, value in items.items():
                if 'Россия' not in value:
                    geo_logs.remove(items)

    return geo_logs


####################################__EXAMPLE_2__####################################


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}



def get_unique_list(some_dict):
    result = []
    if type(some_dict) != dict:
        raise ValueError('Вы привели как пример не словарь')
    else:
        for key, value in some_dict.items():
            for item in value:
                result.append(int(item))
        check_result = set(result)
        return check_result



#
####################################__EXAMPLE_3__####################################

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def find_max_size(some_dict):
    all_numbers = []
    for key, value in some_dict.items():
        all_numbers.append(value)
    result_numb = max(all_numbers)
    for key, value in stats.items():
        if value == result_numb:
            return key

