import time
listNum = [6, 4, 8, 9, 2, 5, 7, 676, 33, 334, 22222]
'''
site-packages\pip\compat\__init__.py", line 75, in console_to_str
    return s.decode('utf_8')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd1 in position 3: invalid continuation byte

'''
# -------------------------------------------------------------------------------------------------------------------------------------------------------
"""
print(time.time())
listNum.sort()
print(time.time())
print(listNum)

# 注意代码缩放的重要性，同级别的放在同一列，语法要求
# 以下以冒泡排序算法示例
nLen = len(listNum)
i = 0
j = 0
temp = 0
print(time.time())
while i < nLen:
    while j < nLen - i - 1:
        if listNum[j] > listNum[j+1]:
            temp = listNum[j+1]
            listNum[j+1] = listNum[j]
            listNum[j] = temp
        j = j + 1
    i = i + 1
print(time.time())
print(listNum)

def myFunc():
    print("hello, myFunc")

# __metaclass__=type表示以下定义的类都是新式类，如没有，则class class():为新式类，class class:为老式类
# class创建的类可以理解为也是一种对象，所以也可以在函数中建立
# type('myclass', (parenclass), {'name':setValua})可以创建父类为parenclass的类，并具有属性setValue()
# 所以type其实就是所有类的父类，此外，python中的整数，字符串，函数，类都是对象，所以如"hello".count('e')
# 的使用是正确的，这些对象都是由type创建的
# 也可以指定元类__metaclass__=mytype，mytype从type继承而来，可以在其中增加一些属性，这样通过mytype创建的类
# 也就拥有了这些属性，可以单独在某个class中定义__metaclass__属性，这样这个属性就只影响到这个类
__metaclass__=type
# myClass中代码被定义在类命名空间内
class myclass:
    # 构造函数
    def __init__(seft):
        seft.nMember = 0
    # 析构函数
    def __del__(): pass
    # 方法中有seft参数，而函数中没有，这就是方法与函数的区别，seft会绑定到实例上
    def setValue(seft):
        pass
    def getValue(seft):
        return seft.name
    # __双下划线开头的方法外部无法访问
    def  __privateFunc(seft):
        print("this is private func")
        type("type")
    def getSomeMsg(seft):
        seft. __privateFunc()
    # 单下划线开头的函数不会被import导入
    def  _noImportFunc():
        print("this func can't imported")

x = myclass()
x.name = 'hello'
print (x.name)
print (x.getValue())
print (myclass.getValue(x))

y = myFunc
y()
z = x.getValue
print(z())

# x._privateFunc()
x.getSomeMsg()
# 但通过以下这种隐秘的方式却是可以访问私有方法
x._myclass__privateFunc()

def myfunc2(*args):
    return [1, 2, 3, 4]

# 可以先对函数的返回值进行操作后再赋值给变量
y = myfunc2()[0:2]
# 组装成元组形式的入参
y = myfunc2(*(1,2,3))
# 组装成字典形式的入参
y = myfunc2(**{'a':1, 'b':2})

# 特性的改变只会体现在实例的成员上面
x.nMember = 1
x1 = myclass()
print(repr(x.nMember)+";"+repr(x1.nMember))

# 指定myClass为超类
class subClass(myclass):
    # 新式类构造函数中调用super方法，可以使用超类中的特性__init__
    def __init__(seft):
        super(myclass, seft).__init__()
    
    # 直接调用父类的构造函数初始化，支持老式类
    #def __init__():
    #    myclass.__init__()
    # 重写超类中的方法
    def setValue(seft):
        ""
x2 = subClass()
# 使用超类中的方法
print(x2.setValue())
# 查看是否为该子类的超类
print(issubclass(subClass, myclass))
# 查看所有基类
print(subClass.__bases__)
# 查看所属的直接类
print(subClass.__class__)
print(isinstance(x2, myclass))

class myClass1:
    def __init__(self):
        self.width = 0
        self.height = 0
    def talk():
        ""
    def setValue(self, size):
        # 这种赋值方式为元组赋值，与width, height单独赋值是不一样的
        self.width, self.height = size
    def getValue(self):
        return self.width, self.height

    # property如果没有参数，那么size将不可以读写，property是隐藏方法的一种方式
    size = property(getValue, setValue)

x = myClass1()
x.width = 1
x.height = 2
print("get size:")

# 其实是调用property对象中的getValue函数
print(x.size)

# 其实是调用property对象中的setValue函数
print("set size:")
x.size = 3, 4
print(x.width)

class myClass11:
    def __init__(self):
        self.width = 0
        self.height = 0

    # 特殊方法中实现特性的赋值，所以类似于x.name = value
    # 这样的特性操作就得先经过__setattr__方法，而不是直接的赋值
    # 特殊方法就是在特定操作下自动被调用的方法，如=赋值操作
    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            # 如果使用self.name = value,将会再次调用__setattr__，这样会
            # 出现死循环
            self.__dict__[name] = value

    # 这个也会拦截对象的__dict__特性，这时可以使用super函数使用超类
    # 中的__getattr__方法
    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError

    def __delattr__(self, name): pass

x = myClass11()
# 其实是调用特殊方法__setattr__
print("set size by __setattr__:")
x.size = 3, 4
print(x.width)

print("get size by __getattr__:")
# 其实是调用特殊方法__getattr__
print(x.size)

# 同时继承于两个类
class ssubClass(myclass, myClass1):
    ""
x3 = ssubClass()
# 使用的是第一个继承的myclass类中方法
x3.setValue()
# 检查对象是否有指定特性
print(hasattr(x3, 'setValue'))
# 获取特性
print(getattr(x3, "setValue", ''))
# 设置对象的特性并赋值
setattr(x3, 'name', 'Mike')
# 查看对象有哪些特性
print(x3.__dict__)

# 抛出了异常类的实例
#raise Exception

# 导入异常模块， 找不到模块。。。内建异常有SyntaxError等
#import exceptions

# 自定义继承于Exception的异常类
class myException(Exception):
    pass

class myclass3:
    def func():
        # 发生异常并自定义捕捉异常类型
        try :
            1/0
       # 捕捉并打印异常对象，如果没有捕捉异常，则异常传播至函数被调用的地方
       # 如果都没有捕捉异常的地方，则会传播至全局区域，这时如果也没有捕捉，
       # 则程序中止，相比if判断，效率高些，因为判断条件中要执行完语句才知道结果
        except (ZeroDivisionError) as e:
            print("catch the Exeption")
            print(e)
    
            # 重新抛出异常
            raise
        except TypeError: pass

        # 捕捉两种类型的异常
        except(ZeroDivisionError, TypeError): pass

        # 捕捉所有Exception异常,但不建议那么做，无法预知具体的异常错误
        except Exception as e: pass

        # 如果没捕捉到异常，则可以执行一些自定义操作
        else: pass

        # 不管是否抛出异常，都会执行finally中的语句，但在finally中引发的异常却是无法被捕捉到的
        finally: pass

# myclass3.func()

def checkIndex(key):
    if not isinstance(key, (int)): raise TypeError
    if key < 0 : raise IndexError

# __双下划线开头的为特殊函数
class myList:
    def __init__(self, start = 0, step = 1):
        self.start = start
        self.step = step
        self.changed = {}
    
    def __getitem__(seft, key):
        checkIndex(key)

        try: return seft.changed[key]
        except KeyError:
            return seft.start + key*seft.step
    
    def __setitem__(seft, key, value):
        checkIndex(key)

        seft.changed[key] = value

s = myList(1,2)

# s[4]调用了类中的特殊函数__getitem__
print(s[4])

# 继承list类并重写__init__与__getitem__方法，带有计数功能
class myList2(list):
    def __init__(seft, *args):
        super(myList2, seft).__init__(*args)
        seft.counter = 0
    def __getitem__(seft, index):
        seft.counter += 1
        return super(myList2, seft).__getitem__(index)

# 这样对象的用法就如同调用普通的函数一样，如x = list("hello")
x = myList2("hello")
print(x)
print(x[2])

class myClass4:
    # 指定该方法为静态方法，可以直接使用类调用
    @staticmethod
    def staticFunc(): print("this is a static func")
    
    # 指定该方法为类方法，且cls参数会自动绑定到当前类上，
    # 所以可以直接只用类调用，当然也可以使用类实例调用
    @classmethod
    def classFunc(cls): print("this is a class func")

myClass4.staticFunc()
myClass4.classFunc()
x = myClass4()
x.staticFunc()

# 由于对象中实现了__next__与__iter__方法，所以
# 该对象可像列表那样在for循环中迭代使用，该对象
# 也可称为迭代器，当__next__无返回值时，将引发StopIteration异常
# 迭代器就是使用__next__函数时才会计算值并返回，这就是迭代器的优势，
# 只有迭代时才会计算生成值
class myIter:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self

iter1 = myIter()

# in iter时，对象实例调用了__iter__方法，返回对象实例本身
# 继而再调用__next__函数，把返回的结果赋值于i
for i in iter1:
    if i > 100:
        print(i)
        break

# 获取list对象的迭代器
iter2 = iter([1, 2, 3])
next(iter2)

class myIter2:
    value = 0    
    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value
        return self.value
    def __iter__(self):
        return self

iter3 = myIter2()

# list对象的构造函数可以将迭代器转换成列表
print(list(iter3))

nested = [[1,2], [3,4], [5,6,7]]

# 函数中包含有yield语句的则该函数称为生成器，
# yield语句会使函数冻结暂停，返回一个迭代器等待被激活后从暂停
# 点开始继续执行
def myGenerator(listParam):
    for sublist in listParam:
        for element in sublist:
            # 第一次被挂起后，再次激活运行后yield才会返回值，其实是外部通过
            # send方法发送给生成器的值
            yield element

for element in myGenerator(nested):
    print(element)

# 生成器推导式，返回一个生成器
creator = (i for i in range(5, 10))
print(next(creator))

# 可以这样使用生成器，无需多一对圆括号
sum(i for i in range(5, 10))

nested = [[1,2], [3,4,[33,44]], [5,6,7]]

# 使用递归生成器能处理嵌套层数不固定的序列，但要是被迭代元素为
# 字符串时，将导致无限递归，因为字符串就是队列，for i in永远不会引发
# 异常
def myGenerator2(listParam):
    try:
        for sublist in listParam:
            # 以上for in试图迭代一个非序列对象时，引发异常，捕捉并返回迭代器，
            # 进而给element赋值，然后被使用于yield语句中
            for element in myGenerator2(sublist):
                yield element
    except TypeError:
        yield listParam

for element in myGenerator2(nested):
    print(element)


nested = ['h', ['e', 'llo']]
def myGenerator3(listParam):
    try:
        # 迭代字符串时，加入检查机制，如果为字符串，则直接产生元素
        # 这样不会导致无穷递归
        try: listParam + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in listParam:
            # 试图迭代一个非序列对象时，引发异常，捕捉并产生元素 
            for element in myGenerator3(sublist):
                yield element
    except TypeError:
        yield listParam

for element in myGenerator3(nested):
    print(element)
print(list(myGenerator3(nested)))

def myGenerator4(value):
    while(True):
        new = (yield value)
        if new is not None: value = new

x = myGenerator4(1)
# next方法被调用后，yield返回None
print(next(x))

# 再次使用时，传给生成器的参数变成了None，
# send方法会在生成器挂起后发送数据给生成器的yield表达式
# 激活生成器，生成器挂起后才能使用send方法
print(x.send('hello'))

# 以下并不是真正的生成器，由于可以像访问生成器那样
# 对其迭代进行访问，所以也叫模拟生成器
def myGenerator4(listParam):
    result = []
    try:
        try: listParam + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in listParam:
            for element in myGenerator3(sublist):
                result.append(element)
    except TypeError:
        result.append(listParam)
    return result

for element in myGenerator4(nested):
    print(element)

# n*n棋盘，同行同列同对角线不能放置同一*符号，已知前n-1位置，求第n个可能的位置
# ------------
# |   | * |   |   |
# ------------
# |   |   |   | * |
# ------------
# | * |   |   |   |
# ------------
# |   |   |    |   |   pos:?
# ------------

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

def symbols(num, state):
    if len(state) == num -1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos
pos = list(symbols(4, (1,3,0)))
print(pos)

# 递归实现符号位置摆放方案，可针对任意n*n棋盘
def symbols2(num, state = ()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num -1:
                yield (pos,)
            else:
                    for result in symbols2(num, state + (pos,)):
                        yield (pos,) + result
allPos = list(symbols2(4))
print(allPos)

# 整理下输出结果
def formatPrint(solution):
    def line(pos, length = len(solution)):
        return '. ' * (pos) + 'X' + '. ' * (length - pos - 1)
    for pos in solution:
        print (line(pos))

import random
print(formatPrint(random.choice(list(symbols2(4)))))
print(formatPrint(random.choice(list(symbols2(8)))))

import sys

# os也是标准库中常用的模块
import os

# environ获取环境变量
print(os.environ["USERNAME"])

# system用于执行外部程序，注意目录是""引起来的，这样不会被当作程序来运行
# 而使用startfile不用双引号
# os.system(r'D:\"Program Files (x86)"\"KuGou"\"KGMusic"\KuGou.exe')
# os.startfile(r'D:\Program Files (x86)\KuGou\KGMusic\KuGou.exe')
print(os.pathsep)

import webbrowser
# 可以这样打开网址
# webbrowser.open("http://www.baidu.com")

# 加载模块所在路径后，就可以直接导入该路径下的模块了，
# 模块名就是文件名
sys.path.append('../..')

# sys模块还有其他有用的特性，如exit，可以退出当前程序
# argv获取运行脚本时附带在脚本名称后面的参数
print(sys.path)
import pprint
# 智能打印，包括对list对象的换行打印
pprint.pprint(sys.path)
import test1
 # 使用模块的特性
print(test1.test)

# 查找模块所在位置
print(test1.__file__)

# 在交互器中使用help函数可以查看模块的特性信息
# help(test1.test)

# 重复导入的效果与一次导入的效果是相同的，
# 所以两个模块可以互相导入
import test1

# 内置的dir函数可以查看模块中有哪些特性
print([n for n in dir(test1) if not n.startswith('__')])


# 表示当前.py程序要是在主程序中运行，则执行相应的操作
if __name__ == '__main__': print('hello main')

# 可以将模块放在编译器默认查找模块路径的目录下，这样可以直接导入，如site-packages目录
# 也可以设定系统环境变量并设置路径，编译器会去该路径下寻找模块
import easy_install

# 导入包，包名其实就是目录名，该目录下必须包含__init__.py文件
import mypacket
# 可以直接使用包中__init__模块的特性
print(mypacket.x)

# 导入包中其他模块
import mypacket.test

import fileinput

# fileinput模块的input函数可以在解释器中读取.py脚本名称后的参数指定的文件，读取完一个文件后
# 继续读取下一个文件，也可以nextfile自动切换到下一个文件
# inplace=True原地替换模式，所以请慎用
#for line in fileinput.input(inplace=True):
#    print(line)

# 集合{1,2,4...}，有数学中常见的操作，如求并集，比较大小等
a = set([1,2,3])
b = set([3,4])
print(a >= b)
# union与|运算符等效
print(a.union(b))
print(a|b)
c = a & b
print(c.issubset(a))
print(a.union(b))
print(a-b)

# 集合不能添加可变值，但可以使用frozenset添加其他集合
# 已有的元素不会被添加进去
a.add(6)
a.add(frozenset(b))
print(sorted(a))

from functools import reduce
# 可以求多个集合的并集
x = reduce(set.union, [{1,2,3},{3,4}, {3,4,5}])
print(x)

from heapq import *
from random import shuffle
data = [1,2,3,4,5]
# 打乱队列元素顺序
shuffle(data)
heap = []
for n in data:
    # heappush建立了堆，也可以使用heapify建立
    heappush(heap, n)
print(heap)

# 入堆时，堆算法内部会自动把最小的数排序在第一位
heappush(heap, 0.1)
print(heap)

# heappop弹出最小的元素
print(heappop(heap))
print(heappop(heap))

# 弹出最小的元素后插入新的元素
x=[0,1,2]
heapreplace(x, 0.5)
print(x)
heapreplace(x, 3)
print(x)

y=[3,1,2]
# 升序排序后返回堆前三个元素，比sorted函数效率更高
n = nlargest(3, y)
print(n)

# 降序排序后返回堆前两个元素
n = nsmallest(2, y)
print(n)

from collections import deque
# 建立一个双端队列，可在列头或列尾增减元素
q = deque(range(5))
q.append(5)
q.appendleft(6)
print(q)
print(q[0])
q.pop()
q.popleft()
# 整体往右移动三位
q.rotate(3)
print(q)
# 在右侧扩展队列
q.extend([6,7])
print(q)


# 时间模块
import time

# (2018, 9, 20, 21, 31, 0, 30, 0) 对应年月日时分秒周天夏令时
print(time.mktime((2018, 9, 20, 21, 31, 30, 3, 30, 0)))

# 时间元组转换成字符串
print(time.asctime())

# 将秒数转换为日期元组
print(time.localtime())

# 等待三秒钟后继续执行
# time.sleep(3)

# 获取全球统一标准时间
uniTime = time.gmtime()
print(uniTime)
print(uniTime[0])

from timeit import timeit
# 计算代码运行所需时间
timeit('x=range(10)')

# 随机数模块
import random

# 返回三位二进制后转换成长整型
print(random.getrandbits(3))

# 获取0-1之间的伪随机数
print(random.random())

# 获取1到5之间的随机实数
print(random.uniform(1,5))

# 返回range中的随意数
print(random.randrange(1,10))

# 返回序列中的的随意元素
print(random.choice([1,2,3,4,5]))

# 打乱序列
a = [1,2,3,4,5]
random.shuffle(a)
print(a)

# 从序列中随机返回n个元素
print(random.sample([1, 1, 2, 2, 3, 3, 4, 5], 2))


# 例子，可以这样来理解，抛三枚骰子后，求骰子朝上的面的点数的总和
sum = 0
for i in range(3): sum += random.randrange(6) + 1
print(sum)

# 建立 一副扑克牌并随机打乱顺序
digital = list(range(2,11)) + 'J Q K A'.split()
shape = "♠ ♥ ♣ ♦".split()  

poker = ['%s%s' % (s, d) for s in shape for d in digital]
#poker.append('♔ ♕'.split())
poker.extend('♔ ♕'.split())
random.shuffle(poker)

from pprint import pprint
pprint(poker[:12])

#while poker:
#    tmp = input("get poker:")
#    x = poker.pop();
#    print(x)

# shelve模块提供一种简单的数据存储方案，可以把数据存储在dat二进制文件中
import shelve
# open方法:如果文件不存在，会创建test1.py.dat文件，返回一个shelf对象
f = shelve.open('mypacket/test1.py')
# 返回的对象可以当做字典一样使用，这里把数据存储到了dat文件中
f['x'] = [1,2]
# 这里的对象与普通字典不一样，append方法其实是把数据添加到副本中
# 所以f['x']并没有被改变
f['x'].append(3)
print(f['x'])

# 可以通过重新赋值达到append的效果
temp = f['x']
temp.append(3)
f['x'] = temp
print(f['x'])

# 存取完数据后close对象，不然之后的操作可能会损坏已经存取的数据，下次读取的
# 时候可能读取不了
f.close()

f = shelve.open('mypacket/test1.py')
# 再次打开存储文件的时候，可以访问到之前存储过的内容
print(f['x'])
# 试图访问对象不存在的key时，会出错
# print(f['y'])
f.close()

# 正则表达式模块
import re
# 会在开头匹配，匹配到则返回match对象，否则返回None
# 首先会把'h'转换成re匹配对象，再去匹配，search也会经过这样的
# 的转换
print(re.match('h', 'hello'))
# 转换成re匹配对象，使用其匹配效率会更高
x = re.compile('he')
print(x.match('hello'))

print(re.match('e', 'hello'))
# ? 可选项，匹配有的或是没有的
print(re.match('e?', 'hello'))
# 会从开始到结尾匹配，找到第一个符合的就返回
print(re.search('e', 'hello'))

text = "hello... wo-rld! are you ok"
# 以指定模式分割字符串，[]集合匹配，+匹配1到多个，匹配集合中的单个字符，'.'为通配符
x = re.split('[. ]+', text)
print(x)
# 位于集合匹配中的^符号是非的意思
x = re.findall('[^h]+', text)
print(x)
# ()子模式匹配，'wo'两边会被分割开来，但'o'会出现在分割后的列表中
x = re.split('w(o)', text)
print(x)
# 返回的是()组中的内容，| 管道可以匹配两个
print(re.findall('a(rr|re)', text))

# 以列表形式返回所有匹配到的项，返回组0，即所有匹配到的项
print(re.findall('[a-z]+', text))
# \反斜杠转义了正则表达式中的'-'符号，使其不会当作范围字符来处理
print(re.findall('[.\-!]+', text))

# 字符串中把匹配模式的pat替换成指定字符
pat = 'ok'
print(re.sub(pat, 'sure', text))

# 把字符串中的所有正则表达式字符进行转义，如. ? - 等
print(re.escape(text))
x = re.search('(ar.)', text)
# 返回匹配模式对象中的第1个匹配组
# 位于匹配模式中()内的内容就是匹配组的内容
# 如果没有()，默认匹配到的所有字符就是组的内容，即组0
print(x.group(1))
# 返回第一个匹配组匹配项的开始索引
print(x.start(1))
# 返回第一个匹配组匹配项的结束索引
print(x.end(1))
# 有了re.VERBOSE参数，就可以在匹配模式中添加注释了，这样不会当作
# 匹配模式的一部分去匹配
print(re.search('\- # 转义"-"符号', text, re.VERBOSE))

# \1将使用匹配组1([^\*]+)匹配到的内容进行替换
print(re.sub('\*([^\*]+)\*', r'<html>\1</html>', 'hello *world*!'))
# .+把中间的星号也当作任意字符来对待了，直到遇到最后的*为止，这是贪婪匹配
print(re.sub('\*(.+)\*', r'<html>\1</html>', 'hello *wo**rld*!'))
# .+? 加个?，只要遇到符合匹配的就匹配一个，接着再继续匹配，这是非贪婪匹配
print(re.sub('\*(.+?)\*', r'<html>\1</html>', 'hello *wo**rld*!'))

import fileinput
# 例子，查找文件中所有type的值，使用.*?非贪婪匹配
# 这样找到第一个符合匹配的就返回，而不是忽略中间的'type'继续匹配到最后一个'type'
pat = re.compile('.*?type="(.*?)"( |>)')
for line in fileinput.input():
    result = pat.search(line)
    if result: print(result.group(1))

# 查找获取不重复的数据
pat = re.compile('.*?type="(.*?)"')
typeset = set()
for line in fileinput.input():
    for result in pat.findall(line):
        typeset.add(result)
print(sorted(typeset))

# 模板填充变量，定义:[name="Mike"]， 模板:hello, [name]->hello, Mike
# 可以接收两个文件，一个是模板变量定义文件，一个是模板文件
pat = re.compile('\[(.+?)\]')
# 把变量收集到该作用域
scope = {}
def replacement(match):
    code = match.group(1)
    try:
        # 如果作用域中定义了变量，则计算值并返回
        return str(eval(code, scope))
    except SyntaxError:
        # python 2.0写法
        # exec(code) in scope
        # python 3.0写法
        # 在作用域中计算如"name='mike'",
        exec(code, scope)
        return ''

# 文件内容全部存于一个字符串中
lines = []
for line in fileinput.input():
    lines.append(line)
# 转换成字符串
text = ''.join(lines)

# 每匹配到一个，就把匹配到的内容作为参数调用replacement函数，
# 用函数返回的值替换匹配到的项
print(pat.sub(replacement, text))

# open方法返回一个文件流对象，此方法不会自动创建文件，参数默认是'r'
f = open(r'myfile\template.txt')
# 从文件开头读取三个字节长度的内容，并记录读取到的位置
f.read(3)
# 从上一次读取到的位置继续读取
f.read(2)
# 移动到文件流第二个字节
f.seek(2)
# 确定不再使用文件流的时候应该手动调用close方法关闭文件
# close后才会解除其他程序对文件的访问限制
# 虽然程序退出的时候也会自动关闭，但可能因为某些情况
# 如程序崩溃可能会导致无法正确地保存文件，
f.close()
f = open(r'myfile\template.txt')
# 读取文件所有内容，读到文件尾时，返回空字符串
print(f.read())
f.close()
f = open(r'myfile\template.txt')
# 读取一行
f.readline()
# 从上次读取到的行后位置继续读取新行
f.readline()
f.close()
f = open(r'myfile\template.txt')
# 返回一个列表，列表中的每一项对应文件每一行的内容,
# 包括行尾的换行符\n
f.readlines()
f.close()
# 指定w参数可以向文件中写入内容
f = open(r'myfile\template.txt', 'w')
# \n是换行符
f.write('how are you\nfine, thanks\n')
f.close()
f = open(r'myfile\template.txt', 'w')
# 按行写入，接受列表传参
f.writelines(['so late!\n', 'maybe we can walk faster'])
f.close()

# 以二进制方式读取文件，读取声音等二进制文件的时候需要，而且不会把文件中
# 换行解释成换行符
f = open(r'myfile\template.txt', 'rb')
print(f.read())

# with语句结束后会自动关闭文件，即使发生异常也会关闭
with open(r'myfile\template.txt') as f:
    f.read()

def process(str):
    print("process...."+str)

f = open(r'myfile\template.txt')
# 在循环读取文件的过程中，可以针对读取到的每一项内容进行自定义处理
#while True:
#    char = f.read(1)
#    if not char: break
#    process(char)
#f.close()
while True:
    line = f.readline()
    if not line: break
    process(line)
f.close()

#f = open(r'myfile\template.txt')
#for char in f.read():
#    process(char)
#f.close()
 
# 每次只读取一行如readline函数，这种叫做懒惰行迭代，只读取需要的行
import fileinput
for line in fileinput.input(r'myfile\template.txt'):
    process(line)

# 可以直接对文件流进行迭代，但在程序关闭的时候才能close文件
for line in open(r'myfile\template.txt'):
    process(line)
 
# 对标准输入进行迭代
#import sys
#for line in sys.stdin:
#	print("new line"+line)

# 把文件流转换成列表
lines = list(open(r'myfile\template.txt'))
print(lines)

# 文件流赋值给多变量时，就相当于把文件每一行赋值给单独的变量
f, s = open(r'myfile\template.txt')
print(f)
print(s)

# 流行GUI库wxPython，还有其他GUI库如Tkinter(python标准库自带)，AWT、Swing(两者都是在Jython环境中使用)
import wx
app = wx.App()
# None 表示不需要父部件作为构造函数的参数来创建窗口(Frame)
win = wx.Frame(None, title = '文本编辑器', pos = (660, 390), size = (435, 500))
# 在Frame上增加控件
# 可以设置每个按钮的大小，风格
# 如果只有一个按钮，设置位置及大小将无效，以下是固定设置控件的尺寸，
# 并不会随窗口大小而变化
#btnOpen = wx.Button(win, label = '打开', pos = (255, 5), size = (80,25))
#btnSave = wx.Button(win, label = '保存', pos = (335, 5), size = (80,25))
#textInput = wx.TextCtrl(win, pos = (5,5), size = (250, 25))
## 指定了style风格后，文本框转换成文本区
#contextText = wx.TextCtrl(win, pos = (5, 35), size = (410, 425), style = wx.TE_MULTILINE | wx.HSCROLL)

def load(event):
     f = open(textInput.GetValue())
     contextText.SetValue(f.read())
     f.close()
        
def save(event):
    f = open(textInput.GetValue(), 'w')
    f.write(contextText.GetValue())
    f.close

def eraseBackground(event):
     dc = event.GetDC()
     if not dc:
         dc = wx.ClientDC(contextText)
         rect = contextText.GetUpdateRegion().GetBox()
         dc.SetClippingRect(rect)
     dc.Clear()
     bmp = wx.Bitmap(r"E:\picture\fire.jpg")
     dc.DrawBitmap(bmp, 0, 0)

# 以下以相对大小设置控件尺寸
# 控件都放在一个面板上
bkg = wx.Panel(win)
btnOpen = wx.Button(bkg, label = '打开')
# 把打开文件函数绑定到点击按钮事件上
btnOpen.Bind(wx.EVT_BUTTON, load)
btnSave = wx.Button(bkg, label = '保存')
btnSave.Bind(wx.EVT_BUTTON, save)
textInput = wx.TextCtrl(bkg)
contextText = wx.TextCtrl(bkg, style = wx.TE_MULTILINE | wx.HSCROLL)
contextText.SetBackgroundColour("LIGHT GREY")
#contextText.Bind(wx.EVT_ERASE_BACKGROUND, eraseBackground)

# 尺寸控制器，默认水平布局
hbox = wx.BoxSizer()
# 以下控件设置的水平空间占用比例为1:0:0，当然比例也调整成其他如3:2:1
hbox.Add(textInput, proportion = 1, flag = wx.EXPAND)
# 设置左边距为5
hbox.Add(btnOpen, proportion = 0, flag = wx.LEFT, border = 5)
hbox.Add(btnSave, proportion = 0, flag = wx.LEFT, border = 5)

# 垂直布局尺寸器，尺寸器中也可以把其他的尺寸器添加进来，形成多层次布局
vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
vbox.Add(contextText, proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)

# 设置面板尺寸控制器
bkg.SetSizer(vbox)

# 窗口只有Show才会展示，不然会隐藏
win.Show()
app.MainLoop()

# sqlite数据库模块
import sqlite3
# 会创建一个数据库db文件
conn = sqlite3.connect('myfile/mysqlitedb.db')
# 游标
curs = conn.cursor()
#curs.execute(
#    CREATE TABLE fruit
#    (
#        id INTEGER primary key,
#        name TEXT,
#        desc TEXT
#    )
#
#    )

insertSql = "insert into fruit values(?,?,?)"
querySql = "select id, name, desc from fruit"
# 从文件中读取数据并插入数据库文件中
#for line in open('myfile/fruit.txt'):
# fields = line.split(',')
# vals = [v for v in fields]
# curs.execute(insertSql, vals)
#curs.execute(insertSql, [2, 'watermelon', 'contain a lot of moisture'])
# 插入不同的数据类型，如Time,Date等
#curs.execute(insertSql, [sqlite3.Time(1,2,3), '', 'contain a lot of moisture'])
curs.execute(querySql)
# fetchall获取所有行，还有rowcount，description等操作
for row in curs.fetchall():
    print(row)
conn.commit()
conn.close()

# 网络编程套接字模块
import socket
# 建立一个服务端套接字，建立套接字->绑定地址->监听连接->等待连接
server = socket.socket()
host  = socket.gethostname()
port = 1025
# 绑定的地址格式为元组
server.bind((host, port))
# 最多同时监听5个连接
server.listen(5)
while True:
    # accept接收连接请求之前会阻塞
    client, addrClt = server.accept()
    print('Got connection from ',addrClt)
    client.send(b'Thanks for connecting')
    client.close()
    
#client = socket.socket()
#host  = socket.gethostname()
#port = 1025
#client.connect((host, port))
## 一次最多可接收1024个字节的内容
#print(client.recv(1024))

# python3中urllib是一个包，urlopen位于包的request模块中
from urllib.request import urlopen
# 也可以open本地文件
# 返回类文件对象
webpage = urlopen('https://www.python.org/')
# 可以把返回的页面当作文件一样读取
text = webpage.read()
# 如果存在中文，则按utf-8格式解码
text = text.decode('utf-8')

import re
#s = '<a href="http://map.baidu.com" name="tj_trmap" class="mnav">地图</a>'
rerult = re.search('<a href="(.*?)" .*?>about</a>', text, re.IGNORECASE)
print(rerult.group(1))

from urllib.request import urlretrieve
from urllib.request import quote
# 获取网页文件并保存到本地，没有指定文件名时，保存在临时目录，使用
# urlcleanup可以清除临时目录中的文件
urlretrieve('https://www.python.org/', 'myfile/python.html')
# quote会把url中的特殊字符转换成对url友好的字符后再返回url
# 如会把~转换成%7E，unquote功能则相反
webpage = urlopen(quote('https://www.~myurl.org/'))

from urllib.parse import urlencode
# 返回param1=test&amp;param2=%c%de类似的字符串
# 这些字符串可以在url中当作参数，如服务器cgi脚本是用
# python编写的，则可通过cgi模块的getvalue方法获取到参数
print(urlencode({'param1':'test', 'param2':'你好'}))

# 导入基础网络服务器框架socketserver，包含TCP,UDP类等
from socketserver import TCPServer, StreamRequestHandler, ThreadingMixIn

# 使用线程处理，每来自一个请求，开启一个线程来处理，
# 也可以采用分叉进程来处理，就是开启多个进程，但在windows中不支持
class Server(ThreadingMixIn, TCPServer): pass

# 继承于StreamRequestHandler类
class Handler(StreamRequestHandler):
    # 重写StreamRequestHandler类中handle处理函数
    def handle(self):
        addr = self.request.getpeername()
        print('the connection from ', addr)
        self.wfile.write(b'hello')

#server = TCPServer(('', 1025), Handler)
# 把端口号与自定义处理类作为构造函数的参数
server = Server(('', 1025), Handler)
server.serve_forever()

import socket, select
s = socket.socket()
s.bind((socket.gethostname(), 1025))
s.listen(5)
inputs = [s]
# 结合select 模块实现响应多个连接
while True:
    # 找出准备好读写的套接字，这样就是处理多个连接了，实现异步socket，select的第四个参数为等待连接的超时时间，为0则不会阻塞
    # 返回的元组的第一个元素是输入文件描述符序列
    # select会监听inputs的状态
    # 给每一个连接分配一个时间片段，这点不同于多线程的同时处理，不会出现多线程中的同步问题
    rs, ws, es = select.select(inputs, [], [], 0)
    for r in rs:
        # 有新客户端请求连接
        if r is s:
            c, addr = s.accept()
            print('connection from ', addr)
            inputs.append(c)
        else:
             try:
                 data = r.recv(1024)
                 disconnected = not data
             except socket.error:
                 disconnected = True
             if disconnected:
                 print(r.getpeername(), 'disconnected')
                 inputs.remove(r)
             else:
                print(data)

import socket, select
s = socket.socket()
s.bind((socket.gethostname(), 1025))

fmap = {s.fileno():s}

s.listen(5)
# 使用poll方法实现接收多个请求连接
# 返回一个poll对象
p = select.poll()
# 注册一个对象得到其文件描述符
p.register(s)
while True:
    events = p.poll()
    # 获取对象的状态，包括其文件描述符，在对象上发生的事件
    for fd, event in events:
        # 有新客户端请求连接
        if fd in fmap:
            c, addr = s.accept()
            print('connection from ', addr)
            p.register(c)
            # 把客户端的socket对象也注册
            fmap[c.fileno()] = c
        elif event & select.POLLINT:
            data = fmap[fd].recv(1024)
            if not data:
                print(fmap[fd].getpeername(), 'disconnected')
                p.unregister(fd)
                del fmap[fd]
        else:
            print(data)

# 使用twisted的简单网络服务器， 这是基于事件处理的网络编程框架
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.protocols.basic import LineReceiver

# 继承于Protocol类
class MyLogger(Protocol):
    # 重写Protocol类的函数，有客户端连接时自动被调用
    def connectionMade(self):
        print ('connection from ', self.transport.client)
    # 客户端断开连接时自动被调用
    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')
    # 接收到客户端数据自动被调用，可能一行只显示一个字符
    def dataReceived(self, data):
        print(data)

# 协议对象工厂
factory = Factory()
# 自定义处理协议，但也可以默认使用工厂中默认的协议
factory.protocol = MyLogger
reactor.listenTCP(1025, factory)
# 启动服务器
reactor.run()

# 继承于LineReceiver类
class MyLogger(LineReceiver):
    def connectionMade(self):
        print ('connection from ', self.transport.client)

    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')

    # 可以接收到完整的行，而不是每一个字符占一行
    def lineReceived(self, line):
        print(line)

factory = Factory()
factory.protocol = MyLogger
reactor.listenTCP(1025, factory)
reactor.run()

from subprocess import Popen, PIPE
text = open('myfile/test.html', 'rb').read()
# 使用subprocess打开tidy,tidy可以用来修复不规范的html文件(如标签没有正确结束)，以便利于解析
tidy = Popen('tidy', stdin = PIPE, stdout = PIPE, stderr = PIPE, shell = True)
tidy.stdin.write(text)
# 以下实际中不会输出数据
tidy.stdout.read()

from urllib.request import urlopen
from HTMLParser import HTMLParser

class Scraper(HTMLParser):
    in_li =False
    in_data = False
    # 找到开始标签时自动调用
    # attr由（键，值）组成的列表
    def handle_startstag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'li':
            self.in_li = True
        if tag == 'li' and 'data-title' in attrs:
            self.in_data = True
            self.chuncks = []

    # 使用文本数据时自动调用
    def handle_data(self, data):
        if self.in_data:
            self.chuncks.append(data)

    # 找到结束标签时自动调用
    def handle_endtag(self, tag):
        if tag == 'li':
            self.in_li = False
        if tag == 'li':
            if self.in_li and self.in_data:
                print('%s' % ''.join(self.chuncks))

text = urlopen('https://movie.douban.com/').read()
parser = Scraper()
parser.feed(repr(text))
parser.close()
from urllib.request import urlopen
import re
exp1 = re.compile(r'<li class="ui-slide-item"  data-title="(.*?)" data-release=".*?"')
exp2 = re.compile(r'<li class="title">.*?<a.*?>(.*?)</a>.*?</li>')
text = urlopen('https://movie.douban.com/').read()
text = text.decode('utf-8')
movie = set()
for name in exp1.findall(text):
    movie.add(name)

for name in exp2.findall(text):
    movie.add(name)

print(movie)

from urllib.request import urlopen
from bs4 import BeautifulSoup

text = urlopen('https://movie.douban.com/').read()
# Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码，所以不需要手动转换格式
#text = text.decode('utf-8')
movie = set()
# 使用html.parser解析器，此外还有lxml解析器，xml解析器，html5lib解析器
soup = BeautifulSoup(text, 'html.parser')
# 获取li标签
print(soup.li)
# 获取标签属性
print(soup.li.attrs)
# for tag in soup('li'):
#     nameall = tag('a', 'reference')
#     if not nameall: continue
#     name = nameall[0]
#     movie.add(name)
# 查找类为title的li标签
lill = soup.find_all('li', class_ = 'title')
for nameall in lill:
    for name in nameall.find_all('a'):
        # 获取标签的文本域内容
        content = name.get_text()
        movie.add(content)
print(movie)

import webbrowser
from urllib.parse import urlencode
urlparam = urlencode({'name':'tbq'})
# 访问cgi脚本编写的服务器并自定义传入参数
# 构建较大型复杂网站服务器可以使用django，zope等框架
webbrowser.open('http://localhost/cgi-bin/test.cgi?'+urlparam)
# doctest测试工具，检测模块中的文档字符串
import doctest, test
# 会检查模块中所有的文档字符串，如文档字符串
# 包含'>>> func(x)'，则会检查这个例子在解释器中运行是否得到正确的结果
doctest.testmod(test)

# 单元测试工具unittest，还有专门针对unittest的GUI界面模块
import unittest, test

# 继承于TestCase
class myunitest(unittest.TestCase):
    def testone(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                result = test.func3(x,y)
                # 如果result == x*y不成立，则抛错
                # 此外还有其他错误抛出方法如failIf,assertEqual等
                self.failUnless(result == x*y, '失败1')

    def testtwo(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x/10.0
                y = y/10.0
                result = test.func3(x,y)
                self.failUnless(result == x*y, '失败2')

# main函数运行的时候会把TestCase的子类实例化，之后执行'test'开头的的所有方法
unittest.main()
"""
#---------------------------------------------------------------------------
# 代码规范检查工具pychecker, pylint会检查代码的语法，命名规范等
# 如定义x变量则会提示短变量，不是规范的命名
# 可以这样在命令行下使用pylint module，还可以在子进程中调用命令并输出检查结果
import unittest, test
from subprocess import Popen, PIPE
class myunitest2(unittest.TestCase):
    def testone(self):
        # -rn关闭其他报告信息，只显示错误与警告信息
        cmd = 'pylint', '-rn', 'test'
        pylint = Popen(cmd, stdout = PIPE, stderr = PIPE)
        # 如果检查结果为空，证明代码规范检查通过
        self.assertEqual(pylint.stdout.read(), '')

unittest.main()

# 代码运行分析工具，如分析运行次数，时间
import profile, test
# 检查某个函数运行所花时间
#profile.run('test.func3(1, 2)')
# 将检查结果保存至文件中
#profile.run('test.func3(1, 2)', 'test.profile')

import pstats
# pstats工具可以查看保存后的代码分析文件
p = pstats.Stats('test.profile')
print(p.print_stats())
