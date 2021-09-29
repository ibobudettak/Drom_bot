import random
import selenium
from selenium import webdriver
from time import sleep
from random import randint
import selenium.webdriver.common.keys

URL = 'https://baza.drom.ru/omsk/sell_spare_parts/'

spare_parts_list = []
list_of_sellers = []


def we_get_the_name_of_the_spare_part():
    with open('артикул-только-названия.txt', mode='r', encoding='utf 8') as file:
        for line in file:
            spare_parts_list.append(line.replace('|', '')[:-1])


def get_sellers():
    with open('пользователи.txt', mode='r', encoding='utf 8') as sellers_file:
        for sellers in sellers_file:
            list_of_sellers.append(sellers[:-1])


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
    part_name.send_keys(random.choice(spare_parts_list))
    sleep(randint(3, 5))
    part_name.send_keys(selenium.webdriver.common.keys.Keys.ENTER)
    sleep(randint(3, 5))
    value = browser.find_elements_by_class_name('ellipsis-text__left-side')
    for i in value:
        if str(i.text) == str(random.choice(list_of_sellers)):
            i.click()
            break
    sleep(5)
    browser.close()


we_get_the_name_of_the_spare_part()
get_sellers()
drom_bot(url=URL)
