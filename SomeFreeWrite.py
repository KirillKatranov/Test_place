
import time


def measure_time(parametr):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func()
            end = time.time()
            return end - start
        return wrapper
    return real_decorator


@measure_time(parametr1 = "some_string")    #some_func = measure_time(parametr="some_string")(some_func)
def some_func(*args, **kwargs):
    time.sleep(5)
    print("Я функция")

if __name__ == "__main__":

    print(some_func(), "сек")