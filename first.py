# layout_testing
import urllib
from lxml import etree
from lxml import html
from selenium import webdriver
import json
from selenium.webdriver.common.action_chains import ActionChains


def get_parameters_of_element(e):
    #Нашли элемент
    try:
        element = driver.find_element_by_xpath(get_xpath_of_el(e))
        # Запихнули в словарь нужные параметры отрисованного элемента
        x = element.location['x']
        y = element.location['y']
        height = element.size['height']
        width = element.size['width']
        if bad_position(x, y, height, width):
            d = 'bad'
        else:
            d = dict(x=element.location['x'], y=element.location['y'],
                    height=element.size['height'], width=element.size['width'])
            #print(get_xpath_of_el(e))
    except:
        d = 'bad'

    return d


#Количество детей у элемента дерева
def сhild_сount(item):
    return len(e.getchildren())

#Создание дерева
def create_tree(url):
    response = urllib.request.urlopen(url).read()
    tree = html.fromstring(response)
    return etree.ElementTree(tree)


#Откидываем плохие элементы
def bad_position(x, y, height, width):
    if (x == 0 & y == 0) or (x < 0) or (y < 0):
        return True
    else:
        return False

#Откидываем плохие xpath
def bad_xpath(e):
    #if ('div' in e.text[-6:]):
    if (e.find('div',-6) != -1):
        return True
    else:
        return False


#Добавление xpath всем элементам
def add_xpath(tree):
    for element in tree.iter():
        xpath = tree.getpath(element)
        #Если у нас див-то мы удаляем этот элемент
        if bad_xpath(xpath):
            element.text = 'bad'
        else:
            element.text = xpath


#Получить xpath элемента
def get_xpath_of_el(element):
    return element.text


def all_in_screen(e,xpath):
    if (e.text.find('bad') == -1):
        params = json.loads(e.text)
        if (params.get('x') + int(params.get('width')) > 700):
            print(xpath)
            print(params.get('x') + int(params.get('width')))


#Задали урл тестируемой страницы
url = "http://rambler.ru"
#Создали дерево по html-коду страницы
tree = create_tree(url)
#К элементам дерева добавляем их xpath-селекторы
add_xpath(tree)

    #if сhild_сount(e) > 1:
    #    print('Child xpath = ', get_xpath_of_el(e.getchildren()[1]))


driver = webdriver.Firefox()
driver.set_window_size(700, 800)
driver.get("http://rambler.ru/")
for e in tree.iter():
    if (e.text.find('bad') == -1):
        xpath = e.text
        parameters_json = json.dumps(get_parameters_of_element(e))
        e.text = parameters_json
        all_in_screen(e,xpath)
        #if (e.text.find('bad') == -1):
            #print(e.text)


driver = webdriver.Firefox()
driver.set_window_size(1400, 800)
driver.get("http://rambler.ru/")
for e in tree.iter():
    if (e.text.find('bad') == -1):
        xpath = e.text
        parameters_json = json.dumps(get_parameters_of_element(e))
        e.text = parameters_json
        all_in_screen(e,xpath)
        #if (e.text.find('bad') == -1):
            #print(e.text)
