#Позиционные аргументы не могут стоять после kwargs аргументов

def my_print(*args, c, b):
    print(args)
    print(c)
    print(b)
    #print(kwargs)
    #print(**kwargs)


if __name__ == "__main__":
    my_print(1, c=2, b=3)

