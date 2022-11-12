import unittest
from task_3 import enter_yandex, find_input_field_put_login

import os


login = os.getenv('login')
password = os.getenv('password')

good_url = 'https://passport.yandex.ru/auth/'
false_url = 'https://passport.yandex.ru/auth/sdsdds'

path_file_chromedriver = os.getenv('path_file_chromedriver')

good_xpath_inp_1 = '//*[@id="passp-field-login"]'

good_xpath_butt_1 = '//*[@id="passp:sign-in"]'



class Yandex_enter(unittest.TestCase):

    def test_enter_yandex_url(self):
        self.assertEqual(enter_yandex(path_file_chromedriver, good_url), 200)
        self.assertEqual(enter_yandex(path_file_chromedriver, false_url), 404)


    def test_find_input_field_put_login(self):
        self.assertRaises(Exception, find_input_field_put_login, 'sddsds', login)
        assert find_input_field_put_login(good_xpath_inp_1, login) == 'Логин или email'


