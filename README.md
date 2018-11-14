# proxy_pool
___
#### 简易代理地址池
    语言依赖 python3.6及以上
    可改写获取代理函数以定制
___
#### CentOS7
```
    yum -y install redis python36-devel python36-setuptools
    echo 'bind 0.0.0.0' > /etc/redis.conf
    python36 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    修改配置文件 config.py
    python run.py
```
___
#### Ubuntu 18.04
```
    sudo apt update
    sudo apt -y install redis python3-venv python3-dev
    sudo echo 'bind 0.0.0.0' > /etc/redis/redis.conf
    sudo python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    修改配置文件 config.py
    python run.py
```
___
