import config
from app.main import app
from app.proxy import check
from multiprocessing import Process

def start_web():
    # app.run(host=config.host, port=config.port)
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer((config.host, config.port), app)
    http_server.serve_forever()


def start_proxy(url):
    check(url)

def main():
    url = config.url
    p1 = Process(target=start_proxy, args=(url,))
    p2 = Process(target=start_web)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == "__main__":
    main()