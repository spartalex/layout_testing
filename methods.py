import urllib.request
from lxml import etree
from lxml import html
from selenium import webdriver
import json
from selenium.webdriver.common.action_chains import ActionChains

def all_in_screen(e,xpath):
    if (e.text.find('bad') == -1):
        params = json.loads(e.text)
        if (params.get('x') + int(params.get('width')) > 700):
            print(xpath)
            print(params.get('x') + int(params.get('width')))


#Просто разница между цветами, лучше чтобы было более 500
def col_diff(r1, g1, b1, r2, g2, b2):
    return max(int(r1), int(r2)) - min(int(r1), int(r2)) + max(int(g1), int(g2)) - min(int(g1), int(g2)) \
           + max(int(b1), int(b2)) - min(int(b1), int(b2))


#Отношение яркостей цветов
def bright_diff(r1, g1, b1, r2, g2, b2):
    br1 = (299 * r1 + 587 * g1 + 114 * b1) / 1000
    br2 = (299 * r2 + 587 * g2 + 114 * b2) / 1000
    return abs(br1 - br2)


#Световой контраст
def lumdiff(r1,g1,b1,r2,g2,b2):
    l1 = 0.2126 * pow(r1/255, 2.2) + 0.7152 * pow(g1/255, 2.2) + 0.0722 * pow(b1/255, 2.2)

    l2 = 0.2126 * pow(r2/255, 2.2) + 0.7152 * pow(g2/255, 2.2) + 0.0722 * pow(b2/255, 2.2)

    if(l1 > l2):
        return (l1+0.05) / (l2+0.05)
    else:
        return (l2+0.05) / (l1+0.05)

#250
def pythdiff(r1,r2,b1,b2,g1,g2):
    rd = r1 - r2
    gd = g1 - g2
    bd = b1 - b2
    return sqrt(rd * rd + gd * gd + bd * bd )

#Отдаю список r1,g1,b1,r2,g2,b2
def parse_colors(color, back_color):
    color = color[5:]
    list = []
    list.append(color[:color.find(',')])
    color = color[color.find(',')+1:]
    list.append(color[:color.find(',')])
    color = color[color.find(',')+1:]
    list.append(color[:color.find(',')])

    color = back_color[5:]
    list.append(color[:color.find(',')])
    color = color[color.find(',') + 1:]
    list.append(color[:color.find(',')])
    color = color[color.find(',') + 1:]
    list.append(color[:color.find(',')])
    return list


def colors_check(element):
    colors_list = parse_colors(element.color,element.back_color)
    r1 = colors_list[0]
    g1 = colors_list[1]
    b1 = colors_list[2]
    r2 = colors_list[3]
    g2 = colors_list[4]
    b2 = colors_list[5]
    colour_diff = col_diff(r1, g1, b1, r2, g2, b2)
    if (colour_diff > 500):
        print(element.xpath + 'очень хорошие цвета ' + str(colour_diff))
    else:
        print(element.xpath + 'очень плохие цвета ' + str(colour_diff))









