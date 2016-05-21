import urllib.request
from lxml import etree
from lxml import html
from selenium import webdriver
import json
from selenium.webdriver.common.action_chains import ActionChains
from tree import *
from bottle import route, run, template, static_file, error, get, post, request


@post('/dom_created')
def do():
    url = request.forms.get('url')
    # Создали дерево по html-коду страницы
    tree = create_tree(url)
    # К элементам дерева добавляем их xpath-селекторы
    add_xpath(tree)
    tr = []
    tr = create_my_tree(tree, url, 1200, 700)

    # for e in tr:
    #    if (e.color != 'transparent') and (e.back_color != 'transparent'):
    #        colors_check(e)
    # print('f')

    return template('dom_created',xpath = tr[3].xpath)

# конроллер возвращает картинку, сохраненную при поиске
@route('/hello/<name>')
def index(name):
    return template('template_main', xpath='xpath')


if __name__ == '__main__':
    run(host='localhost', port=8080)


#print(parse_colors('rgba(12,153,23,3)','rgba(52,25,92,3)'))

#Создали дерево по html-коду страницы
#url = "http://www.zoopicture.ru/"
#Создали дерево по html-коду страницы
#tree = create_tree(url)
#К элементам дерева добавляем их xpath-селекторы
#add_xpath(tree)
#tr = []
#tr = create_my_tree(tree, url, 1200, 700)
#for e in tr:
#    if (e.color != 'transparent') and (e.back_color != 'transparent'):
#        colors_check(e)
#print('f')


