from functools import wraps
import numpy as np
import time

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print("@timefn:" + fn.__name__ + " took " + str(t2 - t1) + " seconds")
        return result
    return measure_time

@timefn
def pure():
    s = 0
    for i in range(100):
        s += i
    return s
@timefn
def su():
    return sum(range(100))
@timefn
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
    m()