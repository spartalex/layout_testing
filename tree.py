import urllib.request
from lxml import etree
from lxml import html
from selenium import webdriver
import json
from methods import *


class Web_element:
    def __init__(self, id, x, y, height, width, parent_id, children_ids, xpath, back_color, color, square_num):
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
        self.square_num = square_num


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
    if (e.find('div',-6) != -1) or (e.find('body',-6) != -1):
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


def normalize_parent_id(tr):
    for e in tr:
        if (len(e.children_ids) > 0):
            for el in e.children_ids:
                for elem in tr:
                    if (elem.id == el):
                        elem.parent_id = e.id

def divide_screen(screen_width, screen_height, num_x,num_y,x,y, width, height):
    squares = []
    square_length_x = round(screen_width / num_x)
    square_length_y = round(screen_height / num_y)
    squares.append((x // square_length_x) + 1 + (y // square_length_y) * num_x)
    ostatok_x = squares[0]*square_length_x - x
    ostatok_y = (squares[0]//num_x + 1)*square_length_y - y
    if (width > ostatok_x):
        num_scrs = 1 + (width-ostatok_x)//square_length_x
        for i in range(num_scrs):
            squares.append(squares[0] + i)

    if (height > ostatok_y):
        num_scrs = 1 + (height - ostatok_y)//square_length_y
        for i in range(num_scrs):
            squares.append(squares[0] + i*num_x)

    return squares


def create_my_tree(tree, url, height_scr, width_scr, num_x, num_y):
    driver = webdriver.Firefox()
    driver.set_window_size(height_scr, width_scr)
    driver.get(url)
    driver.save_screenshot('screenie.png')
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
                if not bad_position(x,y,height,width) and element.is_displayed():
                    square_id = divide_screen(width_scr, height_scr, num_x, num_y, x, y, width, height)
                    Web_elements.append(Web_element(id(e), x, y, width, height, id(e.getparent()),
                                                     change_to_id(e.getchildren()), xpath, back_color, color, square_id))
            except:
                pass
    normalize_parent_id(Web_elements)
    return Web_elements



