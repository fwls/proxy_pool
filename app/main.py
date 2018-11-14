import random
import redis
import config
from app import r
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = config.DEBUG



@app.route('/')
def index():
    ip_list = r.lrange('proxy', 1, config.max_ip)
    return random.choice(ip_list)

if __name__ == "__main__":
    app.run()