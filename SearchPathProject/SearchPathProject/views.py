import pandas as pd
from django.http import HttpResponse
import sys
import os
import json
from SearchPathProject.enter import func
import enter
from demo1.demo6 import *
import demo2.demo4
# from demo1.demo6 import *

# 不可以是文件
# print(demo2.demo4)


def hello(request):
    return HttpResponse("Hello world ! ")


# def enter(request):
#     result = {"result": 0, "msg": "trend_alarm_case1执行成功", "data": func()}
#     return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


def demo1(request):
    result = {"result": 0, "msg": "trend_alarm_case1执行成功",
              "data": enter.func()}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")
