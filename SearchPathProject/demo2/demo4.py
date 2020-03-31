import sys
import os
# sys.path.insert(0,'C:\\Users\\李子杰\\AppData\\Roaming\\Python\\Python38\\site-packages')
# sys.path.append('C:\\Users\\李子杰\\AppData\\Roaming\\Python\\Python38\\site-packages')
# sys.path.insert(0,'D:\\工作\\项目文件\\github下载\\Python\\SearchPathProject\\demo2')
# import six
# import demo3

# sys.path.append('D:\工作\项目文件\github下载\Python\SearchPathProject\demo2')
# import demo3.demo2_1

# import demo2
# from demo3.six import func6
# print( '__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(
#     __file__, __name__, str(__package__)))
# from demo3 import demo7
from demo1 import demo6
print(demo6.func())
# import six
# print(sys.path,six)
# from . import six
# 报错格式错误


# import six
# print(3333,six)

# from .demo3.demo2 import func2  正确书写方式

# print('__name__', demo2)
# print(sys.path, six)


# from __future__ import absolute_import
# from __future__ import absolute
# import string


# print(demo3)


def func():
    return "demo4进入执行"
