import selenium
from selenium import webdriver
from time import sleep
from random import randint
import selenium.webdriver.common.keys

URL = 'https://baza.drom.ru/omsk/sell_spare_parts/'


def drom_bot(url):
    browser = webdriver.Edge('D:\PYTHON\Drom_bot\edgedriver_win64\msedgedriver.exe')
    browser.get(url)
    part_name = browser.find_element_by_name('query')
    part_name.clear()
    part_name.send_keys('Пыльник ШРУСа FB2147')
    sleep(randint(2, 5))
    part_name.send_keys(selenium.webdriver.common.keys.Keys.ENTER)

    sleep(5)
    browser.close()


drom_bot(url=URL)
