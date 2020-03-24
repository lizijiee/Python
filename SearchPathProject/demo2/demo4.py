import sys
import os
# sys.path.insert(0,'C:\\Users\\李子杰\\AppData\\Roaming\\Python\\Python38\\site-packages')
# sys.path.append('C:\\Users\\李子杰\\AppData\\Roaming\\Python\\Python38\\site-packages')
# sys.path.insert(0,'D:\\工作\\项目文件\\github下载\\Python\\SearchPathProject')
# sys.path.append('D:\\工作\\项目文件\\github下载\\Python\\SearchPathProject')
import six
# import demo2
# sys.path.append('D:\工作\项目文件\github下载\Python\SearchPathProject\demo2')
# import demo3.demo2_1
# from . import demo2

# from . import demo3.demo2  报错格式错误
# from .demo3.demo2 import func2  正确书写方式

# print(sys.path)
print(sys.path, six)


# from __future__ import absolute_import
# from __future__ import absolute
# import string
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(
__file__, __name__, str(__package__)))

# print(demo3)


def func():
    return "demo4进入执行"
