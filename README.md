# ProtoPost (for Python)

Like [ProtoPost](https://github.com/tehzevo/protopost) but in Python.

## Usage
### Server
```python
from protopost import ProtoPost
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
```

*NOTE: also supports parameterization of routes, so the following should allow you to capture the full route:*
```
routes = {
  "<path:foo>": lambda data, foo: print(foo)
}
```
With this, `POST`ing to /hello/world will print `hello/world`.

### Client
```python
from protopost import protopost_client as ppcl

ppcl("http://127.0.0.1/foobar/foo") #hello foo
```
NOTE: this will create a requests Session object in hopes of faster requests

## TODO
* exception handling (status 400/500)
