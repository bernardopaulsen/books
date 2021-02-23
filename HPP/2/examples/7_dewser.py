import numpy as np

def launch_memory_usage_server(port=8080):
    import cherrypy
    import dowser
    cherrypy.tree.mount(dowser.Root())
    cherrypy.config.update({
    'environment': 'embedded',
    'server.socket_port': port
    })
    cherrypy.engine.start()

def pure():
    s = 0
    for i in range(100):
        s += i
    return s

def su():
    return sum(range(100))

def num():
    return np.sum(range(100))

def m():
    launch_memory_usage_server()
    pure()
    su()
    num()
    while True:
        time.sleep(1)

if __name__ == "__main__":
    m()