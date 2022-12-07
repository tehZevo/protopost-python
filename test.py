from protopost import ProtoPost
from protopost import protopost_client as ppcl
import requests
import threading
import time

routes = {
    "echo": lambda data: data,
}

PORT = 8121
N = 1000

threading.Thread(target=lambda: ProtoPost(routes).start(PORT), daemon=True).start()

session = requests.Session()
time.sleep(2)
start_time = time.time()
for i in range(N):
    ppcl("{}/echo".format(PORT), {"hello": "world"})

dt = time.time() - start_time
print("took", dt, "seconds")
print(1000 / dt, "per second")
