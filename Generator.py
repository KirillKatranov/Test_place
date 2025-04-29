import sys

def func():
    for i in range(5):
        yield i

if __name__ == "__main__":
    perem1 = [i for i in range(10000000)]
    perem2 = (i for i in range(10000000))
    print(sys.getsizeof(perem1))
    print(sys.getsizeof(perem2))
 