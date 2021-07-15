import re

from flask import Flask, request
from flask_restful import Resource, Api
import requests

class ProtoPostResource(Resource):
    def __init__(self, f):
        self.f = f
    def post(self):
        data = request.get_json()
        result = self.f(data)
        return result

class ProtoPost:
    def __init__(self, routes={}):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.create_routes(routes)

    def create_routes(self, routes, path=""):
        for k, v in routes.items():
            fullpath = path + "/" + k
            if type(v) == dict:
                self.create_routes(v, fullpath)
            else:
                self.api.add_resource(ProtoPostResource, fullpath, resource_class_args=[v], endpoint=fullpath)

    def start(self, port=80, logging=False, threaded=True):
        if not logging:
            self.disable_logging()

        self.app.run(host="0.0.0.0", port=port, threaded=threaded)

    def disable_logging(self):
        import logging
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

#turn bare ports into 127.0.0.1:port and add http:// to urls that lack it
def sanitize_url(url):
    #if its just numbers then a slash
    if re.match(r"^\d+\/", url) or re.match(r"^\d+$/", url):
        return "http://127.0.0.1:" + url
    #if it lacks http
    if not re.match(r"^https?:\/\/", url):
        return "http://" + url

    return url

def protopost_client(url, data={}):
    url = sanitize_url(url)
    r = requests.post(url, json=data)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    import time

    routes = {
        "": lambda x: "Welcome to the api!",
        "ping": lambda x: time.time(),
        "foobar": {
            "": lambda x: "yes this is foobar",
            "foo": lambda x: "hello foo",
            "bar": lambda x: "hello bar"
        }
    }

    ProtoPost(routes).start(8000)
