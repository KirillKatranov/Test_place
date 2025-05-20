x = 1 
def square(n=x):
    return x ** 2



if __name__ == "__main__":
    # x=2
    # square1 = lambda n = x: n**2
    # x=3
    # square2 = lambda n = x: n**2
    # print(square())
    # print(square1())
    # print(square2())
    ints =  range(10)
    for i in map(lambda x : x**2, filter(lambda x: x % 2 == 0, ints)):
        print(i)

