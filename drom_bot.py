import selenium
from selenium import webdriver
from time import sleep
from random import randint
import selenium.webdriver.common.keys

URL = 'https://baza.drom.ru/omsk/sell_spare_parts/'


def drom_bot(url):
    browser = webdriver.Edge('D:\PYTHON\Drom_bot\edgedriver_win64\msedgedriver.exe')
    browser.get('https://www.drom.ru/')
    sleep(randint(3, 5))
    browser.get(url)
    sleep(randint(3, 5))
    scroll = randint(300, 500)
    browser.execute_script(f"window.scrollTo(0, {scroll})")
    sleep(randint(3, 5))
    part_name = browser.find_element_by_name('query')
    part_name.clear()
    part_name.send_keys('Пыльник ШРУСа FB2147')
    sleep(randint(3, 5))
    part_name.send_keys(selenium.webdriver.common.keys.Keys.ENTER)
    value = browser.find_elements_by_class_name('descriptionCell bull-item-content__cell bull-item-content__'
                                                'description-cell js-description-block').text
    print(value)

    sleep(5)
    browser.close()


drom_bot(url=URL)
