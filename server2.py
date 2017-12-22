# coding=utf-8

import os.path
import tornado.ioloop
import tornado.web
import tornado.web
from tornado.options import define, options
from tornado.options import options, define

define("port", default=8080, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html') #返回模版页面


class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,
                difference=noun3)

class testHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html', header_text = "Header goes here",
         footer_text = "Footer goes here")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/poem', PoemPageHandler), (r'/test', testHandler)], # handlers a tuple for url routes
        template_path=os.path.join(os.path.dirname(__file__), "templates"),  # templates_path dir
        static_path = os.path.join(os.path.dirname(__file__), "static"),   # static files path
        debug = True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    print("the Server is running...")
    try:
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()  #开启IO loop 实例
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
        http_server.stop()
        print("the Server is closing...")





