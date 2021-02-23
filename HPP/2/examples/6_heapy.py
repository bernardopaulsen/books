from guppy import hpy; hp = hpy()
import numpy as np


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
    pure()
    print("heapy after pure()")
    h = hp.heap()
    print(h)
    su()
    print("heapy after su()")
    h = hp.heap()
    print(h)
    num()
    print("heapy after num()")
    h = hp.heap()
    print(h)

if __name__ == "__main__":
    m()