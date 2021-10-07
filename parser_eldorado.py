from pprint import pprint
from selenium import webdriver
from time import sleep

dict_price = {}


def parser():
    browser = webdriver.Edge('D:\PYTHON\Drom_bot\edgedriver_win64\msedgedriver.exe')
    browser.get('https://www.eldorado.ru/c/smartfony/?page=12')
    sleep(3)
    container = browser.find_elements_by_xpath('//*[@id="listing-container"]/ul/li[*]')
    number = len(container)
    for i in range(1, number):
        name = browser.find_element_by_xpath(f'//*[@id="listing-container"]/ul/li[{i}]/div[2]/a')
        price = browser.find_element_by_xpath(f'//*[@id="listing-container"]/ul/li[{i}]/div[3]/div[1]/span')
        dict_price[name.text] = price.text
    browser.close()


parser()
pprint(dict_price)
