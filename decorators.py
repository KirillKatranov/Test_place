import time
from functools import wraps


def logger(func):
    def wrapper(*args):
        print(func.__name__)
        for arg in args:
            print(arg)
        result = func(*args)
        return result
    
    return wrapper

def timing(func):
    def wrapper(*args):
        start = time.time()
        time.sleep(5)
        result = func(*args)
        end = time.time()
        print(f"Время выполнения функции: {end - start}")
        return result
    return wrapper

def caching_result(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            return cache[key]
        cache[key] = func(*args, **kwargs)
        result = cache[key]
        return result
    return wrapper


@caching_result # sum = cashing_result(sum) + словарь cashe
def sum(a,b):
    return a + b

@caching_result
def sum(a, b):
    return a + b 

@caching_result
def slow_mul(a, b):
    print(f"Computing {a} * {b}")
    return a * b

if __name__ == "__main__":
    print(slow_mul(2, 3))         # Computing 2 * 3
    print(slow_mul(2, 3))         # (из кэша)
    print(slow_mul(a=2, b=3))     # (тоже из кэша)
    print(slow_mul(b=3, a=2))     # (и это из кэша)