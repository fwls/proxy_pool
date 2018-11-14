from flask import Flask
import random
import redis
import config

app = Flask(__name__)

app.config['DEBUG'] = config.DEBUG

pool= redis.ConnectionPool(host=config.redis_host, port=config.redis_port, decode_responses=True)
r=redis.Redis(connection_pool=pool)

@app.route('/')
def index():
    ip_list = r.lrange('proxy', 1, config.max_ip)
    return random.choice(ip_list)

if __name__ == "__main__":
    app.run()