
import json

import tornado.ioloop
import tornado.web

import config

class BaseHandler(tornado.web.RequestHandler):
    pass


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        data = dict(hello='world')
        self.write(json.dumps(data))


class Upload(BaseHandler):
    pass





def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": config.static_path}),
    ], debug=config.debug)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
