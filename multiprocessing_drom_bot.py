import random
import selenium
from selenium import webdriver
from time import sleep
from random import randint
import selenium.webdriver.common.keys
import multiprocessing
import time

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
    for cycle in range(1, 2):
        print(f'***************  {cycle}ый цикл  ***************')
        browser = webdriver.Edge('D:\PYTHON\Drom_bot\edgedriver_win64\msedgedriver.exe')
        browser.get('https://www.drom.ru/')
        sleep(randint(3, 3))
        browser.get('https://baza.drom.ru/omsk/sell_spare_parts/')
        sleep(randint(3, 3))
        scroll = randint(300, 500)
        browser.execute_script(f"window.scrollTo(0, {scroll})")
        sleep(randint(3, 3))
        part_name = browser.find_element_by_name('query')
        part_name.clear()
        part_name.send_keys(random.choice(spare_parts_list))
        sleep(randint(3, 3))
        part_name.send_keys(selenium.webdriver.common.keys.Keys.ENTER)
        sleep(randint(3, 3))
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

                print(f'совпадение продавца: {i.text}')
                i.click()
                print('Обьявление открыто!')
                # phone = browser.find_element_by_xpath('//*[@id="fieldsetView"]/div/div[1]/'
                #                                       'div/div[3]/div[1]/noindex/div/a')
                # phone.click()
                # print('Телефон просмотрен')
                break
            else:
                print('Нет совпал продавец!')
        sleep(3)
        browser.close()


we_get_the_name_of_the_spare_part()
get_sellers()

if __name__ == "__main__":
    start = time.time()
    drom_bot_1 = multiprocessing.Process(target=drom_bot)
    drom_bot_2 = multiprocessing.Process(target=drom_bot)
    drom_bot_3 = multiprocessing.Process(target=drom_bot)
    drom_bot_4 = multiprocessing.Process(target=drom_bot)

    drom_bot_1.start()
    drom_bot_2.start()
    drom_bot_3.start()
    drom_bot_4.start()

    drom_bot_1.join()
    drom_bot_2.join()
    drom_bot_3.join()
    drom_bot_4.join()

    end = time.time()
    print(dict_sellers)
    print('Время работы:', end - start)
