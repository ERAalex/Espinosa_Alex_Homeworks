import json
import unittest
from task_2 import create_folder


token = 'y0_AgAAAABU48rYAAhViQAAAADMh1IKp3b8VZPgQ_C7kBP8muK0JUadra8'
fail_token = 'asdasHelloWorldsdfsdfd'

class TestYandex(unittest.TestCase):

    def test_token_dict_json_recive(self):
        self.assertEqual(type(create_folder(token, 'Hey').json()), dict)

    def test_response_200(self):
        self.assertEqual(create_folder(token, 'nn1').status_code, 201)

    def test_result_expected_get(self):
        # пробуем создать папку, если она уже существует сразу проверяем это исключение
        try:
            result = create_folder(token, 'h1').json()
            self.assertEqual(result['method'], 'GET')
        except:
            self.assertEqual(result['error'], 'DiskPathPointsToExistentDirectoryError')


    def test_fail_token(self):
        result = create_folder(fail_token, 'new_folder').json()
        self.assertEqual(result['error'], 'UnauthorizedError')


