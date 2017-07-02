# -*- coding: UTF-8 -*-
import json
import os

import tornado.ioloop
import tornado.web

from etc import config
from lib.baiduOCRApi import parse_result,parse_result_table

class BaseHandler(tornado.web.RequestHandler):
    pass


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        data = dict(hello='world')
        self.write(json.dumps(data))


class Upload(BaseHandler):
    def get(self):
        self.write('''
        <html>
          <head><title>Upload File</title></head>
          <body>
            <form action='upload' enctype="multipart/form-data" method='post'>
            <input type='file' name='file'/><br/>
            <input type='submit' value='submit'/>
            </form>
          </body>
        </html>
        ''')

    def post(self):
        #文件的暂存路径
        upload_path=config.upload_path
        #提取表单中‘name’为‘file’的文件元数据
        file_metas=self.request.files['file']    
        for meta in file_metas:
            filename=meta['filename']
            filepath=os.path.join(upload_path,filename)
            #有些文件需要已二进制的形式存储，实际中可以更改
            with open(filepath,'wb') as up:      
                up.write(meta['body'])
            result = parse_result(upload_path, filename)

            # result = parse_result_table(upload_path, filename)
            self.write(result)


class DownLoad(BaseHandler):
    pass





def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": config.static_path}),
        (r"/upload", Upload),
    ], debug=config.debug)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
