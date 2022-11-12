import pytest
from task_1 import get_unique_list


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

ids2 = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 'hello', 119, 119],
       'user3': [213, 98, 98, 35]}


def test_get_unique_list_count():
    assert len(get_unique_list(ids)) == 6



@pytest.mark.parametrize("expected_exception, argument", [(ValueError, 'somewords'),
                                                      (ValueError, [3, 5, 6, 7]),
                                    ])
def test_get_unique_list_type(expected_exception, argument):
    with pytest.raises(expected_exception):
        get_unique_list(argument)


def test_get_unique_list_not_type_in_dict():
    with pytest.raises(ValueError):
        get_unique_list(ids2)


