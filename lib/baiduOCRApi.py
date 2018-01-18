# -*- coding: UTF-8 -*-

import tornado

from lib.OCRApiExt import ExtAipOcr

from etc.config import baidu_OCR, os_env
import json




APP_ID = baidu_OCR['APP_ID']
API_KEY = baidu_OCR['API_KEY']
SECRET_KEY = baidu_OCR['SECRET_KEY']

# 读取图片

def file_path(path, filename):
    if os_env == "win":
        filePath = path + "\\" + filename
    elif os_env == "linux":
        filePath = path + "/" + filename
    return filePath

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 初始化ApiOcr对象
aipOcr = ExtAipOcr(APP_ID, API_KEY, SECRET_KEY)

# 调用通用文字识别接口
# result = aipOcr.basicGeneral(get_file_content('general.jpg'))


def parse_result(path, filename):
    """解析返回结果"""
    data = "<li>"
    filePath = file_path( path ,filename)
    result = aipOcr.basicGeneral(get_file_content(filePath))
    print(result)
    if  result["words_result_num"] == 0:
        return u"无法识别"
    words_results = result['words_result']
    for word_info in words_results:
        words = word_info['words']
        data += words
        data += "<li\>"
        data += "<li>"
    return data + "<li\>"

@tornado.gen.coroutine
def parse_result_sync(path, filename):
    """解析返回结果"""
    data = "<li>"
    filePath = file_path( path ,filename)
    result = aipOcr.basicGeneral(get_file_content(filePath))
    if  result.get("words_result_num",0) == 0:
        return u"无法识别"
    words_results = result['words_result']
    for word_info in words_results:
        words = word_info['words']
        data += words
        data += "<li\>"
        data += "<li>"
    return data + "<li\>"

def parse_result_table(path,filename):
    """处理表格图片"""
    filePath = file_path( path ,filename)
    data = aipOcr.testurl(get_file_content(filePath))
    print(data)
    return data
