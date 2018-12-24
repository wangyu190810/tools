# -*- coding: UTF-8 -*-
import json
import os

import tornado.ioloop
import tornado.web

from views.base import MainHandler,Upload,UploadImg
from lib.LogUtil import addTimedRotatingFileHandler
from views.spider import spider_handler

from etc import config

settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        debug=config.debug,
) 


def make_app():
    handlers = [
        (r"/", MainHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": config.static_path}),
        (r"/upload", Upload),
        (r"/upload_img",UploadImg),
    ]
    handlers.extend(spider_handler)
    
    return tornado.web.Application(handlers, **settings)


if __name__ == "__main__":
    # path = os.path.abspath(__file__)
    addTimedRotatingFileHandler(config.log_path+"run.log",logLevel="INFO")
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
