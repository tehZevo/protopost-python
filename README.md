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

### Client
```python
from protopost import protopost_client as ppcl

ppcl("http://127.0.0.1/foobar/foo") #hello foo
```

## TODO
* exception handling (status 400/500)
