from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver
import os
import json

t_path_file_chromedriver = os.getenv('path_file_chromedriver')
t_login = os.getenv('login')
t_password = os.getenv('password')
url_adres = 'https://passport.yandex.ru/auth/'


good_xpath_inp_1 = '//*[@id="passp-field-login"]'
badd_xpath_inp_1 = '//*[@id="passp-fsddsld-login"]'

good_xpath_butt_1 = '//*[@id="passp:sign-in"]'
badd_xpath_butt_1 = '//*[@id="passp:sisdsd-in"]'

good_xpath_inp_2 = '//*[@id="passp-field-passwd"]'
badd_xpath_inp_2 = '//*[@id="passp-fsddsdsld-login"]'

good_xpath_butt_2 = '//*[@id="passp:sign-in"]'
badd_xpath_butt_2 = '//*[@id="passp:ssdssdign-in"]'


def enter_yandex(chromedriver_argument, url_adr):
    list_response = []
    s = Service(chromedriver_argument)
    browser = webdriver.Chrome(service=s)
    url = url_adr
    browser.get(url)
    for request in browser.requests:
        if request.response:
            list_response.append(request.response.status_code)
    status_code = list_response[1]
    return status_code



def find_input_field_put_login(xpath_s, login_s):
    s = Service(t_path_file_chromedriver)
    browser = webdriver.Chrome(service=s)
    url = 'https://passport.yandex.ru/auth/'
    browser.get(url)

    input_tab_login = browser.find_element(By.XPATH, xpath_s)
    input_tab_login.send_keys(login_s)
    return input_tab_login.accessible_name




def find_button_ok_1(xpath_button):
    s = Service(t_path_file_chromedriver)
    browser = webdriver.Chrome(service=s)
    url = 'https://passport.yandex.ru/auth/'
    browser.get(url)

    button_ok = browser.find_element(By.XPATH, xpath_button)
    button_ok.click()
    sleep(2)
    return browser


def find_input_field_put_password(xpath_s, password):
    s = Service(t_path_file_chromedriver)
    browser = webdriver.Chrome(service=s)
    url = 'https://passport.yandex.ru/auth/'
    browser.get(url)

    input_tab_password = browser.find_element(By.XPATH, xpath_s)
    input_tab_password.send_keys(password)
    sleep(1)
    return browser


def find_button_ok_2(xpath_button):
    s = Service(t_path_file_chromedriver)
    browser = webdriver.Chrome(service=s)
    url = 'https://passport.yandex.ru/auth/'
    browser.get(url)

    button_ok = browser.find_element(By.XPATH, xpath_button)
    button_ok.click()
    sleep(3)


