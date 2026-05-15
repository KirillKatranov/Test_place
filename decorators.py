import time
from functools import wraps

# Если замыкания не пересекаются, то декоратор оборачивает декорируемую функцию один раз и при любом 
# её псоледующем вызове хранит своё состояние
# Декоратор должен быть выше декорируемой функции
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
            print("Из кеша")
            return cache[key]
        print("Без кеша кеша")
        cache[key] = func(*args, **kwargs)
        result = cache[key]
        return result
    return wrapper


@caching_result # sum = cashing_result(sum) + словарь cache
def sum(a,b):
    return a + b

@caching_result
def slow_mul(a, b):
    print(f"Computing {a} * {b}")
    return a * b

if __name__ == "__main__":
    per = {'b': 3, 'a': 2}
    print(per.items())
    print(type(per.items()))
    print(sorted(per.items()))
    tup1 = (1, 2 ,3)
    print(tup1)
    print(type(tup1))
    print(set([1,2,3]))
    print(tuple([1,2,3]))
    per1 = sum(2, 3)
    per2 = sum(2, 3)
    per3 = sum(3, 3)
    per4 = sum(a=2, b=3)
    per5 = sum(b=3, a=2)


