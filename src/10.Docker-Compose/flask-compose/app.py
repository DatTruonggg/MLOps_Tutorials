from flask import Flask
import time 
import redis
import redis.exceptions

app = Flask(__name__)
cache = redis.Redis(host="redis", port = 6379)

def get_hit_count():
    retries = 5
    while True:
        try: 
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries ==0:
                raise exc
            retries -=1
            time.sleep(0.5)

@app.route("/")
def hello():
    count = get_hit_count()
    return f"hello world from Docker, this is MLops course, and  I have seen thiss {count} time"
