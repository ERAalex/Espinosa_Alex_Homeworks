from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os


path_file_chromedriver = os.getenv('path_file_chromedriver')
login = os.getenv('login')
password = os.getenv('password')
url = 'https://passport.yandex.ru/auth/'

#
#
# class Yandex_login():
#
#     def __init__(self, y_path_file, y_login, y_password):
#         self.y_path_file = y_path_file
#         self.y_login = y_login
#         self.y_password = y_password
#         self.s = Service(self.y_path_file)
#         self.browser = webdriver.Chrome(service=self.s)
#
#     def connect_to_url(self, y_url):
#         if type(y_url) != str:
#             raise TypeError('Адресная строка имеет тип данных str!')
#         else:
#             self.browser.get(y_url)
#
#     def find_and_input_login(self, xpath_login):
#         input_tab_login = self.browser.find_element(By.XPATH, xpath_login )
#         input_tab_login.send_keys(self.y_login)
#
#
#
#
#
# start = Yandex_login(path_file_chromedriver, login, password)
#
# start.connect_to_url(url)

#
#
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import os
#
# t_path_file_chromedriver = os.getenv('path_file_chromedriver')
# t_login = os.getenv('login')
# t_password = os.getenv('password')
#
#
#
#
#
#
# def enter_yandex(path_file_chromedriver, login, password):
#     s = Service(path_file_chromedriver)
#     browser = webdriver.Chrome(service=s)
#     url = 'https://passport.yandex.ru/auth/'
#     browser.get(url)
#
#
# def find_input_field_put_login(xpath_s, login_s):
#     input_tab_login = browser.find_element(By.XPATH, '//*[@id="passp-field-login"]')
#     input_tab_login.send_keys(login)
#
#
#
#     button_ok = browser.find_element(By.XPATH, '//*[@id="passp:sign-in"]')
#     button_ok.click()
#     sleep(2)
#
#     input_tab_password = browser.find_element(By.XPATH, '//*[@id="passp-field-passwd"]')
#     input_tab_password.send_keys(password)
#     sleep(1)
#
#     button_ok = browser.find_element(By.XPATH, '//*[@id="passp:sign-in"]')
#     button_ok.click()
#     sleep(2)
#
#     try:
#         #mobile check
#         button_ok = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]'
#                                                    '/div[3]/div/div/div/div[1]/form/div[2]/button')
#         button_ok.click()
#         sleep(1)
#     except:
#         pass
#
#     sleep(20000)
#
#
# if __name__ == "__main__":
#     enter_yandex()
#
#
#
# path_file_chromedriver = os.getenv('path_file_chromedriver')
# login = os.getenv('login')
# password = os.getenv('password')
# url = 'https://passport.yandex.ru/auth/'
# false_XPATH_1 = '//*[@id="passp-fieldsss-login"]'
# good_XPATH_1 = '//*[@id="passp-field-login"]'
#
# class YandexEntr(unittest.TestCase):
#
#     def test_check_type_url(self):
#         new_item = Yandex_login(path_file_chromedriver, login, password)
#         with self.assertRaises(Exception):
#             new_item.connect_to_url({'dsds': 'some_key'})
#
#         assert new_item.connect_to_url(url) == None
#
#
#     def test_find_and_input_login(self):
#         new_item = Yandex_login(path_file_chromedriver, login, password)
#         with self.assertRaises(Exception):
#             new_item.find_and_input_login(good_XPATH_1)
