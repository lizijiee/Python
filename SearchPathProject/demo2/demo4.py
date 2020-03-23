import sys
import os

# sys.path.append('D:\工作\项目文件\github下载\Python\SearchPathProject\demo2')
print(sys.path)

from . import demo2


# from __future__ import absolute_import
# from __future__ import absolute
# import string
# print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(
# __file__, __name__, str(__package__)))

# print(demo3)
print(demo2)


def func():
    return "demo4进入执行"
