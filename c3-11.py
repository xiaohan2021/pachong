# -*- encoding=UTF-8 -*-

import requests  # http请求
from bs4 import BeautifulSoup


def qiushibaike():

    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print(div.text.strip())


def demo_string():
    stra = 'hello world'
    print(stra.capitalize())  # 首字母大写
    print(stra.replace('world', 'nowcoder'))  # 替换

    strb = '    \n\rhello nowcoder  \r\n'
    print(0, strb)
    print(1, strb.lstrip())  # 移除左空格
    print(2, strb.rstrip(), 'xx')  # 移除右空格

    strc = 'hello w'
    print(3, strc.startswith('hel'))  # 判断字符串开始
    print(4, strc.endswith('x'))  # 判断字符串结尾
    print(5, stra + strb + strc)  # 字符串拼接
    print(6, len(stra), len(strb), len(strc))
    print(7, '-'.join(['a', 'b', 'c']))  # 通过-拼接字符串
    print(8, strc.split(' '))  # 空格分隔
    pass


if __name__ == '__main__':
    # print('hello world')
    # qiushibaike()
    demo_string()