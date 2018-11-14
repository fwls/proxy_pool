import random
import redis
import config
from app import r
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = config.DEBUG

@app.route('/')
def index():
    total_ip = r.llen('proxy')
    return f'''
        当前已有ip--->{total_ip}个，
        <br>
        获取随机ip---><a href='/random/'>random</a>
    '''

@app.route('/random/')
def random_ip():
    ip_list = r.lrange('proxy', 1, config.max_ip)
    print(type(ip_list))
    return random.choice(ip_list)

if __name__ == "__main__":
    app.run()