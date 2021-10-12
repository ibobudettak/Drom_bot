import random
import selenium
from selenium import webdriver
from time import sleep
from random import randint
import selenium.webdriver.common.keys
import threading
import logging
import subprocess
import datetime

logging.basicConfig(filename="sample.log", filemode='w', level=logging.ERROR)

spare_parts_list = []
list_of_sellers = []
dict_sellers = {}


def we_get_the_name_of_the_spare_part():
    with open('артикул-только-названия.txt', mode='r', encoding='utf 8') as file:
        for line in file:
            spare_parts_list.append(line.replace('|', '')[:-1])


def get_sellers():
    with open('пользователи.txt', mode='r', encoding='utf 8') as sellers_file:
        for sellers in sellers_file:
            list_of_sellers.append(sellers[:-1])


def drom_bot():
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome('chromedriver.exe', chrome_options=options)
    browser.get('https://www.drom.ru/')
    sleep(4)
    browser.get('https://baza.drom.ru/omsk/sell_spare_parts/')
    sleep(4)
    scroll = randint(300, 500)
    browser.execute_script(f"window.scrollTo(0, {scroll})")
    sleep(4)
    part_name = browser.find_element_by_name('query')
    part_name.clear()
    part_name.send_keys(random.choice(spare_parts_list))
    sleep(4)
    part_name.send_keys(selenium.webdriver.common.keys.Keys.ENTER)
    sleep(4)
    value = browser.find_elements_by_class_name('ellipsis-text__left-side')
    for i in value:
        if str(i.text) in list_of_sellers:
            key = i.text
            count = 1
            if key in dict_sellers:
                v_dict = dict_sellers[key]
                v_dict += 1
                dict_sellers[key] = v_dict
            else:
                dict_sellers[key] = count
            logging.error(f'совпадение продавца: {i.text}')
            i.click()
            break
    browser.close()


we_get_the_name_of_the_spare_part()
get_sellers()

threading_bot = ['drom_bot_1', 'drom_bot_2', 'drom_bot_3', 'drom_bot_4', 'drom_bot_5']
logging.error(f' Программа запущена: {datetime.datetime.now()}')
for cycle in range(1, 101):
    logging.error(f'***************** Цикл №{cycle} *****************')
    threads_bot = [threading.Thread(target=drom_bot) for bots in threading_bot]
    for bot in threads_bot:
        bot.start()
    for bot in threads_bot:
        bot.join()
    subprocess.call('СкриптМегафон.bat')
logging.error(dict_sellers)
print(dict_sellers)