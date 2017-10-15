# -*- coding: utf-8 -*-
 
# Python 2.7 学习参考脚本
 
 
# print 打印函数
print "Hello World!"
 
 
 
 
### import ###
 
# 导入数学模块
import math
math.sqrt(25)
 
# 导入一个函数
from math import sqrt
sqrt(25)  # 没必要再引用模块的名字了
 
# 一次导入多个函数
from math import cos, floor
 
# 引入模块中的所有函数(不建议)
from os import *
 
# 引入模块并起别名
import numpy as np
 
# 显示math模块下的所有函数
dir(math)
 
 
 
 
### 数据类型 ###
 
# 判断一个对象的类型
type(2)        # 返回 'int'
type(2.0)      # 返回 'float'
type('two')    # 返回 'str'
type(True)     # 返回 'bool'
type(None)     # 返回 'NoneType'
 
# 检查一个对象是什么类型
isinstance(2.0, int)   # 返回 False
isinstance(2.0, (int, float))  # 返回 True
 
# 转换数据类型
float(2)
int(2.9)
str(2.9)
 
# 0，None，和空容器转为False
bool(0)
bool(None)
bool('')   # 空字符串
bool([])   # 空列表(list)
bool({})   # 空字典(dictionary)
 
# 非空容器和非0转为True
bool(2)
bool('two')
bool([2])
 
 
 
 
### Math ###
10 + 4    # 加法(14)
10 - 4    # 减法(6)
10 * 4    # 乘法(40)
10 ** 4   # 指数(10000)
10 / 4    # 除法(2, 因为两个数同为int类型)
10 / float(4)  # 除法(2.5)
5 % 4     # 求余(1)
 
# 在python 2.x 中强制做"真除法"（在Python 3.x中没有必要）
# from __future__ import division  # 放在文件头
# print 10 / 4   # 返回 2.5
10 // 4          # 返回 2
 
 
 
### 比较和bool运算 ###
# 全部返回True
5 > 3
5 >= 3
5 != 3
5 == 5
 
# bool 运算 全部返回True
5 > 3 and 6 > 3
5> 3 or 5 < 3
not False
False or not False and True  # 运算顺序为：not，and，or
 
 
 
 
### 控制语句 ###
 
# if 语句
x = 3
if x > 0:
	print '正数'
 
# if/else 语句
if x > 0:
	print '正数'
else:
	print '<= 0'
 
# if/elif/else 语句
if x > 0:
	print '正数'
elif x == 0:
	print '0'
else:
	print '负数'
 
# if 语句，放在一行（不建议）
if x > 0: print '正数'
# if/else 语句，放在一行 (不建议)
print '正数' if x > 0 else '<= 0'


# if判断条件还可以简写，比如：

if x:
    print('True')
	
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。 
 
 

 
 
### For 循环和 while循环
 
# range 返回整数列表
range(0, 3)   # [0, 1, 2]
range(3)      # 同上
range(0, 5, 2) # [0, 2, 4]  # 第三个参数跳跃
 
# for 循环（不建议)
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
	print fruits[i].upper()
 
# 建议
for fruit in fruits:
	print fruit.upper()
 
# 用 xrange 避免遍历大数组时创建 整数数组
for i in xrange(10 ** 6):
	pass
 
# 用元组解包一次遍历两个东西
family = {'dad':'homer', 'mom':'marge', 'size':6}
for key, value in family.items():
	print key, value
 
# 用枚举 如果你想在循环中用索引
for index, fruit in enumerate(fruits):
	print index, fruit
 
# for/else 循环
for fruit in fruits:
	if fruit == 'banana':
		print "I like banana"
		break
else:    # 只用当代码没有执行break时
	print "Can't find the banana"
 
# while 循环
count = 0
while count < 5:
	print count
	count += 1
 
# 例子
nums = [1, 2, 3, 4, 5]
cubes = []
for num in nums:
	cubes.append(num ** 3)
# 等价 comprehension
cubes = [num**3 for num in nums]
# ---------------------------------
cubes_of_even = []
for num in nums:
	if num % 2 == 0:
		cubes_of_even.append(num**3)
# 等价 comprehension
cubes_of_even = [num**3 for num in nums if num % 2 == 0]
# ---------------------------------
cubes_add_squares = []
for num in nums:
	if num % 2 == 0:
		cubes_add_squares.append(num**3)
	else:
		cubes_add_squares.append(num**2)
# 等价 comprehension
cubes_and_squares = [num**3 if num % 2 == 0 else num**2 for num in nums]
# ---------------------------------
matrix = [[1, 2], [3, 4]]
items = []
for row in matrix:
    for item in row:
        items.append(item)
# 等价 comprehension
items = [item for row in matrix
              for item in row]
# ---------------------------------
# set comprehension
fruits = ['apple', 'banana', 'cherry']
unique_lengths = {len(fruit) for fruit in fruits}   # {5, 6}
 
# dictionary comprehension
fruit_lengths = {fruit:len(fruit) for fruit in fruits}              # {'apple': 5, 'banana': 6, 'cherry': 6}
fruit_indices = {fruit:index for index, fruit in enumerate(fruits)} # {'apple': 0, 'banana': 1, 'cherry': 2}
 
 


break 和 continue

# break

# 在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：

n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

# 上面的代码可以打印出1~100。

# 如果要提前结束循环，可以用break语句：

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# 执行上面的代码可以看到，打印出1~10后，紧接着打印END，程序结束。

# 可见break的作用是提前结束循环。

# continue

# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。

n = 0
while n < 10:
    n = n + 1
    print(n)

# 上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue   # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

# 执行上面的代码可以看到，打印的不再是1～10，而是1，3，5，7，9。

# 可见continue的作用是提前结束本轮循环，并直接开始下一轮循环。

# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，开始下一轮循环。这两个语句通常都必须配合if语句使用。


 
### 列表list ###
 
# 创建一个空list (两种方法)
empty_list = []
empty_list = list()
 
# 创建一个list
simpsons = ['homer', 'marge', 'bart']
 
# 获取list元素
simpsons[0]
len(simpsons)   # 返回list长度(3)
 
# 修改list  (操作不会返回list)
simpsons.append('lisa')   # 在list尾插入元素  也可以append一个list
simpsons.extend(['itchy', 'scratchy'])  # 在list尾插入多个元素
# simpsons.append(['itchy', 'scratchy'])  # 比较和extend的区别
simpsons.insert(0, 'maggie')     # 在0索引处插入元素（把所有东西向右移）
simpsons.remove('bart')          # 查找第一元素然后删除
 
simpsons.pop(0)                  # 删除索引为0的元素并返回
del simpsons[0]                  # 同上，但是不返回
simpsons[0] = 'krusty'	         # 替换索引0的元素
 
#  用+号拼接list（比extend方法慢）
neighbors = simpsons + ['ned', 'rod', 'todd']  # simpsons 不变
 
# 在list中查找元素
simpsons.count('lisa')   # 计算元素的个数
simpsons.index('itchy')  # 返回第一元素的索引
 
# 分割list [开始：结束：跨步]
weekdays = ['mon', 'tues', 'wed', 'thurs', 'fri']
weekdays[0]      # 'mon'
weekdays[0:3]    # 'mon', 'tues', 'wed'
weekdays[:3]     # 'mon', 'tues', 'wed'
weekdays[3:]     # 'thurs', 'fri'
weekdays[-1]     # 'fri' 最后一个元素
weekdays[::2]    # 0,2,4   'mon' 'wed' 'fri'
weekdays[::-1]   # 倒序 (4, 3, 2, 1, 0)  'fri' 'thurs' 'wed' 'tues' 'mon'
 
#倒序
list(reversed(weekdays))
 
# 在原地排序
simpsons.sort()
simpsons.sort(reverse=True)  # 倒序
simpsons.sort(key=len)       # 通过key排序
 
 
# 返回一个排过序的列表（不修改原始列表）
sorted(simpsons)
sorted(simpsons, reverse=True)
sorted(simpsons, key=len)
 
# 在排过序的列表中插入一个元素，并保持排序状态
num = [10, 20, 40, 50]
from bisect import insort
insort(num, 30)
 
# 创建同一个列表的引用
same_num = num
same_num[0] = 0      # 修改一个，same_sum 和 sum 一起改了
 
# copy 一个列表（两种方法）
new_num = num[:]
new_num = list(num)
 
# 比较列表list
id(num) == id(same_num) # True
id(num) == id(new_num)  # False
num is same_num         # True
num is new_num          # False
num == same_num         # True
num == new_num          # True (他们的内容相同)
 
 
### 元组（Tuple） ###
# 和list相似，但是它不能改变大小
 
# 创建一个元组
digits = (0, 1, 'two')  # 创建一个元组
digits = tuple([0, 1, 'two'])  # 从list创建元组
zero = (0,)         # 逗号是必不可少的，它指定zero是一个元组,没有的话就是数字0了

# 如果要定义一个空的tuple，可以写成t = () 

# 访问元组数据
digits[2]   # 返回'two'
len(digits) #      3
digits.count(0)  # 0的个数 （1）
digits.index(1)  # 返回第一个1的索引(1)
 
# 元组里的元素不能修改
# digits[2] = 2  # 抛出一个错误
 
# 拼接元组
digits = digits + (3, 4)
 
# 创建一个重复元素的元组（通常和list一起使用）
(3, 4) * 2   # 返回（3，4，3，4）
 
# 排序一个元组列表
tens = [(20,60), (10, 40), (20, 30)]
sorted(tens)   # 按元组里的第一个元素排序，第一个元素相同，比较第二个
               # [(10, 40), (20, 30), (20, 60)]
 
# 元组解包
bart = ('male', 10, 'simpson')
(sex, age, surname) = bart   # 一次符三个值
 
 
 
 
 
### 字符串 ###


# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
# 在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
 
#创建一个字符串
s = str(42)   # 把其它类型的数据转化为string
s = 'I like you'
 
# 提取string
s[0]    # 返回 'I'
len(s)  # 返回 10
 
# 分割字符串
s[:6]    # 'I like'
s[7:]    # 'you'
s[-1]    # 'u'
 
# 基本的string方法 （不修改原string）
s.lower()    # 'i like you'
s.upper()    # 'I LIKE YOU'
s.startswith('I')   # True
s.endswith('you')    # True
s.isdigit()         # False (Ture:数字组成的字符串)
s.find('like')      # 2 索引
s.find('hate')      # -1 没有找到
s.replace('lkie', 'love')  # 替换 'like' 为 'love'
 
 
# 分割字符串
s.split(' ')  # ['I','like','you']
s.split()     # 同上
s2 = 'a, an, the'
s2.split(',')   # ['a',' an',' the']
 
# 把列表中的字符串连成一个字符串
stooges = ['larry','curly','moe']
' '.join(stooges)     # 'larry curly moe'
 
# 连接字符串
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4
s3 + ' ' + str(42) # 'The meaning of life is 42'
 
#移除字符串前后中的空白字符
s5 = '  ham and cheese  '
s5.strip()    # 'ham and cheese'
 
# 字符串替换
'raining %s and %s' % ('cat', 'dogs')    # 老方法
'raining {} and {}'.format('cats', 'dogs') # 新方法
'raining {arg1} and {arg2}'.format(arg1='cats', arg2='dogs')
 
# 字符串格式化
'pi is {:.2f}'.format(3.14159)   # 'pi is 3.14'
 
# normal string 和 raw string
print 'first linensecond line'
print r'first linenfirst line'
 
 
 
 
 
###  字典（dictionaries） ###

# 由key-value对组成
# key是唯一的，可以是string，数字，元组
# values 可以是任何值
 
# 创建一个空字典（两种方法）
empty_dict = {}
empty_dict = dict()
 
# 创建一个字典（两种方法）
family = {'dad':'homer', 'mom':'marge', 'size':6}
family = dict(dad='homer', mom='marge', size=6)
 
# 把元组列表转化为字典
list_of_tuples = [('dad','homer'), ('mom','marge'), ('size', 6)]
family = dict(list_of_tuples)
 
# 获取字典元素
family['dad']   # 'homer'
len(family)     # 3
family.keys()   # ['dad', 'mom', 'size']
family.values() # ['homer', 'marge', 6]
family.items()  # [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
'mom' in family # Ture
'marge' in family # False (只判断key)
 
# 修改字典
family['cat'] = 'snowball'  # 增加一个新纪录
family['cat'] = 'snowball ii' # 编辑一个以存在的记录
del family['cat']         # 删除一个记录
family['kids'] = ['bart', 'lisa']  # 值可以是列表
family.pop('dad')          # 删除一个记录并返回值
family.update({'baby':'maggie', 'grandpa':'abe'}) # 增加多个记录
 
family['mom']   # 'marge'
family.get('mom') # 同上
#family['grandma']  # 抛出错误
family.get('grandma')  # 返回None
family.get('grandma', 'not found')  # 'not found'
 
family['kids'][0]   # 'bart'
family['kids'].remove('lisa')   # 移除'lisa'
 
# 用字典替换字符串
'youngest child is %(baby)s' % family   # 'youngest child is maggie'
 
 
 
 
 
### set  ###
# 无重复集合
 
# 创建空set
empty_set = set()
 
# 创建集合
languages = {'python', 'r', 'java'}
snakes = set(['cobra', 'viper', 'python'])
 
len(languages)  # 3
'python' in languages   # True
 
# set 操作
languages & snakes # 两个集合的交集  ｛'python'｝
languages | snakes # 联合   {'cobra', 'r', 'java', 'viper', 'python'}
languages - snakes # {'r', 'java'}
snakes - languages # {'cobra', 'viper'}
 
# 修改集合
languages.add('sql')   # 增加一个元素
languages.add('r')     # 试图增加一个以存在的元素，忽略，没有错误
languages.remove('java') # 移除一个元素
#languages.remove('c')    # 试图移除一个不存在的元素，抛出错误
languages.discard('c')   # 移除一个存在的元素，如果不存在，忽略
languages.pop()          # 移除并返回元素
languages.clear()        # 清空集合
languages.update('go', 'spark') # 增加多个元素
 
# 排序
sorted(set([9, 0, 2, 1, 0]))  # [0, 1, 2, 9]   去重排序

 
 
 
### 定义函数 ###
 
# 定义一个没有参数和返回值的函数
def print_text():
	print 'you are dumb'
 
# 调用一个函数
print_text()
 
# 定义一个有一个参数没有返回值的函数
def print_this(x):
	print x
 
# 调用
print_this(4)  # 4
n = print_this(4)  # 打印4，但是不会给n赋值
 
# 定义一个一个参数和返回值的函数
def square_this(x):
	return x ** 2
 
# 带函数描述
def square_this(x):
	""" Return the square of number."""
	return x ** 2
 
square_this(3)
var = square_this(3) # var = 9
 
# 带默认参数的函数
def calc(a, b, op='add'):
	if op == 'add':
		return a + b
	elif op == 'sub':
		return a -b
	else:
		print 'no op'
 
# 调用
calc(10, 4, op='add')   # 14
calc(10, 4, 'add')      # 14
calc(10, 4)             # 14
calc(10, 4, 'sub')      # 6
calc(10, 4, 'div')      # 'no op'
 
 
# 用 pass 写一个没有函数体的函数,它只是一个占位符
def stub():
	pass
 
# 一个函数返回2个值
def min_max(nums):
	return min(nums), max(nums)
 
nums = [1, 2, 3]
min_max_num = min_max(nums)  #  min_max_num = (1,3)  元组
min_num, max_num = min_max(nums) # min_num = 1,max_num = 3,  元组解包
 
 
 
 
# 数据类型转换

# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：

>>> int('123')
123
>>> int(12.34)
12
>>> float('12.34')
12.34
>>> str(1.23)
'1.23'
>>> str(100)
'100'
>>> bool(1)
True
>>> bool('')
False 



 
### 匿名函数（Lambda）###
 
# 普通方式定义函数
def squared(x):
	return x ** 2
 
# lamba
squared = lambda x : x ** 2
 
# 通过最后的字符排列字符串（不用lambda）
simpsons = ['homer', 'marge', 'bart']
def last_letter(word):
	return word[-1]
sorted(simpsons, key=last_letter)
# 用lambda
sorted(simpsons, key=lambda word : word[-1])
 
 
   
 
### map reduce  filter ###
 
# 'map'把一个操作应用到所有元素上
simpsons = ['homer', 'marge', 'bart']
map(len, simpsons)   # 求每个元素的长度 [5, 5, 4]
map(lambda word: word[-1], simpsons)  # ['r', 'e', 't']
# 等价
[len(word) for word in simpsons]
[word[-1] for word in simpsons]
 
 
# 先把前两个元素执行某个函数,求的结果，依次计算
reduce(lambda x,y: x + y, range(4)  # (((0+1)+2)+3) = 6
 
# 用指定函数过滤
filter(lambda x: x % 2 == 0, range(5))  # [0, 2, 4]




列表生成式


# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：

>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：

>>> L = []
>>> for x in range(1, 11):
...    L.append(x * x)
...
>>> L
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：

>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]

# 还可以使用两层循环，可以生成全排列：

>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 三层和三层以上的循环就很少用到了。

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

>>> import os # 导入os模块，模块的概念后面讲到
>>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：

>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> for k, v in d.items():
...     print(k, '=', v)
...
y = B
x = A
z = C

# 因此，列表生成式也可以使用两个变量来生成list：

>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']

# 最后把一个list中所有的字符串变成小写：

>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']


匿名函数


>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
[1, 4, 9, 16, 25, 36, 49, 64, 81]


# 匿名函数赋值给一个变量，再利用变量来调用该函数。

>>> f = lambda x: x * x
>>> f
<function <lambda> at 0x101c6ef28>
>>> f(5)
25


# 匿名函数作为返回值返回。

def build(x, y):
    return lambda: x * x + y * y

		

	
偏函数


# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85




查看python已经安装的模块

# 进入python，执行

>>> help('modules')




Python 中拷贝列表（list）的方法


# 一：非常奇怪的语法

new_list = old_list[:]

# 二：内建list()函数

new_list = list(old_list)

# 三：copy

# 这个要比list()慢一点，因为它要找到old_list的类型

import copy

new_list = copy.copy(old_list)

# 四：最慢和最消耗内存的方法，但是有时是必须的

import copy

new_list = copy.deepcopy(old_list


# 从 Python 列表（list）中随机选择一个元素

import random

foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))




# 查找指定目录下的指定文件

import os

def find_files(substring, path):
    results = []
    for f in os.listdir(path):
        if substring in f:
            results.append(os.path.join(path, f))
    return results

# 使用示例：
# find_files('Untitled', '/Users/sebastian/Desktop/')
# 返回 ['/Users/sebastian/Desktop/Untitled0.ipynb']




# 基本目录文件操作


import os
import shutil
import glob

# working directory
c_dir = os.getcwd()                 # show current working directory
os.listdir(c_dir)                   # shows all files in the working directory
os.chdir('~/Data')                  # change working directory


# get all files in a directory
glob.glob('/Users/sebastian/Desktop/*')

# e.g.,  ['/Users/sebastian/Desktop/untitled folder', '/Users/sebastian/Desktop/Untitled.txt']

# walk
tree = os.walk(c_dir)
# moves through sub directories and creates a 'generator' object of tuples
# ('dir', [file1, file2, ...] [subdirectory1, subdirectory2, ...]),
#    (...), ...

#check files: returns either True or False
os.exists('../rel_path')
os.exists('/home/abs_path')
os.isfile('./file.txt')
os.isdir('./subdir')


# file permission (True or False
os.access('./some_file', os.F_OK) # File exists? Python 2.7
os.access('./some_file', os.R_OK) # Ok to read? Python 2.7
os.access('./some_file', os.W_OK) # Ok to write? Python 2.7
os.access('./some_file', os.X_OK) # Ok to execute? Python 2.7
os.access('./some_file', os.X_OK | os.W_OK) # Ok to execute or write? Python 2.7

# join (creates operating system dependent paths)
os.path.join('a', 'b', 'c')
# 'a/b/c' on Unix/Linux
# 'a\b\c' on Windows
os.path.normpath('a/b/c') # converts file separators


# os.path: direcory and file names
os.path.samefile('./some_file', '/home/some_file')  # True if those are the same
os.path.dirname('./some_file')  # returns '.' (everythin but last component)
os.path.basename('./some_file') # returns 'some_file' (only last component
os.path.split('./some_file') # returns (dirname, basename) or ('.', 'some_file)
os.path.splitext('./some_file.txt') # returns ('./some_file', '.txt')
os.path.splitdrive('./some_file.txt') # returns ('', './some_file.txt')
os.path.isabs('./some_file.txt') # returns False (not an absolute path)
os.path.abspath('./some_file.txt')


# create and delete files and directories
os.mkdir('./test')  # create a new direcotory
os.rmdir('./test')  # removes an empty direcotory
os.removedirs('./test') # removes nested empty directories
os.remove('file.txt')   # removes an individual file
shutil.rmtree('./test') # removes directory (empty or not empty)

os.rename('./dir_before', './renamed') # renames directory if destination doesn't exist
shutil.move('./dir_before', './renamed') # renames directory always

shutil.copytree('./orig', './copy') # copies a directory recursively
shutil.copyfile('file', 'copy')     # copies a file


# Getting files of particular type from directory
files = [f for f in os.listdir(s_pdb_dir) if f.endswith(".txt")]

# Copy and move
shutil.copyfile("/path/to/file", "/path/to/new/file")
shutil.copy("/path/to/file", "/path/to/directory")
shutil.move("/path/to/file","/path/to/directory")

# Check if file or directory exists
os.path.exists("file or directory")
os.path.isfile("file")
os.path.isdir("directory")

# Working directory and absolute path to files
os.getcwd()
os.path.abspath("file")




# 基本文件读


# Note: rb opens file in binary mode to avoid issues with Windows systems
# where 'rn' is used instead of 'n' as newline character(s).


# A) Reading in Byte chunks
reader_a = open("file.txt", "rb")
chunks = []
data = reader_a.read(64)  # reads first 64 bytes
while data != "":
    chunks.append(data)
    data = reader_a.read(64)
if data:
    chunks.append(data)
print(len(chunks))
reader_a.close()


# B) Reading whole file at once into a list of lines
with open("file.txt", "rb") as reader_b:   # recommended syntax, auto closes
    data = reader_b.readlines() # data is assigned a list of lines
print(len(data))


# C) Reading whole file at once into a string
with open("file.txt", "rb") as reader_c:
    data = reader_c.read() # data is assigned a list of lines
print(len(data))


# D) Reading line by line into a list
data = []
with open("file.txt", "rb") as reader_d:
    for line in reader_d:
        data.append(line)
print(len(data))




# 脚本的运行时间


import time

start_time = time.clock()

for i in range(10000000):
    pass

elapsed_time = time.clock() - start_time
print("Time elapsed: {} seconds".format(elapsed_time))



# Python 生成随机字符串


import string
import random

def rand_string(length):
    """ 生成由数字大小写字母组成的字符串 """
    return ''.join(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits)
                   for i in range(length)
            )

if __name__ == '__main__':
    print("Example1:", rand_string(length=4))
    print("Example2:", rand_string(length=8))
    print("Example2:", rand_string(length=16))


# Example1: 5bVL
# Example2: oIIg37xl
# Example2: 7IqDbrf506TatFO9	



# enumerate

例如将一个list变成list2index可以用dict([(x, i) for i, x in enumerate(list_x)])