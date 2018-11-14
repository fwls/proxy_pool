import requests
import json
import time
import gevent
import config
from app import r


def get_proxy(url):
    # url = 'http://www.lizihttp.com/index.php/Api/lian/hun?str=njYxaDVmVf44%2Bqw8O135dkl9u0Q9ibCDb47HmwQINwmcUbJzOkfcTYPJ1lw2pHbMyPuOKAEXFHOSHtcuxIqKvv5t8KtYry31U6GrYSGBY6%2FiMvJtHm1s7AzxWlJ93HqXH67mpE%2B4qlQlTy2e3GvgcQq8zJMWpfomYv8eW6F2In0Ce0hBkm7J0mJKWtmqAE1NKculMleUnVo1jVPmcan3hA%3D%3D'

    r1 = requests.get(url)
    if r1.status_code == 200:
        proxies= r1.content.decode('utf-8')
        proxies = json.loads(proxies)
        # print(type(proxies))
        # print(proxies)
        for proxy in proxies:
            r.lpush('proxy', proxy)

def test_proxy(ip):
    ip = eval(ip)
    proxies = { 
                'http': ip['http_ip'] + ':' + ip['http_port'],
                'https': ip['http_ip'] + ':' + ip['http_port'],
            }
    test_url = 'https://www.baidu.com'
    try:
        r1 = requests.get(url=config.test_url, proxies=proxies, timeout=config.timeout)
        if r1.status_code != 200:
            r.lrem('proxy', ip)
            print(f'ip{ip},已经失效')
    except:
        print(f'ip{ip},已经失效')
        r.lrem('proxy', ip)

def check(url):
    while True:
        # time.sleep(30)
        
        ip_list = r.lrange('proxy', 1, config.max_ip)
        test_list = []
        for r_id,ip in  enumerate(ip_list):

            test_list.append(gevent.spawn(test_proxy, ip))
            # print(r_id,type(ip))
        gevent.joinall(test_list)
        total_ip = r.llen('proxy')
        print('当前有效ip数量-->',total_ip)
        if  total_ip < 9:
            get_proxy(url)
        # print('1',r.lrange('proxy', 1,3))
    # print(type(r.lrange('proxy', 1,3)))



if __name__ == "__main__":
    url = 'http://www.lizihttp.com/index.php/Api/lian/hun?str=ty7zmfp0qnSO2tEy630n62149lp5mQ2n2y1pX0KK7fn6OcXtGPc0gxwgPV%2BX05q2DnBnjA0V%2Fk%2BaEOkCDYrLSenr5K5ImFZLu1FhFe8td6%2FyjUONM5u5jPNyLBN8UczOWx1o7atMdIYjAVe8%2BJI3FwwzeYFTjwjDBCUvQgDsYhlgKxFoNrp%2BRqPY%2FEUkYeteevnzncKMGBaFiblsAfdoHA%3D%3D'
    # get_proxy(url)
    check(url)