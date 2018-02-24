#!-*-coding:utf-8-*-
import time
import json
import os
import logging
import tornado.web
import tornado

import uuid
from PIL import Image  

from etc import config
from lib.baiduOCRApi import parse_result, parse_result_table,parse_result_sync
# serializer for JWT
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# exceptions for JWT
from itsdangerous import SignatureExpired, BadSignature, BadData
# Class xxx
#
logger = logging.getLogger(__name__)

class BaseHandler(tornado.web.RequestHandler):
    
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    
    
    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        data = dict(hello='world')
        logger.info(data)
        # self.write(json.dumps(data))
        self.render("index.html")

class Upload(BaseHandler):

    def get(self):
        self.render("OCRupload.html")
    
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        # 文件的暂存路径
        upload_path = config.upload_path
        # 提取表单中‘name’为‘file’的文件元数据
        file_metas = self.request.files['file']
        for meta in file_metas:
            filename = meta['filename']
            file_stmt = filename.split(".")
            file_type = file_stmt[-1]
            if file_type not in config.upload_file_type:
                self.write("file type is not allow")
                return
            filepath = os.path.join(upload_path, filename)
            # 有些文件需要已二进制的形式存储，实际中可以更改
            with open(filepath, 'wb') as up:
                up.write(meta['body'])
            # result = parse_result(upload_path, filename)

            # result = parse_result_table(upload_path, filename)
            # self.write(result)
            response = yield tornado.gen.Task(parse_result_sync, upload_path, filename)
            self.render("OCRresponse.html",result=response)
            # self.finish('hello')



class UploadImg(BaseHandler):

    def get(self):
        self.render("upload_img.html")

    def post(self):
        # 文件的暂存路径
        upload_path = config.upload_img
        # 提取表单中‘name’为‘file’的文件元数据
        file_metas = self.request.files['file']
        size = self.get_body_argument("size")
        for meta in file_metas:
            filename = meta['filename']
            file_stmt = filename.split(".")
            file_type = file_stmt[-1]
            if file_type not in config.upload_file_type:
                self.write("file type is not allow")
                return
            filename = str(int(time.time())) + "." + file_type 
                # filename = file_name_add + "." + file_type
            filepath = os.path.join(upload_path, filename)
            # 有些文件需要已二进制的形式存储，实际中可以更改
            with open(filepath, 'wb') as up:
                up.write(meta['body'])
            if size != "100":
                img = Image.open(filepath) 
                (x, y) = img.size
                x_size = x * int(size) * 0.01
                y_size = y * int(size) * 0.01
                out = img.resize((int(x_size), int(y_size)), Image.ANTIALIAS)
                out.save(filepath)
            static_path = "/static/upload/"+filename
            url = config.img_host+ static_path
            return self.render("upload_resp.html",img_url = url,src=static_path)

class UploadSizeImg(BaseHandler):

    def get(self):
        self.render("upload_size_img.html")

    def post(self):
        # 文件的暂存路径
        upload_path = config.upload_img
        # 提取表单中‘name’为‘file’的文件元数据
        file_metas = self.request.files['file']
        size = self.get_body_argument("size")
        for meta in file_metas:
            filename = meta['filename']
            file_stmt = filename.split(".")
            file_type = file_stmt[-1]
            if file_type not in config.upload_file_type:
                self.write("file type is not allow")
                return
            filename = str(int(time.time())) + "." + file_type 
                # filename = file_name_add + "." + file_type
            filepath = os.path.join(upload_path, filename)
            # 有些文件需要已二进制的形式存储，实际中可以更改
            with open(filepath, 'wb') as up:
                up.write(meta['body'])
            if size != "100":
                img = Image.open(filepath) 
                (x, y) = img.size
                x_size = x * int(size) * 0.01
                y_size = y * int(size) * 0.01
                out = img.resize((int(x_size), int(y_size)), Image.ANTIALIAS)
                out.save(filepath)
            static_path = "/static/upload/"+filename
            url = config.img_host+ static_path
            return self.render("upload_resp.html",img_url = url,src=static_path)



class DownLoad(BaseHandler):
    pass

