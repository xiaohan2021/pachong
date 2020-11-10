# -*- encoding=UTF-8 -*-

import requests  # http请求
import random
import re
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
    print(9, strc.find('ll'))  # 查找字符

    pass

def demo_operation():
    print(1, 1 + 2, 5 / 2, 5 * 2, 5 - 2)
    print(2, 1 + 2, 5 / 2.0, 5 * 2, 5 - 2)
    print(3, True, not True, not False)
    print(4, 1 << 2, 88 >> 2)
    print(5, 1 < 3, 5 < 3)
    print(6, 5 | 3, 5 & 3, 5 ^ 3)  # 或  与  异或
    x = 3
    y = 5.0
    print(x, y, type(x), type(y))


def demo_buildinfunction():
    print(1, max(2, 1), min(3, 5))
    print(2, len('xxx'), len([5, 2, 3]))
    print(3, abs(-2), abs(7))
    print(4, list(range(1, 10, 2)))
    # print(5, '\n'.join(dir(list)))
    x = 2
    print(x + 3)
    print(6, eval('x * 2 + 3'))  # 自动将字符串转成int
    print(7, chr(65), ord('a'))  # ASCII码和字符的转换
    print(8, divmod(11, 3))  # 做除法  得到商和余数


def demo_controlflow():  # 控制流
    score = 70
    if score > 99:
        print(1, 'A')
    elif score > 60:
        print(2, 'B')
    else:
        print(3, 'C')

    while score < 100:
        print(score)
        score += 10
        if score > 80:
            break

    # for(int i = 0; i < 10, i++){}
    for i in range(0, 10):
        if i == 0:
            pass
        if i == 3:
            continue
        if i < 5:
            print(i * i)
        if i == 7:
            break


def demo_list():  # list集合
    lista = ['a', 2, 3]  # vector<int> ArrayList<Integer> 定义
    print(1, lista)
    # print(dir(list))
    listb = [2, 1, 1.1]  # 数据类型不固定
    print(2, listb)
    lista.extend(listb)  # 拼接字符串
    print(3, lista)
    print(4, len(lista))  # 长度
    print(5, 'a' in lista, 'b' in lista)  # 判断是否存在
    lista = lista + listb  # 拼接
    print(6, lista)
    listb.insert(0, 10)  # 指定位置插入元素
    print(7, listb)
    listb.pop(1)  # 取出，类似出栈
    print(8, listb)
    listb.sort()  # 排序，python3.x中需要保持类型一致
    print(9, listb)
    print(10, listb[1], listb[2])  # 取出指定角标的元素
    print(11, listb * 2)  # 集合扩容  直接复制
    print(12, [0] * 10)
    listb.append('www')  # 集合添加元素
    print(13, listb)
    listb.reverse()  # 反转
    print(14, listb)
    t = (1, 1, 3)  # 元组 不可变的list  应用：(x, y) (width, height)
    print(15, t)
    print(16, t.count(1), len(t))  # 元组中1的个数

def add(a, b):  # 定义函数
    return a + b

def sub(a, b):
    return a - b



def demo_dic():  # 字典数据结构  Key——Value
    dicta = {4: 16, 1: 1, 2: 4, 3: 9, 'a': 'b'}
    print(1, dicta)
    print(2, dicta.keys(), dicta.values())
    for key, value in dicta.items():  # 遍历key 和 value
        print(3, key, value)
    for key in dicta.keys():  # 遍历key
        print(4, key)
    print(5, dicta.__contains__(11), dicta.__contains__(1))  # 是否包含元素

    dictb = {'+': add, '-': sub}  # value可以是方法
    print(6, dictb['+'](1, 2))  # 取出方法后直接调用
    print(7, dictb.get('-')(9, 1))

    print(8, dictb)
    del dictb['+']  # 删除key对应的value
    print(9, dictb)

    dictb.pop('-')  # 弹出key对应的value
    print(10, dictb)

    dictb['x'] = 'y'  # 添加key value
    print(11, dictb)


def demo_set():  # set集合
    lista = [1, 2, 3]  # set的定义不太一样
    seta = set(lista)
    print(1, seta)

    setb = set((2, 3, 4))
    print(2, seta.intersection(setb))  # 取交集
    print(3, seta & setb)  # 取交集
    print(4, seta | setb, seta.union(setb))  # 并集
    print(5, seta - setb, seta.difference(setb), setb - seta)  # 我有你没有的减法
    seta.add('xxx')  # 添加元素
    print(6, seta)
    print(7, len(seta))
    print(8, seta.isdisjoint(set(('a', 'b'))))  # 没有交集为true
    print(9, 1 in seta)  # 是否包含

class User:  # user类
    type = 'USER'
    def __init__(self, name, uid):  # 封装
        self.name = name
        self.uid = uid

    def __repr__(self):  # toString()方法
        return 'im ' + self.name + ' ' + str(self.uid)


class Guest(User):  # 继承
    type = 'GUEST'
    def __repr__(self):  # 多态
        return 'im guest ' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'
    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)  # 多态
        self.group = group

    def __repr__(self):
        return 'im admin ' + self.name + ' ' + str(self.uid) + ' ' + self.group

def create_user(type):  # 工厂模式
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 2, 'g1')
    else:
        return Guest('g1', 3)


def demo_obj():  # 面向对象演示
    user1 = User('jim', 20)
    print(1, user1)
    guest1 = Guest('lily', 23)
    print(2, guest1)
    admin1 = Admin('tom', 22, 'nowcoder')
    print(3, admin1)

    print(4, create_user('USER'))  # 工厂模式创建对象


def demo_exception():  # 异常演示
    try:
        print(2 / 1)
        raise Exception('Raise Error', 'Nowcoder')
    except Exception as e:  # catch
        print('error', e)
    finally:
        print('clean up')


def demo_random():
    # random.seed(1)
    for i in range(0, 5):
        print(1, random.randint(0, 100))
    print(2, int(random.random() * 100))
    print(3, random.choice(range(0, 100, 5)))
    print(4, random.sample(range(0, 100, 10), 4))

    lista = [1, 2, 3, 4, 5]
    random.shuffle(lista)
    print(5, lista)


def demo_regex():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    p2 = re.compile('\d')
    print(1, p1.findall(str))
    print(2, p2.findall(str))

    str = 'a@163.com, b@google.com, c@qq.com, d@qq.com, d@163.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print(3, p3.findall(str))

    str = '<html><h>title</h><body>content</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print(4, p4.findall(str))
    p5 = re.compile('<h>[^<]+</h><body>[^<]+</body>')
    print(5, p5.findall(str))

    str = 'xxx2020-11-10xxxx'
    p6 = re.compile('\d{4}-\d{2}-\d{2}')
    print(6, p6.findall(str))




if __name__ == '__main__':   # main方法，main后回车即可自动生成
    # print('hello world')
    # qiushibaike()
    # demo_string()
    # demo_operation()
    # demo_buildinfunction()
    # demo_controlflow()
    # demo_list()
    # demo_dic()
    # demo_set()
    # demo_obj()
    # demo_exception()
    # demo_random()
    demo_regex()