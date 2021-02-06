from fastapi import FastAPI, Request
import uvicorn
import requests

def wrap_protopost(f):
    async def foo(request: Request):
        return f(await request.json())
    return foo


class ProtoPost:
    def __init__(self, routes={}):
        self.app = FastAPI()
        #self.api = Api(self.app)

        self.create_routes(routes)

    def create_routes(self, routes, path=""):
        for k, v in routes.items():
            fullpath = path + "/" + k
            if type(v) == dict:
                self.create_routes(v, fullpath)
            else:
                #self.api.add_resource(ProtoPostResource, fullpath, resource_class_args=[v], endpoint=fullpath)
                self.app.post(fullpath)(wrap_protopost(v))

    def start(self, port=80, logging=False):
        if not logging:
            self.disable_logging()

        uvicorn.run(self.app, host="0.0.0.0", port=port, access_log=False)

    def disable_logging(self):
        import logging
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

def protopost_client(url, data={}):
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
