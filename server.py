import tornado.ioloop
import tornado.web
import tornado.web
from tornado.options import define, options

define("port", default=8080, help="given port", type=int)

class IndexHander(tornado.web.RequestHandler):

    def get(self):
        args = self.get_argument('greet', "anonymous") #接收参数
        self.write("hello,"+args+"!")  # 写响应

    def post(self):
        args = self.get_argument('greet', "anonymous")
        self.write("post!"+args) 

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHander)   #route规则
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    print("the Server is running...")
    try:
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()  #开启IO loop 实例
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
        http_server.stop()
        print("the Server is closing...")

