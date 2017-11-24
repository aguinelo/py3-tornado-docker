import tornado.web
import tornado.ioloop
import tornado.httpserver

class DefaultHandler(tornado.web.RequestHandler):
    def get(self, *args):
        self.write("Hello!")

application = tornado.web.Application([
    (r"/", DefaultHandler)
])

server = tornado.httpserver.HTTPServer(application)
server.listen(8001)
tornado.ioloop.IOLoop.instance().start()