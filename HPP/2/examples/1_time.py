import numpy as np
import time

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
    start = time.time()
    assert pure() == 4950
    stop  = time.time()
    print('pure:', start-stop)
    start = time.time()
    assert su()   == 4950
    stop  = time.time()
    print('su  :', start-stop)
    start = time.time()
    assert num()  == 4950
    stop  = time.time()
    print('num :', start-stop)


if __name__ == "__main__":
    # Calculate the Julia set using a pure Python solution with
    # reasonable defaults for a laptop
    m()