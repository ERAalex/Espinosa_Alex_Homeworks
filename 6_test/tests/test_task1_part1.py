import pytest
from task_1 import only_russia


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


def test_only_russia():
    assert len(only_russia(geo_logs)) == 6


@pytest.mark.parametrize("list, expected_result",
        [([{'visit6': ['Гары', 'Швеция']}, {'visit7': ['Тула', 'Россия']}], [{'visit7': ['Тула', 'Россия']}]),
         ([{'visit5': ['Манчестер', 'Великобритания']}, {'visit6': ['Лиссабон', 'Португалия']}], []),])
def test_only_russia_more_country(list, expected_result):
    assert only_russia(list) == expected_result


@pytest.mark.parametrize("expected_exception, argument",
                         [(AttributeError, {"sdsdsdsd": 5}),
                          (AttributeError, 'hello world'),
                          ])
def test_only_russia_type_not_list_error(expected_exception, argument):
    with pytest.raises(expected_exception):
        only_russia(argument)




