import urllib.request
from lxml import etree
from lxml import html
from selenium import webdriver
import json
from methods import *


class Web_element:
    def __init__(self, id, x, y, height, width, parent_id, children_ids, xpath, back_color, color):
        self.id = id
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.parent_id = parent_id
        self.children_ids = children_ids
        self.xpath = xpath
        self.back_color = back_color
        self.color = color


#Количество детей у элемента дерева
def сhild_сount(e):
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


def change_to_id(list):
    out = []
    for t in list:
        out.append(id(t))
    return out


def create_my_tree(tree, url, height, width):
    driver = webdriver.Firefox()
    driver.set_window_size(height, width)
    driver.get(url)
    Web_elements = []
    for e in tree.iter():
        #prms = get_parameters_of_element(e)
        if (e.text.find('bad') == -1):# and (isinstance(prms, dict)):
            xpath = e.text
            try:
                element = driver.find_element_by_xpath(get_xpath_of_el(e))
                # Запихнули в словарь нужные параметры отрисованного элемента
                x = element.location['x']
                y = element.location['y']
                height = element.size['height']
                width = element.size['width']
                back_color = element.value_of_css_property('background-color')
                color = element.value_of_css_property('color')
                if not bad_position(x,y,height,width):
                    Web_elements.append(Web_element(id(e), x, y, height, width, id(e.getparent()),
                                                                        change_to_id(e.getchildren()), xpath, back_color, color))
            except:
                pass
    return Web_elements



