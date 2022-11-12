import pytest
from task_1 import find_max_size

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def test_find_max_size_list_count():
    assert find_max_size(stats) == 'yandex'



@pytest.mark.parametrize("expected_exception, argument", [(AttributeError, 'somewords'),
                                                      (AttributeError, [3, 5, 6, 7]),
                                                      (TypeError, {'facebook': 'dsdsd', 'yandex': 120, 'vk': 115}),
                                    ])
def test_find_max_size_type(expected_exception, argument):
    with pytest.raises(expected_exception):
        find_max_size(argument)

